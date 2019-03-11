# moonmask
This is a small library that uses PIL and Ernie Wright's moon visualizations from the Nasa Visualization Studio to create artistic renderings of moonphases. 

intended usage:
first, make sure that pip and python are installed

then:
```python
from moonmask import collage
moonmask = collage.Collage()

moonmask.set_moon_mask(relative_date="today")
    """possible parameters: filename, date 
    possible errors: Moon image not found, relative date isn't in valid format, date
    isn't in valid format"""

moonmask.set_main_image(instagram_link="link")
    """possible parameters: url, filename
    possible errors: Main image not found, _ format not supported"""

moonmask.set_moon_foreground(instagram_link="link")
    """possible parameters: url, filename
    possible errors: Image not found, _ format not supported"""

moonmask.set_main_background(instagram_link="link")
    """possible parameters: url, filename
    possible errors: Image not found, _ format not supported"""

moonmask.make_collage()
    """possible parameters: moon_transparency, background_transparency,
    dimensionality
    possible errors: No moon mask, No main image, No moon foreground image"""
```

Resources:
- https://svs.gsfc.nasa.gov/4442
- https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
