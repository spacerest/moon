from moonmask.res.fonts import *
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image
from moonmask.mask import Mask

class WordMask():
    def __init__(self, size, invert, color="black"):
        self.size = size
        self.font = ImageFont.truetype("moonmask/res/fonts/zillah_modern_thin.ttf", 31)
        self.invert = invert
        self.fill = "white"
        self.color = color
        if self.invert:
            self.color="white"
            self.fill="black"
        self.image = Image.new('RGB', self.size, self.color)
        return

    def set_word_mask(self, words="test"):
        """Repeats a string and prints it on an image

        Keyword arguments:
        words -- the string to be repeated and printed on the image
        """

        draw = ImageDraw.Draw(self.image)
        words = self.format_string(words)
        draw.text((-45, -50), words, font=self.font, fill=self.fill)
        #self.image.show()
        self.mask = Mask(self.image, 0, self.size).get_mask()

    def get_word_mask(self):
        #self.mask.show()
        return self.mask

    def format_string(self, words):
        words_char_length = len(words)
        times_to_repeat = words_char_length * 20
        words = (words) * times_to_repeat
        words_char_length = len(words)
        n = 120

        #insert newline every n characters
        split_words = [words[i:i+n] for i in range(0, words_char_length, n)]
        split_words = "\n".join(split_words)

        return split_words



