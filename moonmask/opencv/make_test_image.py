import cv2
import numpy as np
COLORS = [(0,0,0), (255,0,0), (255,255,255)]
SIZE = (10,10)
IMAGE = np.zeros((SIZE[0],SIZE[1],3), np.uint8)
IMAGE[:,0:int(SIZE[0]/3)] = COLORS[0]
IMAGE[:,int(SIZE[0]/3):int(2 * SIZE[0]/3)] = COLORS[1]
IMAGE[:,int(2 * SIZE[0]/3):SIZE[0]] = COLORS[2]
