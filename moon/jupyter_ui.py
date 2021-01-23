from moon.dialamoon import Moon
import matplotlib.pyplot as plt

class JupyterUi(Moon):

    def show(self):
        plt.imshow(self.image)
        plt.show()
  
