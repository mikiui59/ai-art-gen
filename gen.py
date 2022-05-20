import os
import numpy as np

import argparse

from PIL import Image
from ISR.models import RDN,RRDN
from keras.backend import clear_session
import gc
import subprocess
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Ai Art Generator With Upscale Image')

parser.add_argument("-p",    "--prompts", type=str, help="Text prompts", default=None, dest='prompts')
parser.add_argument("-i",    "--iterations", type=int, help="Number of iterations", default=1500, dest='max_iterations')
parser.add_argument("-s",    "--size", nargs=2, type=int, help="Image size (width height) (default: %(default)s)", default=[600,400], dest='size')

if __name__ == "__main__":

  args = parser.parse_args()
  
  text=args.prompts
  itr=args.max_iterations
  size=args.size
  
  if text==None:
    text=input('Enter prompts: ')

  n=text
  name=n.replace(' ','_')
  
  os.system(f'CUDA_LAUNCH_BLOCKING=1 python3 vqgan.py -s {size[0]} {size[1]} -lr 0.085 -i {itr} -opt "RMSprop" -p "{n}" -in "gradient" -o output/{name}.png')

  rdn = RRDN(weights='gans')

  img = Image.open(f'output/{name}.png')
  lr_img = np.array(img)

  sr_img = rdn.predict(lr_img,by_patch_of_size=30)
  image=Image.fromarray(sr_img)
  image.save(f'output/{name}.png')

  f=open('output/art.txt','a')
  f.write(f'output/{name}.png\n')
  f.close()

  del rdn,image,lr_img
