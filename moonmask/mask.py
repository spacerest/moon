import cv2
import numpy as np
from copy import copy
from bisect import bisect_left

class Mask():

    def __init__(self, size, key, image = [], alpha_values=0, mask_divisor=255,prep_mask_divisor=1):
        self.image = image
        self.key = key
        self.size = size
        self.mask_divisor = mask_divisor 
        self.prep_mask_divisor = prep_mask_divisor
        self.mask = self.set_mask(alpha_values) if len(image) > 0 else None

    def set_mask(self, alpha_values):
        """
        if alpha values is 0, all grey values in the image
        will be included in the mask
        """
        print("set mask method called")
        mask = self.rgb_to_gray(self.image)
        mask = mask / self.mask_divisor 
        if not alpha_values == 0:
            mask = self.normalize_mask_values(mask, alpha_values)
        return mask

    def prepare_mask_for_collage_combine(self):
        #WHEN PREP_MASK_DIVISOR IS 255, COLOR STAYS AT POSITIVE SPACE COLOR
        return self.mask / self.prep_mask_divisor

    def normalize_mask_values(self, mask, alpha_values):
        interval = 1.0 / (alpha_values - 1)
        values_list = []
        for x in range(alpha_values):
            values_list.append(x * interval) 
        for a in range(len(mask)):
            for b in range(len(mask[a])):
                for c in range(len(mask[a][b])):
                    mask[a][b][c] = self.take_closest(values_list, c)
        return mask


    def take_closest(self, sorted_list, number):
        """
        source: https://stackoverflow.com/a/12141511/5650506
        Assumes sorted_list is sorted. Returns closest value to number.
    
        If two numbers are equally close, return the smallest number.
        """
        pos = bisect_left(sorted_list, number)
        if pos == 0:
            return sorted_list[0]
        if pos == len(sorted_list):
            return sorted_list[-1]
        before = sorted_list[pos - 1]
        after = sorted_list[pos]
        if after - number < number - before:
           return after
        else:
           return before

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


