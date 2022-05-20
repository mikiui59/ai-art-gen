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
text_one=["A painting of a", "A pencil art sketch of a", "An illustration of a", "A photograph of a"]
text_two=["spinning","dreaming","watering","loving","sleeping","repeating","surreal","psychedelic"]
text_three=["fish","cat","horse","dog","house","door","table","tree","grass", "flower", "plant","bloom", "spanner","spider", "figurine", "statue", "car",  "monitor"]
styles=["Art Nouveau", "Camille Pissarro", "Claude Monet", "Fauvism", "Futurism", "Impressionism",
 "Picasso", "Pop Art", "Modern art", "Surreal Art", "Sandro Botticelli", "oil paints", "watercolours", "weird bananas", "strange colours",'Baroque','Abstract Expressionism','Classicism','Expressionism','Fauvism','Impressionism','Neo Impressionism','Performance Art','Pop Art','Post Impressionism']
place=['forest','sky','space','moon','ice','fire']
t=['in','on','at','into','under']
text_new=["fish","cat","horse","dog","house","table","tree","grass", "plant","bloom", "spanner","spider", "figurine", "statue", "car",  "monitor"]


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
