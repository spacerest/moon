from moonmask.collage import Collage
from moonmask.moon_image import MoonImage
from moonmask.custom_image import CustomImage
from moonmask.mask import Mask
from copy import deepcopy

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

    def add_new_image(self, key, image=None):
        self.image_store[key] = image 

    def add_new_mask(self, key, **kwargs):
        self.mask_store[key] = Mask(self.size, key, **kwargs) 

    def select_collage(self, key):
        self.selected_collage = self.collage_store[key]

    def load_new_image(self, key, **kwargs):
        self.image_store[key] = CustomImage(self.size, key, **kwargs)

    def duplicate_mask(self, source_key, destination_key):
        self.mask_store[destination_key] = deepcopy(self.mask_store[source_key])

    def duplicate_image(self, source_key, destination_key):
        self.image_store[destination_key] = deepcopy(self.image_store[source_key])

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

    def collage_to_image(self, collage_key, destination_image_key):
        self.load_new_image(destination_image_key, image_array=self.collage_store[collage_key].composite)

    def image_to_mask(self, source_image_key, destination_mask_key, **kwargs):
        self.add_new_mask(destination_mask_key, image=self.image_store[source_image_key].image, **kwargs)

 
