import funciones as f
import pandas as pd
import os
import numpy as np
import time
# link = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/ausa/flujo-vehicular-por-radares-ausa/flujo-vehicular-por-radares-2024.csv '
t0 = time.time()
if __name__ == '__main__':
    url = 'https://data.buenosaires.gob.ar/dataset/flujo-vehicular-por-radares-ausa'; year = '2024'
    if f.status_url(url):
        last_date = f.get_last_update(url, year) 
        df_name = list(filter(lambda x: x.endswith('.csv') and year in x, os.listdir(os.getcwd())))
        if df_name != []:
            if not f.check_last_update(last_date):
                df = pd.read_csv(df_name[0]) #Abro el dataset que voy a actualizar
                href = f.get_href(url,year) #Obtengo el archivo para descargar. 
                df_new = f.create_dataframe(f.download_dataset(href,last_date)) #Descargo el archivo y creo el nuevo dataframe 
                f.update_dataset(df,df_new,df_name[0],last_date)
                print('¡Dataset actualizado!')
            else:
                print('No hay actualizaciones nuevas.')
        else:
            href = f.get_href(url,year) 
            df_new = f.create_dataframe(f.download_dataset(href,last_date))
            os.remove('dataset'+last_date+'.csv')
            df_new.to_csv('dataset'+last_date+'.csv', index = False)
            print('¡Dataset descargado!')
    else:
        print('Status url: ',False)
print(time.time() - t0)
#%%
''' Graficar en mapa de Buenos Aires '''
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt5') 
import plotly.express as px
import plotly.io as pio

df = df_new[ (df_new['Dia']==20) & (df_new['Mes']==2)] #Filtro por dia y mes. 

# Luego de filtrar, Creo df nuevos con las columnas de datos que me interesan mostrar.
df['Lat']= df['Disp Lat']  ; df['Lon'] =  df['Disp Lng'] ;  df['Veh/hs'] = df['H_Cant_Veh']

# Create basic choropleth map
fig = px.scatter_mapbox(df, lat=df['Lat'], lon=df['Lon'], color=df['Veh/hs'], size=df['Veh/hs'],
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=10, zoom=12,
                  mapbox_style="carto-positron",   hover_name=df['Disp Nombre'],
                  title='Vehiculos por hora, fecha {dia}/{mes}'.format( mes = 2, dia = 20, hora= 17), animation_frame=df['Hora de H_Fecha'],
                  )
fig.show()
pio.write_html(fig, file='traficflowba.html', auto_open=True) # Guardo y muestro.



