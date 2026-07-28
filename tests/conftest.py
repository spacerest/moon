from __future__ import annotations

from io import BytesIO

import pytest
import responses
from PIL import Image


@pytest.fixture
def mock_api():
    """Yield a responses.RequestsMock so tests can register fake API replies."""
    with responses.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def fake_jpeg_bytes() -> bytes:
    """A tiny valid JPEG for image-fetching tests."""
    buf = BytesIO()
    Image.new("RGB", (10, 10), color=(128, 128, 128)).save(buf, format="JPEG")
    return buf.getvalue()


def make_api_payload(
    timestamp: str = "2025-03-14T12:00",
    image_url: str = "https://example.test/moon.jpg",
) -> dict:
    return {
        "image": {
            "id": 1,
            "url": image_url,
            "filename": "moon.jpg",
            "media_type": "Image",
            "alt_text": "moon",
            "width": 730,
            "height": 730,
            "pixels": 532900,
        },
        "time": timestamp,
        "phase": 99.96,
        "obscuration": 0.0,
        "age": 14.469,
        "diameter": 1783.1,
        "distance": 401962.0,
        "j2000_ra": 11.7665,
        "j2000_dec": 1.6066,
        "subsolar_lon": 0.264,
        "subsolar_lat": -0.08,
        "subearth_lon": 2.606,
        "subearth_lat": -0.099,
        "posangle": 21.832,
    }
