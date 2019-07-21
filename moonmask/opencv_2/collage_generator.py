from moonmask.opencv_2.collage import Collage
from moonmask.opencv_2.moon_image import MoonImage
from moonmask.opencv_2.custom_image import CustomImage
from moonmask.opencv_2.mask import Mask

class CollageGenerator():
    def __init__(self, size):
        self.collage_store = {}
        self.image_store = {} 
        self.mask_store = {} 
        self.selected_collage = None
        self.size = size

    def start_new_collage(self, keyword):
        self.collage_store[keyword] = Collage(keyword)
        self.selected_collage = self.collage_store[keyword]

    def add_new_image(self, key):
        self.image_store[key] = key

    def add_new_mask(self, key, **kwargs):
        self.mask_store[key] = Mask(self.size, key, **kwargs) 

    def select_collage(self, key):
        self.selected_collage = self.collage_store[key]

    def load_new_image(self, key, **kwargs):
        self.image_store[key] = CustomImage(self.size, key, **kwargs)

    def set_moon(self, key, **kwargs):
        """Sets the image that will be used as a mask on the image
        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """
        self.image_store[key] = MoonImage(self.size, key)
        self.image_store[key].set_moon_image(**kwargs)
        self.image_store[key]
        
        return

 
