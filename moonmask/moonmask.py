from collage import Collage
from instagram_wrapper import InstagramWrapper

class MoonMask():

    def __init__(self):
        self.collage = Collage()
        self.instagram = None
        self.moonmask_filename = None

    def set_moon_phase(self, date=None, relative_date="today", filename=None):
        """Sets the moon phase that will be used as a mask on the image

        Keyword arguments:
        date -- the date in format YYYYMMDD
        relative_date -- defaults to "today". Other accepted options are "yesterday" and "tomorrow"
        """
        self.collage.set_mask(date, relative_date, filename)

    def set_main_image(self, url="", instagram_url="", filename="", color=""):
        self.collage.set_main_image(url, instagram_url, filename, color)

    def set_negative_space(self, url="", instagram_url="", filename="", color=""):
        self.collage.set_mask_negative_space(url, instagram_url, filename, color)

    def set_positive_space(self, url="", instagram_url="", filename="", color=""):
        self.collage.set_mask_positive_space(url, instagram_url, filename, color)

    def save_collage(self, filename="moonmask", main_image_file=None, mask_file=None, positive_space_file=None, negative_space_file=None, positive_space_transparency=200, negative_space_transparency=50, dimensionality=3, img_size=1000):
        self.collage.make_collage(filename, main_image_file, mask_file, positive_space_file, negative_space_file, positive_space_transparency, negative_space_transparency, dimensionality, img_size)
        self.moonmask_filename = filename + ".jpg"

    def post_to_instagram(self, username, password, caption="", save_session=False, usertags=[]):
        self.instagram = InstagramWrapper(username, password, save_session)
        self.instagram.post_image(self.moonmask_filename, caption, usertags=usertags)


