import numpy as np
from PIL import Image
from ISR.models import RDN,RRDN
from keras.backend import clear_session

import os
import argparse

parser = argparse.ArgumentParser(description='Ai Art Generator With Upscale Image')

parser.add_argument("-f",    "--file", type=str, help="Image path", default=None, dest='file')

args = parser.parse_args()

name=args.file

rdn = RRDN(weights='gans')

img = Image.open(f'output/{name}.png')
lr_img = np.array(img)

sr_img = rdn.predict(lr_img,by_patch_of_size=30)
image=Image.fromarray(sr_img)
image.save(f'output/{name}.png')
