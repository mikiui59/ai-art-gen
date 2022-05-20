# AI Art Gen
For automating the creation of large batches of AI-generated artwork utilizing VQGAN+CLIP.  
Some example images that I've created via this process:  

<img src="e1.png" width="320">
<img src="e2.png" width="320">
<img src="e3.png" width="320">

# Requirements

You'll need an Nvidia GPU, preferably with a decent amount of VRAM. 12GB of VRAM is sufficient for 512x512 output images, and 8GB should be enough for 384x384. To generate 1024x1024 images, you'll need ~24GB of VRAM. Generating small images and then upscaling via [ESRGAN](https://github.com/xinntao/Real-ESRGAN) or some other package provides very good results as well.

# Install

Clone repo and run `run.sh` to install all dependencies
```
  git clone https://github.com/mikiui59/ai-art-gen.git
  cd ai-art-gen
  
  ./run.sh
```



# Usege

```
usage: vqgan.py [-h] [-p PROMPTS] [-ip IMAGE_PROMPTS] [-i MAX_ITERATIONS]
                [-se DISPLAY_FREQ] [-s SIZE SIZE] [-ii INIT_IMAGE]
                [-in INIT_NOISE] [-iw INIT_WEIGHT] [-m CLIP_MODEL]
                [-conf VQGAN_CONFIG] [-ckpt VQGAN_CHECKPOINT]
                [-nps [NOISE_PROMPT_SEEDS ...]]
                [-npw [NOISE_PROMPT_WEIGHTS ...]] [-lr STEP_SIZE]
                [-cutm {original,updated,nrupdated,updatedpooling,latest}]
                [-cuts CUTN] [-cutp CUT_POW] [-sd SEED]
                [-opt {Adam,AdamW,Adagrad,Adamax,DiffGrad,AdamP,RAdam,RMSprop}]
                [-o OUTPUT] [-vid] [-zvid] [-zs ZOOM_START]
                [-zse ZOOM_FREQUENCY] [-zsc ZOOM_SCALE] [-zsx ZOOM_SHIFT_X]
                [-zsy ZOOM_SHIFT_Y] [-cpe PROMPT_FREQUENCY] [-vl VIDEO_LENGTH]
                [-ofps OUTPUT_VIDEO_FPS] [-ifps INPUT_VIDEO_FPS] [-d]
                [-aug {Ji,Sh,Gn,Pe,Ro,Af,Et,Ts,Cr,Er,Re} [{Ji,Sh,Gn,Pe,Ro,Af,Et,Ts,Cr,Er,Re} ...]]
                [-vsd VIDEO_STYLE_DIR] [-cd CUDA_DEVICE]
```

Random text generator: `python3 random_name_art.py`

# Example
```
  python3 random_name_art.py
  #lemon eye
  CUDA_LAUNCH_BLOCKING=1 python3 vqgan.py -s 600 400 -cd "cuda:0" -lr 0.085 -i 2500 -opt "RMSprop" -p "lemon eye" -in "gradient" -o output/l_eye.png'
```
<img src="l_eye.png" width="320">


## License

[MIT License](http://en.wikipedia.org/wiki/MIT_License)
