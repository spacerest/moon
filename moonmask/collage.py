from PIL import Image
from PIL import ImageOps
import moonmask.mask as mask
import moonmask.custom_image as custom_image
import moonmask.moon_image as moon
from moonmask.res.constants import *

class Collage():

    def __init__(self):
        self.main_image = None
        self.moon_mask_negative_space = None
        self.moon_mask_positive_space = None
        self.moon_mask = None
        self.img_size = (1000,1000)
        return

    def set_mask(self, date=None, relative_date="today", filename=None):
        """Sets the image that will be used as a mask on the image

        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """
        self.moon_image = moon.MoonImage(size=self.img_size)
        self.moon_mask = self.moon_image.set_moon_image(date=date, relative_date=relative_date, filename=filename)
        return

    def get_moon_phase_date(self):
        return self.moon_image.get_moon_phase_date()

    def set_main_image(self, url="", instagram_url="", filename="", color=""):
        img_size = (1000,1000)
        self.main_image = custom_image.CustomImage(img_size).set_image(url, instagram_url, filename, color)
        return

    def set_mask_negative_space(self, url="", instagram_url="", filename="", color=""):
        img_size = (1000,1000)
        self.moon_mask_negative_space = custom_image.CustomImage(img_size).set_image(url, instagram_url, filename, color)
        return

    def set_mask_positive_space(self, url="", instagram_url="", filename="", color=""):
        img_size = (1000,1000)
        self.moon_mask_positive_space = custom_image.CustomImage(img_size).set_image(url, instagram_url, filename, color)
        return

    def make_collage(self, filename, main_image_file=None, mask_file=None, positive_space_file=None, negative_space_file=None, positive_space_transparency=200, negative_space_transparency=50, dimensionality=3, img_size=1000):
        img_size = (img_size, img_size)

        if self.main_image:
            main_image = self.main_image#custom_image.CustomImage(img_size).load_from_instagram(test_url)
            mask_shaped_main_image = self.main_image#custom_image.CustomImage(img_size).load_from_filesystem(main_image_file)
        else:
            main_image = Image.new('RGB', img_size, 'black')
            mask_shaped_main_image = Image.new('RGB', img_size, 'black')

        #give the main_image image the requested white borders
        white_negative_space = Image.new('RGB', img_size, "white")

        main_image = ImageOps.fit(main_image, img_size, Image.ANTIALIAS)
        mask_shaped_main_image = ImageOps.fit(mask_shaped_main_image, img_size, Image.ANTIALIAS)

        if self.moon_mask_negative_space:
            negative_space = self.moon_mask_negative_space#Image.open(negative_space_file, 'r')
            negative_space = ImageOps.fit(negative_space, img_size, Image.ANTIALIAS)
        else:
            negative_space= Image.new('RGB',img_size,'black')

        if self.moon_mask_positive_space:
            mask_shaped_positive_space = self.moon_mask_positive_space#Image.open(positive_space_file)
            mask_shaped_positive_space = ImageOps.fit(mask_shaped_positive_space, img_size, Image.ANTIALIAS)
        else:
            mask_shaped_positive_space = Image.new('RGB', img_size, 'white')

        negative_space_mask = mask.Mask(negative_space, 255, img_size, negative_space_transparency).get_mask()

        #put transparent negative_space over main_image
        main_image.paste(negative_space, (0,0), mask=negative_space_mask)

        transparency_divisor = dimensionality + 1

        #loop through a range, so that different brightnesses of the mask
        #are represented with different transparencies of the positive_space
        for i in range(1, dimensionality + 1):
            transparency_divisor -= 1

            current_transparency = (positive_space_transparency / transparency_divisor) + ((255 - positive_space_transparency / transparency_divisor) / transparency_divisor)
            #255 / 1 + (255 - 255) / 1 = 255
            #255 / 2 + (255 - 123) / 2 = 123
            #255 / 3 + (255 - 61 / 3) = 61

            current_mask = mask.Mask(self.moon_mask, 40 * i, img_size).get_mask()
            mask_transparent = mask.Mask(self.moon_mask, 40 * i, img_size).get_mask()
            mask_transparent = mask_transparent.point(lambda j: min(j * 25, current_transparency))

            mask_shaped_positive_space.putalpha(mask_transparent)

            #reput mask shaped main_image on top of transparent negative_space
            mask_shaped_main_image.putalpha(current_mask)
            main_image.paste(mask_shaped_main_image, (0,0), mask=mask_shaped_main_image)

            #put positive_space over mask
            main_image.paste(mask_shaped_positive_space, (0,0), mask=mask_transparent)

        main_image.save(filename + ".jpg", format='JPEG')
        main_image.show()
