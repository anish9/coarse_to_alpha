from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import tensorflow as tf
import numpy as np
import cv2

import sys

root_ = [x for x in sys.path if x.endswith("3.6")]

try:
    pred = tf.keras.models.load_model(root_[0]+"/site-packages/alphax/estimate.h5")
except:
    pred = tf.keras.models.load_model(root_[1]+"/site-packages/alphax/estimate.h5")

def process_image(x,norm=True):
    x    = tf.io.read_file(x)
    x    = tf.io.decode_png(x,channels=3)
    x    = tf.cast(x,tf.float32)
    rgb  = x
    if norm:
        rgb = rgb/255.
    return rgb

def process_mask(x,norm=False):
    x = tf.io.read_file(x)
    x = tf.io.decode_png(x,channels=1)
    x = tf.cast(x,tf.float32)
    if norm:
        x = x/255.
    return x

def process_alpha(x,norm=True):
    x    = tf.io.read_file(x)
    x    = tf.io.decode_png(x,channels=1)
    x    = tf.cast(x,tf.float32)
    if norm:
        x = x/255.
    return x

def edge_estimator(RGB_FILE,MASK_FILE):
    inputim = process_image(RGB_FILE)
    inputma = process_mask(MASK_FILE)
    h,w = inputim.shape[:2]
    h,w = 32*(h//32),32*(w//32)
    iim = tf.expand_dims(tf.image.resize(inputim,(h,w)),axis=0)
    ima = tf.expand_dims(tf.image.resize(inputma,(h,w)),axis=0)
    esti = pred.predict((iim,ima))
    esti = esti*255.
    return np.uint8(esti[0])

# cv2.imwrite("out.png",edge_estimator("alpha_data/image/V1_00052696-02.jpg","alpha_data/mask/V1_00052696-02.png"))