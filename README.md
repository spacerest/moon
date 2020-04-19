# moon 

This is a small python package that simply gets an numpy array of an image of a given date's moon phase. It uses numpy, opencv and Ernie Wright's moon visualizations from the Dial-a-Moon project at Nasa Visualization Studio.

At time of publishing, this package can access any of the moon visualizations from 2011-2020. I suppose the way it's set up now, it'll need an update before the end of 2020, and perhaps I'll find a better way to set it up by then.

# Installation 

To install this package, just run 

```pip install moon```

# Usage

Currently, this package will return a numpy array representing the lunar phase, as well as some json of the lunar stats from the Dial-a-Moon Nasa site. This array is usable as an image using openCV, or can be saved to disk as a .jpg file.

You can test it out using terminal:

```
from moon.terminal_ui import TerminalUi

ui = TerminalUi()
ui.set_moon_phase() #defaults to today's date
ui.show()
```

You can alternately test it out using Jupyter notebooks:

```
from moon.jupyter_ui import JupyterUi

ui = JupyterUi()
ui.set_moon_phase() #defaults to today's date
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

At the moment, there isn't any built in method for converting the numpy array to a Pillow image. I had this set up with Pillow originally, but it fell by the wayside when I moved over to playing around with openCV. 

# Updates

Please feel free to post bugs, suggestions and feature requests on this repo. Through some trial and error, I think I finally have the package as simple as possible, but I'm open to evolution. This will be my first time creating and maintaining a python package, and I am receptive to any tips or PRs as far as best-practices go.

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
       



