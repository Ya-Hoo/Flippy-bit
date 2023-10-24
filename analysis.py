import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns
import seaborn.objects as so

with open(r"eddy/log.txt", 'r') as file:
    eddy_v1 = np.array([int(line.rstrip('\n')) for line in file])

with open(r"big ed/log.txt", 'r') as file:
    eddy_v2 = np.array([int(line.rstrip('\n')) for line in file])

# WORK IN PROGRESS