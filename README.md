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

At time of publishing, this package can access any of the moon visualizations from 2011-2021. The way it's set up now, it'll need an update before the end of 2021.

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
       



