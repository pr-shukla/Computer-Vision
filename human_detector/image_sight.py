# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:02:13 2020

@author: HP
"""

from os import listdir
from os.path import isdir
from PIL import Image
import matplotlib.pyplot as plt
from numpy import savez_compressed
from numpy import asarray
#from mtcnn.mtcnn import MTCNN
import numpy as np
from numpy import load
from numpy import expand_dims
from numpy import asarray
from numpy import savez_compressed
#from keras.models import load_model

from numpy import load

filename = input('Please Enter the file name:' )

image = Image.open(filename)
image_array = asarray(image)

plt.imshow(image_array)
plt.show()
