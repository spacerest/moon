from copy import deepcopy
import numpy as np

class Collage():
    def __init__(self, key):
        self.key = key
        self.negative_space = None
        self.positive_space = None

    def __str__(self):
        return self.key

    def set_negative_space(self, custom_image):
        self.negative_space = custom_image

    def set_positive_space(self, custom_image):
        self.positive_space = custom_image

    def set_mask(self, mask_container):
        self.mask = mask_container

    def combine(self):
        #helpful post: https://stackoverflow.com/questions/46267443/merge-images-using-opencv-and-a-mask
        #making masks: https://codereview.stackexchange.com/questions/184044/processing-an-image-to-extract-green-screen-mask
        #creating alpha gradient image https://note.nkmk.me/en/python-numpy-generate-gradation-image/

        if len(self.mask.mask.shape) != 2:
            mask = self.mask.prepare_mask_for_collage_combine()#WHEN I COMMENT OUT 255, COLOR STAYS AT POSITIVE SPACE COLOR
            self.composite = (self.positive_space.image * mask + self.negative_space.image * (1 - self.mask.mask)).astype(np.uint8)
        #CREATES A composite image FROM boolean mask
        else:
            self.composite = copy(self.positive_space.image)
            self.composite[~self.mask.mask] = self.positive_space.image[~self.mask.mask]
            self.composite[self.mask.mask] = self.negative_space.image[self.mask.mask]#.astype(float))
