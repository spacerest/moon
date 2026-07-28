from __future__ import annotations

from moon.dialamoon import Moon


class JupyterUi(Moon):
    """Moon subclass that adds a ``show()`` method for Jupyter notebooks.

    Requires the ``jupyter`` extra: ``pip install moon[jupyter]``.
    """

    def show(self) -> None:
        if self.image is None:
            raise RuntimeError("Call set_moon_phase() before show().")
        try:
            import matplotlib.pyplot as plt
        except ImportError as e:
            raise ImportError(
                "JupyterUi.show() requires matplotlib. "
                "Install with: pip install moon[jupyter]"
            ) from e
        plt.imshow(self.image)
        plt.axis("off")
        plt.show()
