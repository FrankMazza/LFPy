###############################################################################
###################### Import
###############################################################################
import os
from os.path import join
import sys
import zipfile
import ssl
if sys.version < '3':
    from urllib2 import urlopen
else:
    from urllib.request import urlopen
from warnings import warn
import numpy as np
import scipy.stats
import neuron
import LFPy
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
print('Import complete')

###############################################################################
###################### Compile and Load Mechanisms
###############################################################################
os.system('''
    cd L5bPCmodelsEH/mod
    nrnivmodl
    ''')

mechanisms = neuron.load_mechanisms('L5bPCmodelsEH/mod')
if mechanisms==True:
    print('Mechanisms loaded')
