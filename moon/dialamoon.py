from __future__ import annotations

from datetime import datetime, timezone
from io import BytesIO
from typing import Any

import numpy as np
import requests
from PIL import Image

DIALAMOON_API_URL = "https://svs.gsfc.nasa.gov/api/dialamoon/{timestamp}"
DIALAMOON_MIN_YEAR = 2011
DEFAULT_SIZE = (730, 730)
REQUEST_TIMEOUT = 30


class Moon:
    """A moon phase image fetched from NASA's Dial-a-Moon API.

    Attributes are populated by :meth:`set_moon_phase`:
      - ``image``: the phase image as a NumPy ``ndarray`` (H, W, 3), RGB uint8
      - ``info``: the full API response (phase, distance, illumination, etc.)
      - ``url``: the source image URL
      - ``requested_datetime`` / ``returned_datetime``: UTC datetimes
    """

    def __init__(self, size: tuple[int, int] = DEFAULT_SIZE) -> None:
        self.size = size
        self.image: np.ndarray | None = None
        self.info: dict[str, Any] | None = None
        self.url: str | None = None
        self.requested_datetime: datetime | None = None
        self.returned_datetime: datetime | None = None

    def __repr__(self) -> str:
        if self.requested_datetime is None:
            return "Moon(unset)"
        return f"Moon({self.requested_datetime.isoformat()})"

    def set_moon_phase(
        self,
        date: str | None = None,
        hour: int | None = None,
    ) -> None:
        """Fetch the moon phase image and info for a UTC date/hour.

        Args:
            date: UTC date as ``YYYY-MM-DD``. Defaults to today (UTC).
            hour: UTC hour 0-23. Defaults to the current hour (UTC).
        """
        self.requested_datetime = _parse_datetime(date, hour)
        self.info = _fetch_info(self.requested_datetime)
        self.returned_datetime = datetime.strptime(
            self.info["time"], "%Y-%m-%dT%H:%M"
        ).replace(tzinfo=timezone.utc)
        self.url = self.info["image"]["url"]
        self.image = _fetch_image(self.url, self.size)

    def save(self, prefix: str = "moon-image-") -> str:
        """Save the current image to disk as ``{prefix}{YYYYMMDD}.jpg``.

        Returns the written filename.
        """
        if self.image is None or self.requested_datetime is None:
            raise RuntimeError("Call set_moon_phase() before save().")
        date_str = self.requested_datetime.strftime("%Y%m%d")
        filename = f"{prefix}{date_str}.jpg"
        return self.save_to_disk(filename.removesuffix(".jpg"))

    def save_to_disk(self, filename: str) -> str:
        """Save the current image as ``{filename}.jpg``. Returns the filename."""
        if self.image is None:
            raise RuntimeError("No image to save; call set_moon_phase() first.")
        out = f"{filename}.jpg"
        Image.fromarray(self.image).save(out, format="JPEG")
        return out

    def get_image(self) -> np.ndarray | None:
        return self.image

    def get_moon_phase_date(self) -> datetime | None:
        return self.requested_datetime


def _parse_datetime(date: str | None, hour: int | None) -> datetime:
    now = datetime.now(timezone.utc)
    if date is None:
        base = now
    else:
        base = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if hour is None:
        hour = now.hour
    if not 0 <= hour <= 23:
        raise ValueError("hour must be between 0 and 23")
    if base.year < DIALAMOON_MIN_YEAR:
        raise ValueError(
            f"Dial-a-Moon only supports {DIALAMOON_MIN_YEAR} onward; "
            f"got year {base.year}. The API silently returns the first 2011 "
            "frame for earlier dates."
        )
    return base.replace(hour=hour, minute=0, second=0, microsecond=0)


def _fetch_info(dt: datetime) -> dict[str, Any]:
    timestamp = dt.strftime("%Y-%m-%dT%H:%M")
    resp = requests.get(
        DIALAMOON_API_URL.format(timestamp=timestamp),
        timeout=REQUEST_TIMEOUT,
    )
    resp.raise_for_status()
    return resp.json()


def _fetch_image(url: str, size: tuple[int, int]) -> np.ndarray:
    resp = requests.get(url, timeout=REQUEST_TIMEOUT)
    resp.raise_for_status()
    img = Image.open(BytesIO(resp.content)).convert("RGB")
    if img.size != size:
        img = img.resize(size, Image.Resampling.LANCZOS)
    return np.asarray(img)
