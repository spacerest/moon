import pytest
import cv2
from copy import copy
from moonmask.opencv import collage
from .res.constants import *
import numpy as np
def pytest_namespace():
    return {'collage': None}

class TestClass(object):
    def test_makes_collage_with_black_background(self):
        c = collage.Collage("test", SIZE)
        assert c.base.image[0][0].tolist() == [0, 0, 0]

    def test_makes_collage_with_red_background(self):
        c = collage.Collage("test", SIZE)
        c.set_base_array(color=(0,0,255))
        assert c.base.image[0][0][2] == 255

    def test_gets_mask_makes_red_on_black(self):
        c = collage.Collage("test", (3,3))
        c.set_base_array()
        c.set_positive_space(color=(0,0,255))

        mask = np.zeros((3,3,3), 'uint8')
        mask[1][1] = [255, 255, 255]
        RED, GREEN, BLUE = (2, 1, 0)
        reds = mask[:, :, RED]
        greens = mask[:, :, GREEN]
        blues = mask[:, :, BLUE]
        mask = (greens > 35) | (reds > greens) | (blues > greens)

        c.set_alpha_mask(mask)
        c.create()
        assert c.composite[1][1].tolist() == [0, 0, 255] and c.composite[0][0].tolist() == [0, 0, 0]

    def test_gets_mask_makes_red_on_white(self):
        c = collage.Collage("test", (3,3))
        c.set_base_array()
        c.set_positive_space(color=(0,0, 255))
        c.set_negative_space(color=(255,255,255))

        mask = np.zeros((3,3,3), 'uint8')
        mask[1][1] = [255, 255, 255]
        RED, GREEN, BLUE = (2, 1, 0)
        reds = mask[:, :, RED]
        greens = mask[:, :, GREEN]
        blues = mask[:, :, BLUE]
        mask = (greens > 35) | (reds > greens) | (blues > greens)

        c.set_alpha_mask(mask)
        c.create()
        assert c.composite[1][1].tolist() == [0, 0, 255] and c.composite[0][0].tolist() == [255, 255, 255]

    def test_makes_mask_from_image(self):
        c = collage.Collage("test", (3,3))
        c.set_base_array()
        c.set_positive_space(color=(0,0, 255))
        c.set_negative_space(color=(255,255,255))

        self.show_image(DOT_IMAGE)
        mask = self.create_alpha_mask(DOT_IMAGE)
        print(mask)

        c.mask = mask
        c.create()
        self.show_image(c.composite)
        assert c.composite[0][0].tolist() == [0, 0, 255] and c.composite[1][1].tolist() == [255, 255, 255]


    def show_image(self, image):
        cv2.imshow("test", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def create_alpha_mask(self, image):
        ##creating alpha gradient image https://note.nkmk.me/en/python-numpy-generate-gradation-image/
        #RED, GREEN, BLUE = (2, 1, 0)
        #reds = image[:, :, RED]
        #greens = image[:, :, GREEN]
        #blues = image[:, :, BLUE]
        #mask = (greens > 70) | (reds > 70) | (blues > 70)
        mask = self.rgb_to_gray(image)
        #mask = self.get_gradation_3d(self.size[0], self.size[1], (0, 0, 0), (255, 255, 255), (True, True, True))
        return mask


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


