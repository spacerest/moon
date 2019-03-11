To use this library, run these commands:

installing pip and python...
pip install MoonMask
python

import MoonMask
moonmask = MoonMask()

moonmask.set_moon_image(relative_date="today")
    possible parameters: filename, date 
    possible errors: Moon image not found, relative date isn't in valid format, date
    isn't in valid format

moonmask.set_main_image(instagram_link="link")
    possible parameters: url, filename
    possible errors: Main image not found, _ format not supported

moonmask.set_moon_foreground(instagram_link="link")
    possible parameters: url, filename
    possible errors: Image not found, _ format not supported

moonmask.set_main_background(instagram_link="link")
    possible parameters: url, filename
    possible errors: Image not found, _ format not supported

moonmask.make_collage()
    possible parameters: moon_transparency, background_transparency,
    dimensionality
    possible errors: No moon mask, No main image, No moon foreground image

Resources:
- https://blog.sicara.com/perfect-python-command-line-interfaces-7d5d4efad6a2


