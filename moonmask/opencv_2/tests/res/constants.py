import numpy as np

SIZE = (1000,1000)
HALF_SIZE = (int(SIZE[0]/2), int(SIZE[1]/2))
DATE = "2019-07-21"
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

DOT_IMAGE = np.zeros((SIZE[0],SIZE[1],3), np.uint8)
DOT_IMAGE[:,int(SIZE[0]/2):SIZE[0]] = (255, 255, 255)

IMAGE_URL="https://lh3.googleusercontent.com/QWQNGWFGzsOqw9OLMWkiUkJ6sqhhqXfZf_D7kGuLy1hYfHTW1JoZSr351GIZntmw_Fjb5FbpDfqhgm3tKTlLdXVjxXhSwar4tOQ2hF2INNLZZ0U_Pvyjo92CWCgOY0zihbpUrd_3DQ6QgjEo_YnyGh2Rxll5gTLUMWATOO4LJkL_hfIKcSbBllK-QabtMPTgy-UIt9dtHCVn9mNh6-eVw3hxT5ycwWrIdMDYqW7pDouMV7U5wo-XRcWBMMiX305TTEXurxfxjlBQffPhhmUo1AG5O1YZq3ehohg9FurDyeP855tvG1tOWAoAHvaKHH-Qqlp1o_UfNLNW-wSzX64AKLjM1nULBVB3sSu_GpwkU3T-jtrQfd0PWflhu1Y_WcQAhO0DPZMNsvInXZNZsDGZdv6SPxIHzJ9XDULlvZSVX-xgi-qTOcLZlYEqVXgAA1fX1JvkL3R5aG3SOEr4YU-2wbFU3LAJX5W4PWK6umrNptdL5a_Myk_OYd6Pxk-gUZDGl0DfyqZmCXthZlSP6km_E2G7sMcij_OpdFq7wnBcPb71zYo1geD-6dWwQuVFBn7g0Mb7zbi8f1RS7wbp_pZ-D3_P_ODVRElaJVbdNxPpUnVek9LB_FfxM3tBqF1ifQ5Ck_yttkwGfWb3U2lOWHpiDI24Ql7Erg_e=w782-h585-no"
