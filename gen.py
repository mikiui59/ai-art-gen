import random
import os
import torch
from IPython.display import HTML, Javascript, display
import numpy as np
from PIL import Image
from ISR.models import RDN,RRDN
from keras.backend import clear_session
import gc
import subprocess
from tqdm import tqdm

with open('text.txt','r') as f:
  text=f.read()

n=text
name=n.replace(' ','_')
os.system(f'cd ai-art-generator && CUDA_LAUNCH_BLOCKING=1 python3 vqgan.py -s 600 400 -cd "cuda:0" -lr 0.085 -i 2500 -opt "RMSprop" -p "{n}" -in "gradient" -o output/{name}.png')

rdn = RRDN(weights='gans')

img = Image.open(f'ai-art-generator/output/{name}.png')
lr_img = np.array(img)

sr_img = rdn.predict(lr_img,by_patch_of_size=30)
image=Image.fromarray(sr_img)
image.save(f'ai-art-generator/output/{name}.png')

f=open('ai-art-generator/output/art.txt','a')
f.write(f'ai-art-generator/output/{name}.png\n')
f.close()

del rdn,image,lr_img
