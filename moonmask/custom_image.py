import urllib.request
import io
import cv2
import numpy as np
from copy import deepcopy, copy

class CustomImage():
    def __init__(self, img_size, key, **kwargs):
        self.size = img_size
        self.key = key
        self.height = img_size[0]
        self.width = img_size[1]
        self.set_image(**kwargs)
        return

    def get_image(self):
        return self.image

    def set_image(self, image_array=None, url=None, instagram_url=None, filename=None, color=(0,0,0)):
        #if more than one of these parameters are provided, raise an error.

        if isinstance(image_array,np.ndarray): self.image = deepcopy(image_array)
        elif url: self.load_from_url(url)
        elif instagram_url: self.load_from_instagram(instagram_url)
        elif filename: self.load_from_filesystem(filename)
        elif color: self.make_custom_image(color)
        else: self.image = None
        return

    def make_custom_image(self, color):
        self.image = np.zeros((self.size[0],self.size[1],3), np.uint8)
        self.image[:,0:self.size[0]] = color
        return

    def add_vertical_stripe(self, beginning, end, color):
        beginning_index = int(beginning * self.width)
        end_index = int(end * self.width)

        #slicing numpy arrays
        self.image[:,beginning_index:end_index] = color
        return


    def add_horizontal_stripe(self, beginning, end, color):
        beginning_index = int(beginning * self.height)
        end_index = int(end * self.height)

        #slicing numpy arrays
        self.image[beginning_index:end_index,:] = color
        return

    def rot90(self, times=1):
        self.image = np.rot90(self.image, times)
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
        self.resize_image()
        return

    def load_from_url(self, url):
        # METHOD #1: OpenCV, NumPy, and urllib
	    # download the image, convert it to a NumPy array, and then read
	    # it into OpenCV format
        # https://www.pyimagesearch.com/2015/03/02/convert-url-to-image-with-python-and-opencv/
        resp = urllib.request.urlopen(url)
        self.image = np.asarray(bytearray(resp.read()), dtype="uint8")
        self.image = cv2.imdecode(self.image, cv2.IMREAD_COLOR)
        print("resizing image")
        print(self.key)
        self.resize_image()
        return

    def resize_image(self):
        #https://medium.com/@manivannan_data/resize-image-using-opencv-python-d2cdbbc480f0
        #Preferable interpolation methods are cv.INTER_AREA for shrinking and cv.INTER_CUBIC(slow) & cv.INTER_LINEAR for zooming. By default, interpolation method used is cv.INTER_LINEAR for all resizing purposes.
        try:
            self.image = cv2.resize(self.image, self.size, interpolation=cv2.INTER_AREA)
        except Exception as e:
            print(str(e))
        self.image = cv2.resize(self.image, self.size, interpolation=cv2.INTER_CUBIC)
        print(self.image.shape)
        print(self.key)

    def pixelate_image(self, 
		       radius = 5, 
                       step = 14, 
                       jitter = 0, 
                       point_shape="circle",
                       radius_expansion_rate=1,
                       min_radius = 1,
                       max_radius = 100,
                       step_expansion_rate=1):
        height, width, channel = self.image.shape

        points = copy(self.image)

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
                if radius * radius_expansion_rate >= min_radius and radius * radius_expansion_rate <= max_radius:
                    radius = int(radius * radius_expansion_rate)
                x = int(i)# + random.randint(1, 2*JITTER-JITTER))
                y = int(j)# + random.randint(1, 2*JITTER-JITTER))
                if(x >= height):
                        x = height-1
                if( y >= width):
                        y = width-1
                gray = self.image[x,y]
                gray = (int(gray[0]),int(gray[1]),int(gray[2]))
                if point_shape=="circle":
                    cv2.circle(points,
                            (y, x),
                            radius,
                            (gray),
                            -1,
                            cv2.LINE_AA)
                elif point_shape=="square":
                    cv2.rectangle(points,
                            (y, x),
                            (int(1 + y + radius/2), int(1 + x + radius/2)),
                            (gray),
                            -1,
                            cv2.LINE_AA)
        self.image = points
        return
