import numpy as np
from PIL import Image
from ISR.models import RDN,RRDN
from keras.backend import clear_session

import os

name=input('Path to image: ')

rdn = RRDN(weights='gans')

img = Image.open(f'output/{name}.png')
lr_img = np.array(img)

sr_img = rdn.predict(lr_img,by_patch_of_size=30)
image=Image.fromarray(sr_img)
image.save(f'output/{name}.png')
