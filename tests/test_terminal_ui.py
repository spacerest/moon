from __future__ import annotations

import pytest
import responses

from moon.dialamoon import DIALAMOON_API_URL
from moon.terminal_ui import TerminalUi

from .conftest import make_api_payload


def _register(mock_api, fake_jpeg_bytes):
    mock_api.add(
        responses.GET,
        DIALAMOON_API_URL.format(timestamp="2025-03-14T12:00"),
        json=make_api_payload(),
        status=200,
    )
    mock_api.add(
        responses.GET,
        "https://example.test/moon.jpg",
        body=fake_jpeg_bytes,
        status=200,
        content_type="image/jpeg",
    )


def test_show_ascii_writes_ramp_chars(mock_api, fake_jpeg_bytes, capsys):
    _register(mock_api, fake_jpeg_bytes)
    ui = TerminalUi(size=(60, 60))
    ui.set_moon_phase(date="2025-03-14", hour=12)
    ui.show(mode="ascii", width=20)

    out = capsys.readouterr().out
    lines = [ln for ln in out.splitlines() if ln]
    assert lines, "expected some output"
    assert all(len(ln) == 20 for ln in lines)
    assert all(c in " .:-=+*#%@" for ln in lines for c in ln)


def test_show_blocks_writes_ansi_and_half_blocks(mock_api, fake_jpeg_bytes, capsys):
    _register(mock_api, fake_jpeg_bytes)
    ui = TerminalUi(size=(60, 60))
    ui.set_moon_phase(date="2025-03-14", hour=12)
    ui.show(mode="blocks", width=20)

    out = capsys.readouterr().out
    assert "▀" in out
    assert "\x1b[38;2;" in out  # truecolor foreground
    assert "\x1b[48;2;" in out  # truecolor background
    assert "\x1b[0m" in out     # reset


def test_show_before_fetch_raises():
    ui = TerminalUi()
    with pytest.raises(RuntimeError):
        ui.show()


def test_show_unknown_mode_raises(mock_api, fake_jpeg_bytes):
    _register(mock_api, fake_jpeg_bytes)
    ui = TerminalUi(size=(60, 60))
    ui.set_moon_phase(date="2025-03-14", hour=12)
    with pytest.raises(ValueError):
        ui.show(mode="hologram")
