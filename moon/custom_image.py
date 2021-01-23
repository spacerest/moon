import urllib.request
import io
import cv2
import numpy as np
from copy import deepcopy, copy
from functools import lru_cache

class CustomImage():
    def __init__(self, img_size, **kwargs):
        self.size = img_size
        self.height = img_size[0]
        self.width = img_size[1]
        self.set_image(**kwargs)
        return

    def save_to_disk(self, filename):
        try:
            cv2.imwrite(filename + ".jpg", self.image)
        except Exception as e:
            print(e)

    def get_image(self):
        return self.image
    
    @lru_cache(maxsize=10)#$todo maybe revisit this maxsize
    def set_image(self, url=None, filename=None):
        # METHOD #1: OpenCV, NumPy, and urllib
	    # download the image, convert it to a NumPy array, and then read
	    # it into OpenCV format
        # https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/
        if url:
            resp = urllib.request.urlopen(url)
            self.image_src = url
            self.image = np.asarray(bytearray(resp.read()), dtype="uint8")
            self.image = cv2.imdecode(self.image, cv2.IMREAD_COLOR)
            self.resize_image()
        elif filename:
            self.image_src = filename
            self.image = cv2.imread(filename)
            self.resize_image()
        #$todo not sure easy way to cache image
        #without returning the ndarray to child obj...?
        return self.image

    def resize_image(self):
        #https://medium.com/@manivannan_data/resize-image-using-opencv-python-d2cdbbc480f0
        #Preferable interpolation methods are cv.INTER_AREA for shrinking and cv.INTER_CUBIC(slow) & cv.INTER_LINEAR for zooming. By default, interpolation method used is cv.INTER_LINEAR for all resizing purposes.
        try:
            self.image = cv2.resize(self.image, self.size, interpolation=cv2.INTER_AREA)
        except Exception as e:
            raise e
        self.image = cv2.resize(self.image, self.size, interpolation=cv2.INTER_CUBIC)
