import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rows = [0,4,9,14,21,41,82,110,120,234,245,252]
#columns = [0,1,54,55,56,57,58,59]
columns = [0,1,34,44,54,63]
#49,50,51,52,53,
#i = ['Africa Western and Central','United Arab Emirates','Australia','Bangladesh','China','United Kingdom','India','Japan','Saudi Arabia','United States']

df_population = pd.read_csv("Population.csv",skiprows=lambda x: x not in rows)
df_population = df_population. iloc[:, columns]
df_population = df_population.set_index('Country Name')

print(df_population)

#plt.title("Electricity consumption",size = 40)
x = np.arange(len(df_population["Country Code"]))


def bar_population(y):
    """ This function plots bar graph for countries(x-axis)
    vs Population(y-axis).Visualization method used 
    is BAR GRAPH"""
    
    plt.figure(figsize=(30,17))
    plt.bar(x-0.2,y['1990'],width = 0.15,label='1990',align='edge')
    plt.bar(x-0.1,y['2000'],width = 0.15,label='2000',align='edge')
    plt.bar(x+0.0,y['2010'],width = 0.15,label='2010',align='edge')
    plt.bar(x+0.1,y['2019'],width = 0.15,label='2019',align='edge')
    plt.xlabel("Countries", fontsize = 25)
    plt.ylabel("Population", fontsize = 25)
    plt.legend(fontsize = 25)
    plt.title('Total Population',size = 35)
    plt.xticks(x,y['Country Code'], fontsize=22)#rotation=90)
    #plt.savefig('bar1.png', bbox_inches="tight", dpi = 300)
    plt.show()
  
#Reading to dataframe and setting the required columns
df_no2 = pd.read_csv("NO2.csv",skiprows=lambda x: x not in rows)
df_no2 = df_no2. iloc[:, columns]

#Set Index
df_no2 = df_no2.set_index('Country Name')


x = np.arange(len(df_no2["Country Code"]))
def bar_no2(z):
    """ This function plots bar graph for countries(x-axis)
    vs Nitrous Oxide emissions(y-axis).Visualization method used 
    is BAR GRAPH"""

    plt.figure(figsize=(30,17))
    plt.bar(x-0.2,z['1990'],width = 0.15,label='1990',align='edge')
    plt.bar(x-0.1,z['2000'],width = 0.15,label='2000',align='edge')
    plt.bar(x-0.0,z['2010'],width = 0.15,label='2010',align='edge')
    plt.bar(x+0.1,z['2019'],width = 0.15,label='2019',align='edge')
    plt.xlabel("Countries",fontsize=25)
    plt.ylabel("NO2 Emissions",fontsize=25)
    plt.legend(fontsize = 25)
    plt.title('Nitrous Oxide Emissions',size = 35)
    plt.xticks(x,df_no2['Country Code'], fontsize=22)#rotation=90)
    #plt.savefig('bar1.png', bbox_inches="tight", dpi = 300)
    plt.show()
    
#Calling the bar_no2 function    
bar_no2(df_no2)
    
bar_population(df_population)


