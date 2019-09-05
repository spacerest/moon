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
       

moon ascii art courtesy of [jsg](http://www.ascii-art.de/ascii/mno/moon.txt)

# dialamoon 

This is a small python package that simply gets an image of a given date's moon phase. It uses numpy, opencv and Ernie Wright's moon visualizations from the Dial-a-Moon project at Nasa Visualization Studio.

At time of publishing, this package can access any of the moon visualizations from 2011-2019.

# Installation 

To install this package, just run 

```pip install dialamoon```

# Usage

Currently, this package will return a numpy array representing the lunar phase, as well as some json of the lunar stats from the Dial-a-Moon Nasa site. This array is usable as an image using openCV, or can be saved to disk as a .jpg file.

You can test it out using terminal:

```
from dialamoon.terminal_ui import TerminalUi

ui = TerminalUi()
ui.set_moon_image() #defaults to today's date
ui.show()
```

You can alternately test it out using Jupyter notebooks:

```
from dialamoon.jupyter_ui import Jupyter

ui = JupyterUi()
ui.set_moon_image() #defaults to today's date
ui.show()
```

To just use it in a project, you can use it like this:

```
from dialamoon.moon import Moon

moon = Moon()
moon.set_moon_phase()

```
and access the image array itself with

```
moon.image
```

At the moment, there isn't any built in method for converting the numpy array to a Pillow image. 

# Updates

Please feel free to post bugs and feature requests on this repo.

# Resources:
- [nasa moon visualization studio](https://svs.gsfc.nasa.gov/4442)
- [how to publish a python package on pypi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)
