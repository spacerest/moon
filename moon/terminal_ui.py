from moon.dialamoon import Moon
import cv2
import matplotlib.pyplot as plt

class TerminalUi(Moon):
    def show(self):
        print("☽ the image will open up in a new window. It might be behind your terminal window.")
        try:
            plt.imshow(cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB))
            plt.show()
            print("Image closed.")
        except:
            e = sys.exc_info()[1]
            print("Error: %s" % e) 
