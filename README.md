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

This is a Python package that gets an image of a given date's moon phase. It uses NumPy, OpenCV, and Ernie Wright's moon visualizations from the Dial-a-Moon project at Nasa's Scientific Visualization Studio.

At time of last release, this package can access any of the moon visualizations from 2011-2024. In November of each calendar year, the data for the next year's moon becomes available on SVS and copied over to this repositorhy as soon as possible, so for best performance, the new version of this package should be installed at the end of each year.

# Installation 

To install this package, just run 

```pip install moon```

# Usage

Currently, this package can get a NumPy.ndarray representing the lunar phase, as well as some json of the lunar stats from the Dial-a-Moon Nasa site. This array is usable as an image using openCV, or can be saved to disk as a .jpg file.

You can test it out using terminal:

```
from moon.terminal_ui import TerminalUi

ui = TerminalUi()
ui.set_moon_phase() #defaults to today's date
print(ui.moon_datetime_info)
ui.show()

```

You can alternately test it out using Jupyter notebooks:

```
from moon.jupyter_ui import JupyterUi

ui = JupyterUi()
ui.set_moon_phase() #defaults to today's date
print(ui.moon_datetime_info)
ui.show()

```

To just use it in a project, you can use it like this:

```
from moon.dialamoon import Moon

moon = Moon()
moon.set_moon_phase()

```
and access the image array itself with

```
moon.image
```

You can save the current image to disk with the method `moon.save_to_disk('filename')` or `ui.save_to_disk('filename')`, which would save a `filename.jpg` in your current directory.


# Updates

Please feel free to post bugs, suggestions and feature requests on this repo. This will be my first time creating and maintaining a python package, and I am receptive to any recommendations or PRs.

## 1.1.2 2021-01-24
- can include `hour` parameter in `Moon.set_moon_phase()`
## 1.1.3 2021-05-01
- update numpy and opencv-python versions
- fix lru_cache decorator to fix issue #4
## 1.1.5 2021-12-30
- put constants in a `.json` file instead of a `.py` file
- add SVS ID for 2022
- if a SVS ID for a year isn't available, check whether it's available on in `res/constants.json` on the GitHub repo and then remind the user to update the package for next time

## todo
- check whether there are edge cases where json mooninfo or date attributes might not match the currently requested moon phase
- make a clearer method for loading previously downloaded images/json as the current moon phase and data

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
       



