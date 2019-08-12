from moonmask.collage_generator import CollageGenerator
from moonmask.res.ascii_art import *
import numpy as np
import textwrap
import os
import cv2
import shutil
import math
from copy import copy

class TerminalUi(CollageGenerator):
    def __init__(self, size=(1000,1000)):
        super().__init__(size)
        self.gscale1 = "#########*oaZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.         "
        self.gscale2 = ' #@%#*+=-:. '

        self.terminal_width = shutil.get_terminal_size().columns
        self.text_width = int(self.terminal_width * 0.75)
        self.text_margin = int(self.terminal_width * 0.12)
        self.text_wrapper = textwrap.TextWrapper(width=self.text_width)
        self.margin_symbols = " "*(self.text_margin - 2)+"  "

        self.columns_per_image = 30 
        self.text_description_width = 30

    def preview(self):
        
        image_ascii_list = {} 
        for image_key in self.image_store:
            im_copy = copy(self.image_store[image_key].image)
            image_ascii_list[image_key] = self.convertImageToAscii(im_copy, self.columns_per_image, .5, self.gscale2)

        if len(image_ascii_list) > 0:
            self.print_ascii_art(IMAGES_TEXT)
            image_ascii_art_reordered = self.combine_ascii_images_on_line(image_ascii_list)
            self.print_ascii_art(image_ascii_art_reordered)

        collage_ascii_list = {}
        for image_key in self.collage_store:
            im_copy = copy(self.collage_store[image_key].composite) 
            collage_ascii_list[image_key] = self.convertImageToAscii(im_copy, self.columns_per_image, .5, self.gscale2)
        
        if len(collage_ascii_list) > 0:
            self.print_ascii_art(COLLAGES_TEXT)
            collage_ascii_art_reordered = self.combine_ascii_images_on_line(collage_ascii_list)
            self.print_ascii_art(collage_ascii_art_reordered)

    def show_image(self, image_key):
        self.print_text("Press any key to close the image")
        cv2.imshow(image_key, self.image_store[image_key].image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_collage(self, collage_key):
        self.text_format("Press any key to close the image")
        cv2.imshow(collage_key, self.collage_store[collage_key].composite)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def combine_ascii_images_on_line(self, image_ascii_list):
        image_ascii_formatted_list = []
        #self.text_width

        #we're going to make a list of lists
        #it will combine the 1st, 2nd, nth row of each image ascii art
        #each outlined by a border and with some textual description
        #on the right of the image

        #figure out how many images will fit on each line
        images_per_line = math.floor(self.text_width / (self.columns_per_image + self.text_description_width))

        #find out how many lines of images there will be
        lines_of_images = math.ceil(len(image_ascii_list) / images_per_line)
        
        #split dict of images into separate groups of # of images per line
        grouped_images_list = []
        image_keys = list(image_ascii_list.keys())
        num_rows=len(image_ascii_list[image_keys[0]])

        for x in range(lines_of_images):
            grouped_images_list.append([])
            for y in range(images_per_line):
                if len(image_keys) > 0:
                    grouped_images_list[x].append(image_keys.pop())
      
        grouped_images_dict = [] 
        for y in range(lines_of_images):
            grouped_images_dict.append({})
            for x in range(images_per_line):
                if x < len(grouped_images_list[y]):
                    grouped_images_dict[y][grouped_images_list[y][x]] = image_ascii_list[grouped_images_list[y][x]]
        image_names = []
        for group in range(len(grouped_images_dict)):
            image_names_line = []
            for image in grouped_images_dict[group]:
                image_names_line.append(image)
            image_names.append(image_names_line)
        
        ascii_image_lines = []
        for image_group_number in range(len(grouped_images_dict)):
            ascii_image_line = []
            for i in range(num_rows):
                terminal_line = [] 
                for image_key in grouped_images_dict[image_group_number]:
                    terminal_line.append(grouped_images_dict[image_group_number][image_key][i])
                ascii_image_line.append(terminal_line)
            ascii_image_lines.append(ascii_image_line)

        images_ascii_art = []
        for image_block_line in ascii_image_lines:
            for line in image_block_line:
                terminal_line = "                         ".join(line)
                images_ascii_art.append(terminal_line)
            images_ascii_art.append(" ")
        
        return images_ascii_art

        for x in image_names:
            x = (self.columns_per_image*" ").join(x)
            print(x) 
   
    def print_ascii_art(self, ascii_art_list):
        for element in ascii_art_list:
            self.print_text(element[:self.text_width])
        print("")

    def text_format(self,text):
        return textwrap.indent(text=self.text_wrapper.fill(text=text), prefix=self.margin_symbols)

    def print_list(self, list_to_print):
        for element in list_to_print:
            self.print_text((" * " + element))
            print("")

    def print_text(self, text):
        print(self.text_format(text))

    def print_multiline_text(self, text_list, substitute_text=""):
        for text in text_list:
            self.print_text(text.format(self.command_prompt + substitute_text))
            print("")

    def rgb_to_gray(self, img):
        grayImage = np.zeros(img.shape)
        R = np.array(img[:, :, 0])
        G = np.array(img[:, :, 1])
        B = np.array(img[:, :, 2])

        R = (R *.299)
        G = (G *.587)
        B = (B *.114)

        Avg = (R+G+B)
        grayImage = img

        for i in range(3):
           grayImage[:,:,i] = Avg

        return grayImage       

    ### PYTHON TO ASCII ART - https://github.com/electronut/pp/blob/master/ascii/ascii.py#L2 modified to just take numpy images

    def getAverageL(self, im):
        """
        Given PIL Image, return average value of grayscale value
        """
        # get shape
        w = im.shape[0]
        h = im.shape[1]
        # get average
        #cv2.imshow("test", im)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        return np.average(im)
    
    def convertImageToAscii(self, im, cols, scale, moreLevels):
        """
        Given Image and dims (rows, cols) returns an m*n list of Images 
        """
        # declare globals
        # open image and convert to grayscale
        im = self.rgb_to_gray(im)
        # store dimensions
        W, H = im.shape[0], im.shape[1]
        # compute width of tile
        w = W/cols
        # compute tile height based on aspect ratio and scale
        h = w/scale
        # compute number of rows
        rows = int(H/h)
        
        # check if image size is too small
        if cols > W or rows > H:
            print("Image too small for specified cols!")
            exit(0)
    
        # ascii image is a list of character strings
        aimg = []
        # generate list of dimensions
        for j in range(rows):
            y1 = int(j*h)
            y2 = int((j+1)*h)
            # correct last tile
            if j == rows-1:
                y2 = H
            # append an empty string
            aimg.append("")
            for i in range(cols):
                # crop image to tile
                x1 = int(i*w)
                x2 = int((i+1)*w)
                # correct last tile
                if i == cols-1:
                    x2 = W
                # crop image to extract tile
                #print(x1)
                #print(x2)
                #print(y1)
                #print(y2)
                img = im[x1:x2, y1:y2]
                #print(img)
                # get average luminance
                avg = int(self.getAverageL(img))
                # look up ascii char
                if moreLevels:
                    gsval = self.gscale1[int((avg*69)/255)]
                else:
                    gsval = self.gscale2[int((avg*9)/255)]
                # append ascii char to string
                aimg[j] += gsval
        
        # return txt image
        return aimg
   
