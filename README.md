# moonmask

This is a small library that uses PIL and Ernie Wright's moon visualizations from the Nasa Visualization Studio to create artistic renderings of moonphases. 

## intended usage (mac/linux instructions):

First, [make sure that pip and python3 are installed](https://realpython.com/installing-python/). A [virtual environment](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) would be a good idea, though would be optional.

Next, install this package:

```bash
pip install moonmask
```

Then, open up a python interactive shell:

```bash
python
```

You can now run these commands to simply generate a black and white version of the current moon phase:

```python
from moonmask import collage
moonmask = collage.Collage()
moonmask.set_moon_mask()
moonmask.make_collage("current_moon_phase")
exit()
```

```bash
open current_moon_phase.png
```

You can add a few commands to make it a collage made up of different images: 

```
python

moonmask.set_main_image(instagram_link="link")
    """possible parameters: url, filename
    possible errors: Main image not found, _ format not supported"""

moonmask.set_moon_foreground(instagram_link="link")
    """possible parameters: url, filename
    possible errors: Image not found, _ format not supported"""

moonmask.set_main_background(instagram_link="link")
    """possible parameters: url, filename
    possible errors: Image not found, _ format not supported"""

    """possible parameters: moon_transparency, background_transparency,
    dimensionality
    possible errors: No moon mask, No main image, No moon foreground image"""
```

Resources:
- https://svs.gsfc.nasa.gov/4442
- https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
