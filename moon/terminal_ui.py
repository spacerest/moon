from __future__ import annotations

import os
import shutil
import sys

import numpy as np

from moon.dialamoon import Moon

ASCII_RAMP = " .:-=+*#%@"


class TerminalUi(Moon):
    """Moon subclass that renders the image in the terminal.

    Uses Unicode half-blocks with 24-bit color when the terminal supports it,
    falls back to ASCII art otherwise. Force a mode with the ``mode`` argument
    to ``show()``: ``"blocks"``, ``"ascii"``, or ``"auto"`` (default).
    """

    def show(self, mode: str = "auto", width: int | None = None) -> None:
        if self.image is None:
            raise RuntimeError("Call set_moon_phase() before show().")
        if mode == "auto":
            mode = "blocks" if _supports_truecolor() else "ascii"
        if mode == "blocks":
            sys.stdout.write(_render_blocks(self.image, width))
        elif mode == "ascii":
            sys.stdout.write(_render_ascii(self.image, width))
        else:
            raise ValueError(f"unknown mode: {mode!r}")
        sys.stdout.write("\n")
        sys.stdout.flush()


def _terminal_width(default: int = 80) -> int:
    return shutil.get_terminal_size((default, 24)).columns


def _supports_truecolor() -> bool:
    if not sys.stdout.isatty():
        return False
    colorterm = os.environ.get("COLORTERM", "").lower()
    if colorterm in ("truecolor", "24bit"):
        return True
    term = os.environ.get("TERM", "").lower()
    return "kitty" in term or "iterm" in term or "alacritty" in term


def _resize(image: np.ndarray, target_w: int, target_h: int) -> np.ndarray:
    src_h, src_w = image.shape[:2]
    ys = (np.linspace(0, src_h - 1, target_h)).astype(np.int32)
    xs = (np.linspace(0, src_w - 1, target_w)).astype(np.int32)
    return image[ys][:, xs]


def _render_blocks(image: np.ndarray, width: int | None) -> str:
    src_h, src_w = image.shape[:2]
    cols = width or min(_terminal_width(), src_w)
    # Each terminal cell is ~2x taller than wide; each cell shows two vertical pixels.
    rows = max(2, int(cols * (src_h / src_w) * 0.5)) * 2
    small = _resize(image, cols, rows)
    lines = []
    for y in range(0, rows, 2):
        top = small[y]
        bot = small[y + 1]
        line = []
        for x in range(cols):
            tr, tg, tb = top[x]
            br, bg, bb = bot[x]
            line.append(
                f"\x1b[38;2;{tr};{tg};{tb}m\x1b[48;2;{br};{bg};{bb}m▀"
            )
        line.append("\x1b[0m")
        lines.append("".join(line))
    return "\n".join(lines)


def _render_ascii(image: np.ndarray, width: int | None) -> str:
    src_h, src_w = image.shape[:2]
    cols = width or min(_terminal_width(), src_w)
    rows = max(1, int(cols * (src_h / src_w) * 0.5))
    small = _resize(image, cols, rows)
    gray = (0.299 * small[..., 0] + 0.587 * small[..., 1] + 0.114 * small[..., 2])
    idx = np.clip((gray / 255 * (len(ASCII_RAMP) - 1)).astype(np.int32),
                  0, len(ASCII_RAMP) - 1)
    ramp = np.array(list(ASCII_RAMP))
    return "\n".join("".join(row) for row in ramp[idx])
