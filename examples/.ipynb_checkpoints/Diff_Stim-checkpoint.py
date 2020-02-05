###############################################
###########     IMPORT    #####################
###############################################
import os
from os.path import join
import sys
from urllib.request import urlopen
import zipfile
import ssl
from warnings import warn
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt


import LFPy
#import neuron