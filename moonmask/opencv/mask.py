import cv2
import numpy as np
from copy import copy

class Mask():

    def __init__(self, key, image):
        self.image = image
        self.key = key
        self.mask = self.set_mask()
        self.pixelated_mask = self.pixelate_mask()

    def set_mask(self):
        mask = self.rgb_to_gray(self.image)
        mask = mask / 255
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


    def pixelate_mask(self, radius = 15, step = 34, jitter = 0):
        #height, width, channel = self.image.shape

        #points = copy(self.image)

        #for i in range(height):
        #    for j in range(width):
        #        points[i, j] = 255
        #xrange = np.zeros(int(height/step))
        #yrange = np.zeros(int(width/step))
        #for xvalue in range(len(xrange)):
        #    xrange[xvalue] = xvalue
        #for yvalue in range(len(yrange)):
        #    yrange[yvalue] = yvalue
        #xrange = [value*step+step/2 for value in xrange]
        #yrange= [value*step+step/2 for value in yrange]
        #np.random.shuffle(xrange)
        #for i in xrange:
        #    np.random.shuffle(yrange)
        #    for j in yrange:
        #        x = int(i)# + random.randint(1, 2*JITTER-JITTER))
        #        y = int(j)# + random.randint(1, 2*JITTER-JITTER))
        #        if(x >= height):
        #                x = height-1
        #        if( y >= width):
        #                y = width-1
        #        gray = self.image[x,y]
        #        cv2.circle(points,
        #                (y, x),
        #                radius,
        #                int(gray),
        #                -1,
        #                cv2.LINE_AA)
        #self.pixelated_mask = points
        return

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


