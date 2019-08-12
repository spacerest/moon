import numpy as np

SIZE = (1000,1000)
HALF_SIZE = (int(SIZE[0]/2), int(SIZE[1]/2))
DATE = "2019-07-23"
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

IMAGE_URL="https://lh3.googleusercontent.com/EnanLZTdQ4ArK42RmR0DDa03XiLrw9y0VpUru7RUF-ICAdbrv_W8Voqpy6DdbuAwwgGkyxYnAx56EAXpdOnDDHUcLpuIMhTC9f5zfBvUF-C1AlR48TsyTfCtvqkIyGM_lUOmUHCz7AK5WOKtSdYpBfPML-Lyvu6yDs5FavrdIz5iq7RBfGD1asxOCbALxBJNJRckD4pMTvR2ZT_Un6taryj2tzc2uUFyQU7Jr0dp7TGXVru99FIL4i_aVjBpGHuvN-unVRYLG0COfnnCAcCjsveHmZ1NfakQ22DR4Ov98ZfTk5pd7eKdsP6t6zjCM-FcsSHJbqE2xLChwUuZQ_dcqJ4N2Nu_-oD-ZknS4M3oRWyOK5rMuNiDQVE-VyiwYal3gMyYgu6vLAAjdzP6GACse6tcoxYFG9gROeaAKgvjTtxHDnNS1Ky5ERhuh1M2gg2ig3TH4eR1ypcxtGqqxSkDmeWI_2Rfp7d_5zh0dGLgSw7N7LcpERqeEsCtFx40XXp1C659LcEe3RJ0ZasiQ8v85RxtsSbN_50l8eVSW32N3vp6Q-bO60M1w2o-uPkNq5-BaJOhtuK6lb1Txn2powgQCd1yKIoKNOYqqigaoj2O1XZyLsFq2ISB3fsGj1gudo7Rwb-V0Awh9c6q63C3lKpVde2vVxRq96Sw=w566-h585-no"
