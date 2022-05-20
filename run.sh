git clone https://github.com/rbbrdckybk/ai-art-generator
cd ai-art-generator

conda install -c anaconda git urllib3
pip3 install transformers keyboard pillow ftfy regex tqdm omegaconf pytorch-lightning IPython kornia imageio imageio-ffmpeg einops torch_optimizer ISR

git clone https://github.com/openai/CLIP
git clone https://github.com/CompVis/taming-transformers

mkdir checkpoints
curl -L -o checkpoints/vqgan_imagenet_f16_16384.yaml -C - "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1"
curl -L -o checkpoints/vqgan_imagenet_f16_16384.ckpt -C - "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1"

