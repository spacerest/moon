"""Integration tests that hit the real NASA Dial-a-Moon API.

Run with: pytest -m integration
"""
from __future__ import annotations

import numpy as np
import pytest

from moon import Moon


@pytest.mark.integration
def test_fetches_real_moon_phase():
    m = Moon()
    m.set_moon_phase(date="2025-03-14", hour=12)
    assert isinstance(m.image, np.ndarray)
    assert m.image.shape == (730, 730, 3)
    assert m.info is not None
    assert "phase" in m.info
