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

# moonmask

This is a small library that uses numpy, opencv and Ernie Wright's moon visualizations from the Nasa Visualization Studio to create artistic renderings of moonphases. 

## intended usage (mac/linux instructions):

1. First, [make sure that pip and python3 are installed](https://realpython.com/installing-python/). A [virtual environment](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) would be a good idea, though would be optional.

2. Next, install this package. Open terminal or another command line interface on your computer and then install the package by typing:

```bash
pip install moonmask
```

3. Now to use this package and make an image, open up a python interactive shell by typing:

```bash
python
```

4. You can now run these commands to simply see the current moon phase:

```python
>>> from moonmask.terminal_ui import TerminalUi 
>>> ui = TerminalUi()
>>> ui.set_moon("moon_today") #"moon_today" could be any key you'd like
>>> ui.show_image("moon_today"
```

You can add a few commands to use it in a collage made up of different images: 

```python
>>> ui.start_new_collage("collage1")
>>> ui.load_new_image("image1", url="SOME_URL")
>>> ui.load_new_image("image2", filename="SOME_FILENAME")
>>> ui.image_to_mask("moon_today", "moon_today_mask")
>>> ui.selected_collage.set_mask(ui.mask_store["moon_today_mask"])
>>> ui.selected_collage.set_positive_space(ui.image_store["image1"])
>>> ui.selected_collage.set_negative_space(ui.image_store["image2"])
>>> ui.selected_collage.combine()
>>> ui.show_collage("collage1")
```

# Updates

There will be updates to this package soon. It is actively being maintained as of March 12, 2019, so please feel free to post bugs and feature requests on this repo.

Resources:
- [nasa moon visualization studio](https://svs.gsfc.nasa.gov/4442)
- [how to publish a python package on pypi](https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56)
- [pixelation with
    opencv](https://medium.com/@elvisdias/lets-work-with-borders-opencv-implementation-in-python-b37c3d87c73a)
