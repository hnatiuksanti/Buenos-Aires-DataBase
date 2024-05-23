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
import requests
from bs4 import BeautifulSoup
 
def status_url(url): # if res.ok < 400, status = True
    res = requests.get(url)
    status = res.ok
    return status

def get_href(url):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    soups = soup.findAll('a', class_ = 'btn')
    for s in soups :
        if s.get('href')[-8:-4] == year:
            return s.get('href')
            
def save_in_folder(url):
    r = requests.get(url)
    file = 'traffic_flow' + year + '.csv'
    with open(file,'wb') as f:
        f.write(r.content)
    return file   
if __name__ == '__main__':
    url = 'https://data.buenosaires.gob.ar/dataset/flujo-vehicular-por-radares-ausa'; year = '2024'
    if status_url(url) == True:
        link = get_href(url)
        file = save_in_folder(link)
    else:
        print(False)
#%%

df = pd.read_csv('dataset_flujo_vehicular.csv')
df = df.drop_duplicates(keep='first')
df = df.dropna(how='any')    #to drop if any value in the row has a nan
import datetime as dt
df['HORA'] = df['HORA'].apply(lambda x: dt.datetime.strptime(x,'%d%b%Y:%H:%M:%S')) # Convierto la fecha en formato dd-mm-aaaa...

detectors = df.drop_duplicates(subset= ['CODIGO_LOCACION'],keep = 'last')
print(detectors)

#%%

df2 = pd.read_csv(file)
df2 = df2.drop_duplicates(keep='first')
df2 = df2.dropna(how='any') 

detectors2 = df2.drop_duplicates(subset= ['Disp Nombre'],keep = 'first')
print(detectors2)

