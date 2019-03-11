from PIL import Image

class Mask():
    def __init__(self, image, alpha_threshold, img_size, transparency=0):
        self.alpha_threshold = alpha_threshold
        self.transparency = transparency
        self.image = image
        self.image = self.image.resize(img_size, Image.ANTIALIAS)
        self.make_mask()
        return

    def make_mask(self):
        self.image = self.image.point(lambda p: p > self.alpha_threshold and 255)
        if (self.transparency != 0):
            self.image = self.image.point(lambda p: self.transparency)
        self.image = self.image.convert("L")
        return

    def get_mask(self):
        return self.image
