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
import datetime as dt
from sympy.solvers import solve 
from sympy import Symbol
from sympy import*

import requests
from bs4 import BeautifulSoup

#from matplotlib.animation import FuncAnimation, PillowWriter 
# import funciones
# get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt5') 


''' --------- DOWNLOAD & UPDATE --------- '''

def status_url(url): # if res.ok < 400, status = True
    res = requests.get(url)
    status = res.ok
    return status

def get_href(url,y):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    soups = soup.findAll('a', class_ = 'btn') # Busca en todos los elementos que tengan la etiquita 'a' y clase 'btn', y guarda sus contenidos en una lista 'soups'.
    for s in soups :
        if s.get('href')[-8:-4] == y: # Me quedo solo con el contenido que tiene el año que me interesa. 
            return s.get('href')
            
def download_dataset(url,ld):
    r = requests.get(url)
    file = 'dataset' + ld + '.csv'
    with open(file,'wb') as f:
        f.write(r.content)
    return file 
  
#Esta funcion no va a servir para otros datasets que no sean del flujo de AUSA. 
def create_dataframe(file): # Creo un dataframe para poder ordenar los datos de una manera que me facilite analizarlos. 
    
    df = pd.read_csv(file,delimiter=(';'), decimal=",").replace('',np.nan).dropna()
    df['Día, Mes, Año de H_Fecha'] = df['Día, Mes, Año de H_Fecha'].apply(lambda x: x.rstrip('2024'))
    
    # Separo la columna de las fechas en 3 columnas, dia, mes y año. 
    df.insert(1,'Año','2024') 
    df.insert(1,'Mes',df['Día, Mes, Año de H_Fecha'].apply(lambda x: x.partition('/')[2][:-1])) 
    df.insert(1,'Dia',df['Día, Mes, Año de H_Fecha'].apply(lambda x: x.partition('/')[0])) 
    del df['Día, Mes, Año de H_Fecha'] # Borro la columna original de fechas
    return df

def get_last_update(url, year):
    soup = BeautifulSoup(requests.get(url).text, 'html.parser')
    soups = soup.find_all('div', attrs = {"class": "col-xs-7 value"} )
    for s in soups :
        if year in s.get_text(): # Me quedo solo con el contenido que tiene el año que me interesa. 
            return s.get_text().replace(' de ','').strip() #Devuelve string con el formato '22Abril2024'
        
def check_last_update(ld):
    files = os.listdir('/'); name = "dataset"+ ld +'.csv'
    if os.path.exists(name):
        return True
    else:
        return False
    
def update_dataset(df,df_new,df_name,ld):
    name = "dataset"+ ld +'.csv'
    df = pd.concat([df,df_new]).drop_duplicates(keep=False)#If keep = False, drop ALL duplicates!  
    df = df.replace('', np.nan).dropna()   
    os.remove(name)
    os.rename(df_name,name)
    


# cwd = os.getcwd() 
# print("Current working directory:", cwd) 

# files = os.listdir('/') # '/' means current dir
# # print("Files and directories in '", path, "' :") 
# print(dir_list) 

