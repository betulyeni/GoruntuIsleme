import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from mpl_toolkits.basemap import Basemap
import datetime
import time

data = pd.read_csv("Deprem Verisi Ege Bölgesi.csv")
def harita():
    data1 = data[['Enlem', 'Boylam']]
    m = Basemap(width=1200000,height=900000,projection='lcc',
            resolution='l',lat_1=26.,lat_2=85,lat_0=39,lon_0=30.)

    longitudes = data1["Boylam"].tolist()
    latitudes = data1["Enlem"].tolist()
    x,y = m(longitudes,latitudes)
    fig = plt.figure(figsize=(60,60))
    plt.title("EGE BÖLGESİNDE DAHA ÖNCE OLAN DEPREMLER")
    m.plot(x, y, "o", markersize = 2, color = 'blue')
    m.drawcoastlines()
    m.fillcontinents(color='coral',lake_color='aqua')
    m.drawmapboundary()
    m.drawcountries()
