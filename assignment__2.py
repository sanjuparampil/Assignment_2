import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

rows = [0,4,9,14,21,41,82,110,120,234,245,252]
columns = [0,1,54,55,56,57,58,59]
#49,50,51,52,53,
#i = ['Africa Western and Central','United Arab Emirates','Australia','Bangladesh','China','United Kingdom','India','Japan','Saudi Arabia','United States']
#Reading data to dataframe and selecting the required rows and columns

df_electricty = pd.read_csv("Electricity.csv",skiprows=lambda x: x not in rows) 
df_electricty = df_electricty.iloc[:, columns] 
df_electricty = df_electricty.set_index('Country Name')
df_electricty.index.name = None
print(df_electricty)

df_access = pd.read_csv("Access_to_electricity.csv",skiprows=lambda x: x not in rows)
df_access = df_access.iloc[:, columns]
df_access = df_access.set_index('Country Name')
# df_access = df_access.drop(columns = df_access.columns[0])
#df_access.reset_index().drop(columns=['  '])
#df_access.drop([0,1,2,3,4,5,6,7,8,9])

df_co2 = pd.read_csv("CO2_emission.csv",skiprows=lambda x: x not in rows)
df_co2 = df_co2. iloc[:, columns]
df_co2 = df_co2.set_index('Country Name')

df_population = pd.read_csv("Population.csv",skiprows=lambda x: x not in rows)
df_population = df_population. iloc[:, columns]
df_population = df_population.set_index('Country Name')

df_energy = pd.read_csv("Energy_consump.csv",skiprows=lambda x: x not in rows)
df_energy = df_energy. iloc[:, columns]
df_energy = df_energy.set_index('Country Name')


#Transposing all the data frames

df_electricity_tr = df_electricty.transpose()
df_access_tr = df_access.transpose()
df_co2_tr = df_co2.transpose()
df_population_tr = df_population.transpose()
df_energy_tr = df_energy.transpose()


#Plotting bar graph
#df_1 = pd.DataFrame({'2006': df_electricty['2006'], 
#                     '2007': df_electricty['2007'],},index = df_electricty.index)
#df_1.plot.bar()
print(df_electricty.columns)

#plt.title("Electricity consumption",size = 40)
x = np.arange(len(df_electricty["Country Code"]))

plt.figure(figsize=(30,17))
#25,17
# year_2005 = plt.bar(x-0.5,df_electricty['2005'],width = 0.10,label='2005',align='edge')
# year_2006 = plt.bar(x-0.4,df_electricty['2006'],width = 0.10,label='2006',align='edge')
# year_2007 = plt.bar(x-0.3,df_electricty['2007'],width = 0.10,label='2007',align='edge')
# year_2008 = plt.bar(x-0.2,df_electricty['2008'],width = 0.10,label='2008',align='edge')
# year_2009 = plt.bar(x-0.1,df_electricty['2009'],width = 0.10,label='2009',align='edge')
# year_2010 = plt.bar(x-0.0,df_electricty['2010'],width = 0.10,label='2010',align='edge')
year_2011 = plt.bar(x-0.2,df_electricty['2011'],width = 0.15,label='2011',align='edge')
year_2012 = plt.bar(x-0.1,df_electricty['2012'],width = 0.15,label='2012',align='edge')
year_2013 = plt.bar(x+0.0,df_electricty['2013'],width = 0.15,label='2013',align='edge')
year_2014 = plt.bar(x+0.1,df_electricty['2014'],width = 0.15,label='2014',align='edge')
year_2015 = plt.bar(x+0.2,df_electricty['2015'],width = 0.15,label='2015',align='edge')

# plt.bar_label(year_2005, padding=3)
# plt.bar_label(year_2006, padding=3)
# plt.bar_label(year_2007, padding=3)
# plt.bar_label(year_2008, padding=3)
# plt.bar_label(year_2009, padding=3)
# plt.bar_label(year_2010, padding=3)
"""plt.bar_label(year_2011, padding=3)
plt.bar_label(year_2012, padding=3)
plt.bar_label(year_2013, padding=3)
plt.bar_label(year_2014, padding=3)
plt.bar_label(year_2015, padding=3)"""
#Plotting bar graphs
# plt.figure()
plt.xlabel("Countries")
plt.ylabel("Years")
plt.legend(fontsize = 25)
plt.title('Electricity production',size = 35)
plt.xticks(x,df_electricty['Country Code'], fontsize=22)#rotation=90)
#plt.savefig('bar1.png', bbox_inches="tight", dpi = 300)
plt.show()

