import numpy as np

SIZE = (5,5)
HALF_SIZE = (int(SIZE[0]/2), int(SIZE[1]/2))
DATE = "2019-07-17"
FRAME_ID = '4729'
URL = "https://svs.gsfc.nasa.gov/vis/a000000/a004400/a004442/frames/730x730_1x1_30p/moon.4729.jpg"

COLORS = [(255,100,255), (255,100,255), (255,100,255)]
IMAGE = np.zeros((SIZE[0],SIZE[1],3), np.uint8)
IMAGE[:,0:int(SIZE[0]/3)] = COLORS[0]
IMAGE[:,int(SIZE[0]/3):int(2 * SIZE[0]/3)] = COLORS[1]
IMAGE[:,int(2 * SIZE[0]/3):SIZE[0]] = COLORS[2]

COLORS = [(200,255,210), (200,255,210), (200,255,210)]
IMAGE2 = np.zeros((SIZE[0],SIZE[1],3), np.uint8)
IMAGE2[:,0:int(SIZE[0]/3)] = COLORS[0]
IMAGE2[:,int(SIZE[0]/3):int(2 * SIZE[0]/3)] = COLORS[1]
IMAGE2[:,int(2 * SIZE[0]/3):SIZE[0]] = COLORS[2]

DOT_IMAGE = np.zeros((3,3,3), np.uint8)
DOT_IMAGE[:,1:3] = (255, 255, 255)

IMAGE_URL = "https://lh3.googleusercontent.com/HA3nuOhRhdZLEqcu5hOUKlh83oMepXBgA9REvo0ZgaZmOdTzsXly-qyXtYa8ky-toxXSdQDb0I2tk8FKVx2_Et0jWz9W1UX9TU7z5deYY3lv6snpF0Dx5YH3NT6A_GbWizGFcOSgsNGCWVO7W6QHrOXGfswcDokCxAnehYDYvd7XtOv3uUDOZ9Oz7gbIFUOFPyRI7yVdX2sv0Hb-ixLpy7VGYtrFK8dquVEMtQCx6f4f91NbSI26wiAz9xWy_e-_XLCsOgY6BjqbZbZHS0H0fBlgvuBtmFzUF_BGB1BFmhnaHlEWRI6bG3hRrXFqEoTDfBAH3KiPgxdIdMRJNNDK7z_2tH0JPgiVefOV-gbt_iXNia-Err_cua2ftw_D0RzloXygLNkGu04h5lb252jrcl-j0wI42t2YtJaGHbwQpj_n7RgsfJH9kiQFQ-Ln9KXZJFjxIxGSuP_bQkzYI2L9TdGpKrytybBP7n-kQfBA48p1-Qw1wmDMvrhlRz_gHOHc_3vipstdAdaa7JZc_Ct2saD5blRr3LEJ4wZEQ5mhxKwJLnQqSo-c43UwQo9hD8utk-_Z5xZH_o87UdQmtecLGAu3RY-d9m0iXY01CvSnphG_I_oATTNYOETvMT-3RkQGJjsGxWuhyo9W9KyLVv_-kfK_ey0hwjp3=w439-h585-no"
