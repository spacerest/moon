import pytest
import cv2
import numpy as np
from .. import mask
from .. import collage
import os

SIZE = (1000,1000)
DATE = "2019-07-17"
FRAME_ID = '4729'
URL = "https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/frames/730x730_1x1_30p/moon.4729.jpg"
COLORS = [(0,0,0), (255,0,0), (255,255,255)]
IMAGE = np.zeros((SIZE[0],SIZE[1],3), np.uint8)
IMAGE[:,0:int(SIZE[0]/3)] = COLORS[0]
IMAGE[:,int(SIZE[0]/3):int(2 * SIZE[0]/3)] = COLORS[1]
IMAGE[:,int(2 * SIZE[0]/3):SIZE[0]] = COLORS[2]

def pytest_namespace():
    return {'mask': None}

class TestClass(object):
    def test_gets_input_image(self):
        pytest.mask = mask.Mask("test", IMAGE)

    def test_makes_simple_mask(self):
        assert pytest.mask.mask[0][0].tolist() == [0, 0, 0]

    def test_sets_moon_filename_mask(self):
        im = cv2.imread('tests/res/testmoon.jpg')
        pytest.mask = mask.Mask('moon', im).mask
        print(im)
        print(pytest.mask)

