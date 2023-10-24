import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

with open("eddy_v1/log.txt", 'r') as file:
    eddy_v1 = np.array([int(line.rstrip('\n')) for line in file])

with open("eddy_v2/log.txt", 'r') as file:
    eddy_v2 = np.array([int(line.rstrip('\n')) for line in file])

# WORK IN PROGRESS