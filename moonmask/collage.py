from PIL import Image
from PIL import ImageOps
from moonmask import mask
from moonmask import custom_image
from moonmask import moon_image as moon
from moonmask.constants import *

class Collage():

    def __init__(self):
        self.main_image = None
        self.main_background = None
        self.moon_foreground = None
        self.moon_mask = None
        self.img_size = (1000,1000)
        return

    def set_moon_mask(self, date=None, relative_date="today", filename=None):
        """Sets the image that will be used as a mask on the image

        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """
        self.moon_mask = moon.MoonImage(size=self.img_size)
        self.moon_mask = self.moon_mask.set_moon_image(date=date, relative_date=relative_date, filename=filename)

    def set_main_image(self, url="", instagram_url="", filename=""):
        img_size = (1000,1000)
        self.main_image = custom_image.CustomImage(img_size).set_image(url, instagram_url, filename)
        return

    def set_main_background(self, url="", instagram_url="", filename=""):
        img_size = (1000,1000)
        self.main_background = custom_image.CustomImage(img_size).set_image(url, instagram_url, filename)
        return

    def set_moon_foreground(self, url="", instagram_url="", filename=""):
        img_size = (1000,1000)
        self.moon_foreground = custom_image.CustomImage(img_size).set_image(url, instagram_url, filename)
        return

    def make_collage(self, filename, selfie_file=None, moon_file=None, foreground_file=None, background_file=None, foreground_transparency=200, background_transparency=50, dimensionality=3, img_size=1000):
        img_size = (img_size, img_size)

        if self.main_image:
            selfie = self.main_image#custom_image.CustomImage(img_size).load_from_instagram(test_url)
            moon_shaped_selfie = self.main_image#custom_image.CustomImage(img_size).load_from_filesystem(selfie_file)
        else:
            selfie = Image.new('RGB', img_size, 'black')
            moon_shaped_selfie = Image.new('RGB', img_size, 'black')

        #give the selfie image the requested white borders
        white_background = Image.new('RGB', img_size, "white")

        selfie = ImageOps.fit(selfie, img_size, Image.ANTIALIAS)
        moon_shaped_selfie = ImageOps.fit(moon_shaped_selfie, img_size, Image.ANTIALIAS)

        if self.main_background:
            background = self.main_background#Image.open(background_file, 'r')
            background = ImageOps.fit(background, img_size, Image.ANTIALIAS)
        else:
            background= Image.new('RGB',img_size,'black')

        if self.moon_foreground:
            moon_shaped_foreground = self.moon_foreground#Image.open(foreground_file)
            moon_shaped_foreground = ImageOps.fit(moon_shaped_foreground, img_size, Image.ANTIALIAS)
        else:
            moon_shaped_foreground = Image.new('RGB', img_size, 'white')

        background_mask = mask.Mask(background, 255, img_size, background_transparency).get_mask()

        #put transparent background over selfie
        selfie.paste(background, (0,0), mask=background_mask)

        transparency_divisor = dimensionality + 1

        #loop through a range, so that different brightnesses of the moon
        #are represented with different transparencies of the foreground
        for i in range(1, dimensionality + 1):
            transparency_divisor -= 1

            moon_mask = mask.Mask(self.moon_mask, 40 * i, img_size).get_mask()
            moon_mask_transparent = mask.Mask(self.moon_mask, 40 * i, img_size).get_mask()
            moon_mask_transparent = moon_mask_transparent.point(lambda j: min(j * 25, foreground_transparency / transparency_divisor))

            moon_shaped_foreground.putalpha(moon_mask_transparent)

            #reput moon shaped selfie on top of transparent background
            moon_shaped_selfie.putalpha(moon_mask)
            selfie.paste(moon_shaped_selfie, (0,0), mask=moon_shaped_selfie)

            #put foreground over moon
            selfie.paste(moon_shaped_foreground, (0,0), mask=moon_mask_transparent)

        selfie.save(filename + ".png", format='PNG')
