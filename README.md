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

This is a Python package that gets an image of a given date's moon phase. It uses Ernie Wright's moon visualizations from the Dial-a-Moon project at NASA's Scientific Visualization Studio.

At the time of the last release, this package can access any of the moon visualizations from 2011 onward.

## Installation

To install this package, just run:

```bash
pip install moon
```

## Usage

This package retrieves a **NumPy.ndarray** representing the lunar phase, along with JSON data containing lunar statistics from NASA's Dial-a-Moon project. The image array can be manipulated with **OpenCV** and/or saved to disk as a `.jpg` file.

### Basic Usage

```python
from moon.dialamoon import Moon

moon = Moon()
moon.set_moon_phase()
```

Access the image array with:

```python
moon.image
```

Save the image to disk as `filename.jpg` with:

```python
moon.save_to_disk('filename')
```

### Jupyter Notebook Usage

```python
from moon.jupyter_ui import JupyterUi

ui = JupyterUi()
ui.set_moon_phase()  # Defaults to today's date
print(ui.info)
ui.show()
```

### Resizing the Image

By default, the returned image is **730x730 pixels**. To specify a different size, use the `size` keyword argument:

```python
moon = Moon(size=(100, 100))
```

## OpenCV & NumPy Integration

The inclusion of OpenCV and NumPy in this package is a remnant of earlier versions that supported additional image processing features. While currently not necessary for core functionality, these libraries allow for further customization, such as:

- **Image manipulation** (e.g., adjusting brightness, contrast, or applying filters)
- **Overlaying text or graphics** on the moon image
- **Efficient in-memory image processing** using NumPy arrays

For example, you can use OpenCV to apply a grayscale filter:

```python
import cv2
import numpy as np

image = moon.image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_moon.jpg", gray_image)
```

Since these dependencies are no longer required for core functionality, they may be removed in a future version.

## Additional rmation

You can access [more details and related lunar imagery](https://svs.gsfc.nasa.gov/help/#apis-dialamoon) via `Moon.info`.


# Updates

Please feel free to post bugs, suggestions and feature requests on this repo. 

## 2.0.0 2024-02-01
- use the new API to determine moon image urls, so yearly IDs don't need to be added anymore
- deprecate image viewing via terminal
## 1.1.5 2021-12-30
- put constants in a `.json` file instead of a `.py` file
- add SVS ID for 2022
- if a SVS ID for a year isn't available, check whether it's available on in `res/constants.json` on the GitHub repo and then remind the user to update the package for next time
## 1.1.3 2021-05-01
- update numpy and opencv-python versions
- fix lru_cache decorator to fix issue #4
## 1.1.2 2021-01-24
- can include `hour` parameter in `Moon.set_moon_phase()`


# Resources:
- [nasa moon visualization studio](https://svs.gsfc.nasa.gov/4442)
- [how to publish a python package on pypi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)


moon ascii art courtesy of [jsg](http://www.ascii-art.de/ascii/mno/moon.txt)
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
       



