import urllib.request
import io
import cv2
import numpy as np

class CustomImage():
    def __init__(self, img_size):
        self.size = img_size
        return

    def get_image(self):
        return self.image

    def set_image(self, url="", instagram_url="", filename="", color=""):
        #if more than one of these parameters are provided, raise an error.

        if url: self.load_from_url(url)
        if instagram_url: self.load_from_instagram(instagram_url)
        if filename: self.load_from_filesystem(filename)
        if color: self.make_custom_image(color)
        return

    def make_custom_image(self, color):
        self.image = np.zeros((self.size[0],self.size[1],3), np.uint8)
        self.image[:,0:self.size[0]] = color
        return

    def load_from_instagram(self, instagram_url):
        #TODO check if link has extra info at the end
        #https://nono.ma/says/get-an-instagram-image-url
        try:
            self.load_from_url(instagram_url + "media/?size=l")
        except:
            raise Exception("I can't seem to download that image from that link: " + instagram_url + ". Check that it's an instagram link in the form 'https://instagram.com/p/SOME_NUMBERS_AND_LETTERS/'.")
        return

    def load_from_filesystem(self, path):
        self.image = cv2.imread(path)
        self.resize(self.size)
        return

    def load_from_url(self, url):
        # METHOD #1: OpenCV, NumPy, and urllib
	    # download the image, convert it to a NumPy array, and then read
	    # it into OpenCV format
        # https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/
        resp = urllib.request.urlopen(url)
        self.image = np.asarray(bytearray(resp.read()), dtype="uint8")
        self.image = cv2.imdecode(self.image, cv2.IMREAD_COLOR)
        self.resize_image()
        return

    def resize_image(self):
        #https://medium.com/@manivannan_data/resize-image-using-opencv-python-d2cdbbc480f0
        #Preferable interpolation methods are cv.INTER_AREA for shrinking and cv.INTER_CUBIC(slow) & cv.INTER_LINEAR for zooming. By default, interpolation method used is cv.INTER_LINEAR for all resizing purposes.
        self.image = cv2.resize(self.image, self.size, interpolation=cv2.INTER_AREA)
        #self.image = cv2.resize(self.image, self.size, interpolation=cv2.INTER_CUBIC)
