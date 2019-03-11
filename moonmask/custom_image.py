from PIL import Image
import urllib.request
import io

class CustomImage():
    def __init__(self, img_size):
        self.size = img_size
        return

    def set_image(self, url="", instagram_url="", filename=""):
        #if more than one of these parameters are provided, raise an error.
        #TODO check for a cleaner way to do this
        if (url and instagram_url) or (url and filename) or (instagram_url and filename):
            raise Exception("set_image takes only one parameter")

        if url: return self.load_from_url(url)
        if instagram_url: return self.load_from_instagram(instagram_url)
        if filename: return self.load_from_filesystem(filename)

    def load_from_instagram(self, instagram_url):
        #TODO check if link has extra info at the end
        #https://nono.ma/says/get-an-instagram-image-url
        try:
            self.load_from_url(instagram_url + "media/?size=l")
        except:
            raise Exception("I can't seem to download that image from that link: " + instagram_url + ". Check that it's an instagram link in the form 'https://instagram.com/p/SOME_NUMBERS_AND_LETTERS/'.")
        return self.image

    def load_from_filesystem(self, path):
        self.image = Image.open(path)
        self.resize_image()
        return self.image

    def load_from_url(self, url):
        print("Requesting image from the internets...")
        print(" ,-,\n/.(\n\ {\n `-`")
        fd = urllib.request.urlopen(url)
        image_file = io.BytesIO(fd.read())
        self.image = Image.open(image_file)
        self.resize_image()
        print("Got it!")
        return self.image

    def resize_image(self):
        self.image.resize(self.size, Image.ANTIALIAS)
