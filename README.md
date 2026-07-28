```
        _..._           _..._            _..._            _..._            _..._
      .:::::::.       .::::. `.        .::::  `.        .::'   `.        .'     `.
     :::::::::::     :::::::.  :      ::::::    :      :::       :      :         :
     :::::::::::     ::::::::  :      ::::::    :      :::       :      :         :
     `:::::::::'     `::::::' .'      `:::::   .'      `::.     .'      `.       .'
       `':::''         `'::'-'         `'::.-'           `':..-'          `-...-'

        _..._           _..._           _..._            _..._            _..._
      .'     `.       .'   `::.       .'  ::::.        .' .::::.        .:::::::.
     :         :     :       :::     :    ::::::      :  ::::::::      :::::::::::
     :         :     :       :::     :    ::::::      :  ::::::::      :::::::::::
     `.       .'     `.     .::'     `.   :::::'      `. '::::::'      `:::::::::'
       `-...-'         `-..:''         `-.::''          `-.::''          `':::''
```

# moon

A Python package that fetches moon-phase images from NASA's [Dial-a-Moon API](https://svs.gsfc.nasa.gov/help/#apis-dialamoon), based on Ernie Wright's visualizations at NASA's Scientific Visualization Studio.

Any UTC date and hour supported by the Dial-a-Moon API works (currently 2011 onward).

## Installation

```bash
pip install moon
```

Optional Jupyter support:

```bash
pip install "moon[jupyter]"
```

## Usage

```python
from moon import Moon

m = Moon()
m.set_moon_phase()                    # defaults to now (UTC)
# m.set_moon_phase(date="2025-03-14", hour=12)

m.image           # numpy.ndarray, RGB uint8, shape (730, 730, 3)
m.info            # full API response: phase, distance, illumination, etc.
m.url             # source image URL
m.save()          # writes moon-image-YYYYMMDD.jpg to CWD
```

Resize by passing `size` to the constructor:

```python
m = Moon(size=(100, 100))
```

In a Jupyter notebook:

```python
from moon.jupyter_ui import JupyterUi

ui = JupyterUi()
ui.set_moon_phase()
ui.show()
```

In a terminal (Unicode half-blocks with truecolor, ASCII fallback):

```python
from moon.terminal_ui import TerminalUi

ui = TerminalUi()
ui.set_moon_phase()
ui.show()                     # auto-detects truecolor support
ui.show(mode="ascii")         # force ASCII
ui.show(mode="blocks", width=60)
```

`m.info` includes fields like `phase`, `age`, `distance`, `diameter`, `subsolar_lon`, `subsolar_lat`, plus a `image_highres` URL if you want a larger version. See the [Dial-a-Moon API docs](https://svs.gsfc.nasa.gov/help/#apis-dialamoon).

## Development

```bash
pip install -e ".[dev]"
pytest                    # unit tests only
pytest -m integration     # hit the real NASA API
```

## Changelog

### 3.0.0 (2026)
- Modernized packaging: `pyproject.toml` (PEP 621), Python 3.10+
- Replaced OpenCV with Pillow (~50 MB → ~3 MB dependency)
- Replaced `urllib` with `requests`
- Type hints and `py.typed` marker
- `Moon` no longer requires a subclass for basic use
- Reimplemented `TerminalUi` with Unicode half-block truecolor rendering + ASCII fallback (was a deprecation stub in 2.0.0)
- Removed stale SVS-ID year lookup
- pytest test suite with mocked HTTP; opt-in integration tests
- GitHub Actions CI across Python 3.10–3.13
- **Breaking:** `moon.image` is now RGB (was BGR when using OpenCV). If you were passing `moon.image` back into OpenCV, swap channels with `cv2.cvtColor(m.image, cv2.COLOR_RGB2BGR)`.
- **Breaking:** `moon.custom_image.CustomImage` and `moon.res.constants` are removed.

### 2.0.0 (2024-02-01)
- Use the Dial-a-Moon API to determine image URLs (no more yearly SVS ID updates)
- Deprecate terminal image viewing

### 1.1.5 (2021-12-30)
- Move constants to `.json`, add 2022 SVS ID, fallback to GitHub constants when a year is missing

### 1.1.3 (2021-05-01)
- Update numpy and opencv-python versions, fix `lru_cache` bug (#4)

### 1.1.2 (2021-01-24)
- `Moon.set_moon_phase()` accepts an `hour` parameter

## Resources

- [NASA Scientific Visualization Studio: Dial-a-Moon](https://svs.gsfc.nasa.gov/4442)
- [Dial-a-Moon API](https://svs.gsfc.nasa.gov/help/#apis-dialamoon)

Moon ASCII art courtesy of [jsg](http://www.ascii-art.de/ascii/mno/moon.txt).
