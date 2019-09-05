from moon.dialamoon import Moon
import cv2

class TerminalUi(Moon):
    def show(self):
        print("☽ the image will open up in a new window. It might be behind your terminal window. To close the image, press any key while it's open.")
        cv2.imshow(str(self.datetime), self.image)
        cv2.waitKey(0)
        print("Closing image...")
        cv2.destroyAllWindows()

  
