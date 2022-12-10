import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rows = [0,4,9,14,21,41,82,110,120,234,245,252]
columns = [0,1,34,44,54,63]

df_population = pd.read_csv("Population.csv",skiprows=lambda x: x not in rows)
df_population = df_population. iloc[:, columns]
df_population = df_population.set_index('Country Name')

df_agriculture = pd.read_csv("Agriculture.csv",skiprows=lambda x: x not in rows)
df_agriculture = df_agriculture. iloc[:, columns]
df_agriculture = df_agriculture.drop(columns={"Country Name","Country Code"})

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

#Reading data to dataframe and selecting the required rows and columns
df_fossil = pd.read_csv("Fossil.csv",skiprows=lambda x: x not in rows)
df_fossil = df_fossil. iloc[:, columns]

#Removing country names and country codes
df_fossil = df_fossil.drop(columns={"Country Name","Country Code"})

#Transposing the dataframe and renaming columns
df_fossil_tr = df_fossil.transpose()
df_fossil_tr = df_fossil_tr.rename(columns={0:"AFW",1:"ARE",2:"AUS",3:"BGD",4:"CHN",5:"GBR",6:"IND",7:"JPN",8:"THA",9:"TUR",10:"USA"})

#Removing null values 
df_fossil_tr = df_fossil_tr.dropna()
print(df_fossil_tr)

#Plotting the line graph

def line_fossil(u):
    """ This function plots line graph for years(x-axis)
    vs Percentage of fossile consumption(y-axis).Visualization method used 
    is LINE GRAPH"""
    plt.figure(figsize=(35,20))
    plt.plot(u.index, df_fossil_tr['AFW'],'--',label = "AFW")
    plt.plot(u.index, df_fossil_tr['ARE'],'--',label = "ARE")
    plt.plot(u.index, df_fossil_tr['AUS'],'--',label = "AUS")
    plt.plot(u.index, df_fossil_tr['BGD'],'--',label = "BGD")
    plt.plot(u.index, df_fossil_tr['CHN'],'--',label = "CHN")
    plt.plot(u.index, df_fossil_tr['GBR'],'--',label = "GBR")
    plt.plot(u.index, df_fossil_tr['IND'],'--',label = "IND")
    plt.plot(u.index, df_fossil_tr['JPN'],'--',label = "JPN")
    plt.plot(u.index, df_fossil_tr['THA'],'--',label = "THA")
    plt.plot(u.index, df_fossil_tr['TUR'],'--',label = "TUR")
    plt.plot(u.index, df_fossil_tr['USA'],'-',label = "USA")
    plt.xlabel("Years",fontsize = 30)
    plt.legend(fontsize = 25)
    plt.title('Fossil Fuel Energy Consumption',size = 30)
    plt.xticks(fontsize=25)

    #plt.xticks(df_agriculture_tr['Country Code'], fontsize=22)#rotation=90)
    plt.savefig('fossil.png', bbox_inches="tight", dpi = 300)
    plt.show()


    
#Calling function line_fossil()
line_fossil(df_fossil_tr)

#Transposing the dataframe
df_agriculture_tr = df_agriculture.transpose()
df_agriculture_tr=df_agriculture_tr.rename(columns={0:"AFW",1:"ARE",2:"AUS",3:"BGD",4:"CHN",5:"GBR",6:"IND",7:"JPN",8:"THA",9:"TUR",10:"USA"})

print(df_agriculture_tr)
#Plotting the line graph

def line_agriculture(v):
    """ This function plots line graph for years(x-axis)
    vs Agriculture land area(y-axis).Visualization method used 
    is LINE GRAPH"""
    
    plt.figure(figsize=(35,20))
    plt.plot(v.index, df_agriculture_tr['AFW'],'--',label = "AFW")
    plt.plot(v.index, df_agriculture_tr['ARE'],'--',label = "ARE")
    plt.plot(v.index, df_agriculture_tr['AUS'],'--',label = "AUS")
    plt.plot(v.index, df_agriculture_tr['BGD'],'--',label = "BGD")
    plt.plot(v.index, df_agriculture_tr['CHN'],'--',label = "CHN")
    plt.plot(v.index, df_agriculture_tr['GBR'],'--',label = "GBR")
    plt.plot(v.index, df_agriculture_tr['IND'],'--',label = "IND")
    plt.plot(v.index, df_agriculture_tr['JPN'],'--',label = "JPN")
    plt.plot(v.index, df_agriculture_tr['THA'],'--',label = "THA")
    plt.plot(v.index, df_agriculture_tr['TUR'],'--',label = "TUR")
    plt.plot(v.index, df_agriculture_tr['USA'],'--',label = "USA")
    plt.xlabel("Years",fontsize = 30)
    plt.legend(fontsize = 25)
    plt.title('Agricultural land',size = 30)
    #plt.xticks(x,df_agriculture_tr['Country Code'], fontsize=22)#rotation=90)
    plt.xticks(fontsize=25)
    plt.savefig('agroculture.png', bbox_inches="tight", dpi = 300)
    plt.show()

    
line_agriculture(df_agriculture_tr)
#Calling the bar_no2 function    
bar_no2(df_no2)
    
bar_population(df_population)


