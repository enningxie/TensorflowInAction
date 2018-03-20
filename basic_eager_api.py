'''
    Eager execution is an imperative, define-by-run interface where operations are
executed immediately as they are called from Python. This makes it easier to
get started with TensorFlow, and can make research and development more
intuitive.
'''

from __future__ import division, absolute_import, print_function

import numpy as np
import tensorflow as tf
import tensorflow.contrib.eager as tfe

# set Eager API
print("setting eager mode...")
tfe.enable_eager_execution()

# Define constant tensors
print('define constant tensors')
a = tf.constant(2)
print('a = %i' % a)
b = tf.constant(3)
print('b = %i' % b)

