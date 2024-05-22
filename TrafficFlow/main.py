import math
import numpy as np
import os
from matplotlib import pyplot as plt
import scipy.optimize
import sympy as sp 
import pandas as pd
from IPython import get_ipython
from scipy.optimize import curve_fit
import scipy.signal
from scipy.signal import argrelextrema
import matplotlib as mtp
from scipy.stats import norm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython import display
import networkx as nx
import matplotlib.animation as animation
from decimal import Decimal, ROUND_HALF_UP

from sympy.solvers import solve 
from sympy import Symbol
from sympy import*
#from matplotlib.animation import FuncAnimation, PillowWriter 
# import funciones
# get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt5') 

#%%

df = pd.read_csv('dataset_flujo_vehicular.csv')
df= df.drop_duplicates(keep='first')

import datetime as dt
df['HORA'] = df['HORA'].apply(lambda x: dt.datetime.strptime(x,'%d%b%Y:%H:%M:%S')) # Convierto la fecha en formato dd-mm-aaaa...
 

    
