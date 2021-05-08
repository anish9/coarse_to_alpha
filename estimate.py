from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession

config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

import tensorflow as tf
import numpy as np
import cv2
from utils import *

pred = tf.keras.models.load_model("estimate.h5")

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