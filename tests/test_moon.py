from __future__ import annotations

from datetime import timezone

import numpy as np
import pytest
import responses

from moon import Moon
from moon.dialamoon import DIALAMOON_API_URL

from .conftest import make_api_payload


def test_set_moon_phase_populates_all_fields(mock_api, fake_jpeg_bytes):
    payload = make_api_payload()
    mock_api.add(
        responses.GET,
        DIALAMOON_API_URL.format(timestamp="2025-03-14T12:00"),
        json=payload,
        status=200,
    )
    mock_api.add(
        responses.GET,
        "https://example.test/moon.jpg",
        body=fake_jpeg_bytes,
        status=200,
        content_type="image/jpeg",
    )

    m = Moon()
    m.set_moon_phase(date="2025-03-14", hour=12)

    assert m.requested_datetime is not None
    assert m.requested_datetime.tzinfo == timezone.utc
    assert m.requested_datetime.hour == 12
    assert m.info is not None
    assert m.info["phase"] == pytest.approx(99.96)
    assert m.url == "https://example.test/moon.jpg"
    assert isinstance(m.image, np.ndarray)
    assert m.image.shape == (730, 730, 3)
    assert m.image.dtype == np.uint8


def test_invalid_hour_raises():
    m = Moon()
    with pytest.raises(ValueError):
        m.set_moon_phase(date="2025-03-14", hour=99)


def test_invalid_date_format_raises():
    m = Moon()
    with pytest.raises(ValueError):
        m.set_moon_phase(date="190-01-01")


def test_pre_2011_date_raises():
    m = Moon()
    with pytest.raises(ValueError, match="2011"):
        m.set_moon_phase(date="2010-12-31", hour=23)


def test_custom_size_is_applied(mock_api, fake_jpeg_bytes):
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

    m = Moon(size=(100, 100))
    m.set_moon_phase(date="2025-03-14", hour=12)

    assert m.image is not None
    assert m.image.shape == (100, 100, 3)


def test_save_writes_jpeg(mock_api, fake_jpeg_bytes, tmp_path, monkeypatch):
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

    monkeypatch.chdir(tmp_path)
    m = Moon(size=(50, 50))
    m.set_moon_phase(date="2025-03-14", hour=12)
    out = m.save()

    assert out == "moon-image-20250314.jpg"
    assert (tmp_path / out).exists()
    assert (tmp_path / out).stat().st_size > 0


def test_save_before_fetch_raises():
    m = Moon()
    with pytest.raises(RuntimeError):
        m.save()


def test_returned_datetime_parsed(mock_api, fake_jpeg_bytes):
    payload = make_api_payload(timestamp="2025-03-14T12:00")
    mock_api.add(
        responses.GET,
        DIALAMOON_API_URL.format(timestamp="2025-03-14T12:00"),
        json=payload,
        status=200,
    )
    mock_api.add(
        responses.GET,
        "https://example.test/moon.jpg",
        body=fake_jpeg_bytes,
        status=200,
        content_type="image/jpeg",
    )

    m = Moon()
    m.set_moon_phase(date="2025-03-14", hour=12)

    assert m.returned_datetime is not None
    assert m.returned_datetime.year == 2025
    assert m.returned_datetime.tzinfo == timezone.utc
