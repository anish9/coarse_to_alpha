"""utils for estimator"""
import tensorflow as tf



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