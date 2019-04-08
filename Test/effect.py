import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as ff

import pandas as pd
import scipy

import numpy as np
 
import wave
 
import struct
 
import matplotlib.pyplot as plt

from scipy import signal

file = "test.wav"
wav_file=wave.open(file, 'r')

print(wav_file.getparams())
