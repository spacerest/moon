# moonmask

This is a small library that uses PIL and Ernie Wright's moon visualizations from the Nasa Visualization Studio to create artistic renderings of moonphases. 

        _..._           _..._            _..._            _..._            _..._
      .:::::::.       .::::. `.        .::::  `.        .::'   `.        .'     `.
     :::::::::::     :::::::.  :      ::::::    :      :::       :      :         :  
     :::::::::::     ::::::::  :      ::::::    :      :::       :      :         :
     `:::::::::'     `::::::' .'      `:::::   .'      `::.     .'      `.       .'
       `':::''         `'::'-'         `'::.-'           `':..-'          `-...-'

        _..._             _..._
      .'     `.         .'   `::.
     :         :       :       ::: 
     :         :       :       :::
     `.       .'       `.     .::'
       `-...-'           `-..:''
       
              ascii art courtesy of [jsg](http://www.ascii-art.de/ascii/mno/moon.txt)

        _..._
      .'   `::.
     :       ::: 
     :       :::
     `.     .::'
       `-..:''
        _..._
      .'  ::::.
     :    ::::::    LAST QUARTER
     :    ::::::
     `.   :::::'
       `-.::''
        _..._
      .' .::::.
     :  ::::::::    WANING CRESCENT
     :  ::::::::
     `. '::::::'
 jgs   `-.::''
        _..._
      .:::::::.
     :::::::::::    NEW MOON
     :::::::::::
     `:::::::::'
       `':::''

## intended usage (mac/linux instructions):

First, [make sure that pip and python3 are installed](https://realpython.com/installing-python/). A [virtual environment](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b) would be a good idea, though would be optional.

Next, install this package:

```bash
pip install moonmask
```

Now to use this package and make an image, open up a python interactive shell:

```bash
python
```

You can now run these commands to simply generate a black and white version of the current moon phase:

```python
>>> from moonmask import collage
>>> moonmask = collage.Collage()
>>> moonmask.set_moon_mask()
>>> moonmask.make_collage("current_moon_phase") #current_moon_phase will be the name of the file in this example
>>> exit()
```

```bash
open current_moon_phase.png
```

You can add a few commands to make it a collage made up of different images: 

```python

>>> from moonmask import collage
>>> moonmask = collage.Collage()
>>> moonmask.set_moon_mask()
>>> moonmask.set_main_image(instagram_link="https://instagram.com/p/SOME_LETTERS_NUMBERS_SYMBOLS_1/")
>>> moonmask.set_moon_foreground(instagram_link="https://instagram.com/p/SOME_LETTERS_NUMBERS_SYMBOLS_2/")
>>> moonmask.set_main_background(instagram_link="https://instagram.com/p/SOME_LETTERS_NUMBERS_SYMBOLS_3/")
>>> moonmask.make_collage("moon_collage")
>>> exit()
```

```bash
open moon_collage.png
```

There are other parameters that these functions take. For example, wherever you can use "instagram_url" as a parameter to load an image, you can instead use "url" and "filename" parameters.

# Updates

There will be updates to this package soon. 


Resources:
- https://svs.gsfc.nasa.gov/4442
- https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56
