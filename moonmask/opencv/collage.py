import moonmask.mask as mask
import moonmask.opencv.custom_image as custom_image
from moonmask.res.constants import *
import cv2
import numpy as np
from copy import copy
import random

class Collage():
    def __init__(self, key, size):
        self.key = key
        self.size = size
        self.base = custom_image.CustomImage(size)
        self.positive_space = custom_image.CustomImage(size)
        self.negative_space = custom_image.CustomImage(size)

    def set_base_array(self, *args, **kwargs):
        '''takes kwargs like color, url, instagram_url, filename
        and passes it to a CustomImage object to make a numpy array'''
        self.base.set_image(**kwargs)

    def set_positive_space(self, *args, **kwargs):
        '''takes kwargs like color, url, instagram_url, filename
        and passes it to a CustomImage object to make a numpy array'''
        self.positive_space.set_image(**kwargs)

    def set_negative_space(self, *args, **kwargs):
        '''takes kwargs like color, url, instagram_url, filename
        and passes it to a CustomImage object to make a numpy array'''
        self.negative_space.set_image(**kwargs)

    def set_alpha_mask(self, mask):
        self.mask = mask

    def set_mask(self, mask_generator):
        self.mask = copy(mask_generator.mask)

    def create_alpha_mask(self, image):
        ##creating alpha gradient image https://note.nkmk.me/en/python-numpy-generate-gradation-image/
        #RED, GREEN, BLUE = (2, 1, 0)
        #reds = image[:, :, RED]
        #greens = image[:, :, GREEN]
        #blues = image[:, :, BLUE]
        #mask = (greens > 70) | (reds > 70) | (blues > 70)
        mask = self.rgb_to_gray(image)
        #mask = self.get_gradation_3d(self.size[0], self.size[1], (0, 0, 0), (255, 255, 255), (True, True, True))
        self.set_alpha_mask(mask)
        return

    def rgb_to_gray(self, img):
        #https://stackoverflow.com/a/47380815/5650506
        gray_image = np.zeros(img.shape)
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        grayImage = img

        for i in range(3):
           gray_image[:,:,i] = Avg

        return gray_image

    def get_gradation_2d(self, start, stop, width, height, is_horizontal):
        #from https://note.nkmk.me/en/python-numpy-generate-gradation-image/
        if is_horizontal:
            return np.tile(np.linspace(start, stop, width), (height, 1))
        else:
            return np.tile(np.linspace(start, stop, height), (width, 1)).T

    def get_gradation_3d(self, width, height, start_list, stop_list, is_horizontal_list):
        #from https://note.nkmk.me/en/python-numpy-generate-gradation-image/
        result = np.zeros((height, width, len(start_list)), dtype=np.float)

        for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
            result[:, :, i] = self.get_gradation_2d(start, stop, width, height, is_horizontal)

        return result

    def create(self):
        #helpful post: https://stackoverflow.com/questions/46267443/merge-images-using-opencv-and-a-mask
        #making masks: https://codereview.stackexchange.com/questions/184044/processing-an-image-to-extract-green-screen-mask
        #creating alpha gradient image https://note.nkmk.me/en/python-numpy-generate-gradation-image/

        if len(self.mask.shape) != 2:
            mask = self.mask / 255
            self.composite = (self.negative_space.image * mask + self.positive_space.image * (1 - mask)).astype(np.uint8)
        #CREATES A composite image FROM boolean mask
        else:
            self.composite = copy(self.base.image)
            self.composite[~self.mask] = self.negative_space.image[~self.mask]
            self.composite[self.mask] = self.positive_space.image[self.mask]#.astype(float))

    def pixelate_mask(self, radius = 15, step = 34, jitter = 0):
        height, width, channel = self.mask.shape

        points = copy(self.mask)

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
                gray = self.mask[x,y]
                cv2.circle(points,
                        (y, x),
                        radius,
                        int(gray),
                        -1,
                        cv2.LINE_AA)
        self.mask = points
        return
