from PIL import Image
from PIL import ImageOps
import moonmask.mask as mask
import moonmask.custom_image as custom_image
import moonmask.moon_image as moon
from moonmask.res.constants import *
from moonmask.word_mask import WordMask

#for pixellating image, test
import cv2
import numpy as np
from copy import copy
import random

class Collage():

    def __init__(self):
        self.main_image = None
        self.moon_mask_negative_space = None
        self.moon_mask_positive_space = None
        self.moon_mask = None
        self.img_size = (1000,1000)
        self.image_queue = {}
        self.created_collage = None
        self.words_main_image = None
        self.words_positive_space = None
        self.words_negative_space = None
        self.positive_space_pixelated = False
        self.negative_space_pixelated = False
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

    def add_to_image_queue(self, image_key, image=None, url="", instagram_url="", filename="", color=""):
        if image:
            self.image_queue[image_key] = image
        else:
            self.image_queue[image_key] = custom_image.CustomImage(self.img_size).set_image(url, instagram_url, filename, color)
        return

    def list_image_queue(self):
        for image_key in self.image_queue:
            print(image_key)
        return

    def get_moon_phase_date(self):
        return self.moon_image.get_moon_phase_date()

    def set_main_image(self, image_key, url="", instagram_url="", filename="", color=""):
        self.main_image = self.create_image(image_key, url, instagram_url, filename, color)
        return

    def set_mask_negative_space(self, image_key, url="", instagram_url="", filename="", color=""):
        self.moon_mask_negative_space = self.create_image(image_key, url, instagram_url, filename, color)
        return

    def set_main_image_words(self, words="test", invert=False):
        self.words_main_image = WordMask(self.img_size, invert)
        self.words_main_image.set_word_mask(words)
        self.words_main_image = self.words_main_image.get_word_mask()
        return

    def set_positive_space_words(self, words="test", invert=False):
        self.words_positive_space = WordMask(self.img_size, invert)
        self.words_positive_space.set_word_mask(words)
        self.words_positive_space = self.words_positive_space.get_word_mask()
        return

    def set_negative_space_words(self, words="test", invert=False):
        self.words_negative_space = WordMask(self.img_size, invert)
        self.words_negative_space.set_word_mask(words)
        self.words_negative_space = self.words_negative_space.get_word_mask()
        return

    def set_mask_positive_space(self, image_key, url="", instagram_url="", filename="", color=""):
        self.moon_mask_positive_space = self.create_image(image_key, url, instagram_url, filename, color)
        return

    def create_image(self, image_key, url="", instagram_url="", filename="", color=""):
        if not image_key in self.image_queue:
            if not url and not instagram_url and not filename and not color:
                raise Exception("There is no image in queue that has the key " + image_key)
            else:
                created_image = custom_image.CustomImage(self.img_size).set_image(url, instagram_url, filename, color)
                self.image_queue[image_key] = created_image
        else:
            created_image = self.image_queue[image_key]
        return created_image

    def create_collage(self, main_image_file=None, mask_file=None, positive_space_file=None, negative_space_file=None, positive_space_transparency=200, negative_space_transparency=50, dimensionality=3, img_size=1000):
        img_size = (img_size, img_size)

        #1 - START - get the images and make them the right size
        if self.main_image:
            main_image = self.main_image
            mask_shaped_main_image = self.main_image
        else:
            main_image = Image.new('RGB', img_size, 'black')
            mask_shaped_main_image = Image.new('RGB', img_size, 'black')

        white_img = Image.new('RGB', img_size, 'white')

        main_image = ImageOps.fit(main_image, img_size, Image.ANTIALIAS)
        mask_shaped_main_image = ImageOps.fit(mask_shaped_main_image, img_size, Image.ANTIALIAS)

        if self.words_main_image:
            main_image.paste(white_img, (0,0), mask=self.words_main_image)
            mask_shaped_main_image.paste(white_img, (0,0), mask=self.words_main_image)

        if self.moon_mask_negative_space:
            if self.negative_space_pixelated:
                negative_space = self.pixelate_image(self.moon_mask_negative_space)
            else:
                negative_space = self.moon_mask_negative_space
            negative_space = ImageOps.fit(negative_space, img_size, Image.ANTIALIAS)
        else:
            negative_space= Image.new('RGB',img_size,'black')

        if self.moon_mask_positive_space:
            if self.positive_space_pixelated:
                mask_shaped_positive_space = self.pixelate_image(self.moon_mask_positive_space)
            else:
                mask_shaped_positive_space = self.moon_mask_positive_space#Image.open(positive_space_file)
            mask_shaped_positive_space = ImageOps.fit(mask_shaped_positive_space, img_size, Image.ANTIALIAS)
        else:
            mask_shaped_positive_space = Image.new('RGB', img_size, 'white')

        if self.words_main_image:
            mask_shaped_positive_space.paste(white_img, (0,0), mask=self.words_main_image)
        #1 - END

        negative_space_mask = mask.Mask(negative_space, 255, img_size, negative_space_transparency).get_mask()
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
        self.created_collage = main_image

    def desktop_show_collage(self):
        self.created_collage.show()

    def create(self, main_image_file=None, mask_file=None, positive_space_file=None, negative_space_file=None, positive_space_transparency=200, negative_space_transparency=50, dimensionality=3, img_size=1000):
        self.create_collage(main_image_file, mask_file, positive_space_file, negative_space_file, positive_space_transparency, negative_space_transparency, dimensionality, img_size)
        self.desktop_show_collage()

    def save_collage(self, filename):
        self.created_collage.save(filename + '.jpg', format='JPEG')

#TEST - try adding some pixellation to the moon mask

    def pixelate_positive_space(self, radius=2, step=1, jitter=0):
        self.positive_space_pixelated = True

    def pixelate_negative_space(self, radius=2, step=1, jitter=0):
        self.negative_space_pixelated = True

    def get_created_collage(self):
        return self.created_collage

    def pixelate_image(self, image, radius = 15, step = 34, jitter = 0):
        image = image.convert('L')
        image = np.array(image)
        print(image.shape)
        height, width = image.shape

        points = copy(image)

        for i in range(height):
            for j in range(width):
                points[i, j] = 255
        xrange = np.zeros(int(height/step))
        yrange = np.zeros(int(width/step))
        for xvalue in range(len(xrange)):
            xrange[xvalue] = xvalue
        for yvalue in range(len(yrange)):
            yrange[yvalue] = yvalue
        xrange = [value*step+step/2 for value in xrange]
        yrange= [value*step+step/2 for value in yrange]
        np.random.shuffle(xrange)
        for i in xrange:
            np.random.shuffle(yrange)
            for j in yrange:
                x = int(i)# + random.randint(1, 2*JITTER-JITTER))
                y = int(j)# + random.randint(1, 2*JITTER-JITTER))
                if(x >= height):
                        x = height-1
                if( y >= width):
                        y = width-1
                gray = image[x,y]
                cv2.circle(points,
                        (y, x),
                        radius,
                        int(gray),
                        -1,
                        cv2.LINE_AA)
        return Image.fromarray(points)
