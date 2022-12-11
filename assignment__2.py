import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def read(doc_name, col):
    """ This function reads files in the world bank data format, sets columns,
    renames columns with new names,returs original and transposed dataframe.
    Rows having null values are dropped."""
    d_frame = pd.read_csv(doc_name, skiprows=lambda x: x not in rows)
    d_frame = d_frame. iloc[:, col]
    d_frame = d_frame.drop(columns={"Country Name", "Country Code"})
    d_frame_tr = d_frame.transpose()
    d_frame_tr = d_frame_tr.rename(columns={0: "AFW", 1: "ARE", 2: "AUS",
                                            3: "BGD",4: "CHN", 5: "GBR",
                                            6: "IND", 7: "JPN", 8: "THA",
                                            9: "TUR", 10: "USA"})
    d_frame_tr = d_frame_tr.dropna()
    return d_frame, d_frame_tr

def read_set_index(doc_name, col):
    """This function reads files in the world bank data format, sets columns,
    sets 'Country Name' as index, returns original dataframe."""
    d_frame = pd.read_csv(doc_name, skiprows=lambda x: x not in rows)
    d_frame = d_frame. iloc[:, col]
    d_frame = d_frame.set_index('Country Name')
    return d_frame

# Selecting the index positions of rows and columns
rows = [0, 4, 9, 14, 21, 41, 82, 110, 120, 234, 245, 252]
columns = [0, 1, 34, 44, 54, 63]
columns_2 = [0, 1, 24, 34, 39, 44, 49]
columns_3 = [0, 1, 24, 34, 39, 44, 49, 54, 59]
columns_4 = [0, 1, 24, 34, 39, 44, 49, 54, 59, 63]

# Reading different CSV files and passing it to variables which then gets
fossil_df, fossil_df_tr = read("Fossil.csv", columns_3)
agriculture_df, agriculture_df_tr = read("Agriculture.csv", columns_2)
no2_df = read_set_index("NO2.csv", columns)
population_df = read_set_index("Population.csv", columns)

# Reading to dataframe,setting the required columns,dropping unwanted columns,
#renaming columns, dropping null values and transposing for all dataframes
df_energy = pd.read_csv("Energy_consump.csv", skiprows=lambda x: x not in rows)
df_energy = df_energy. iloc[:, columns]
df_energy = df_energy.drop(columns={"Country Name", "Country Code"})
df_energy_tr = df_energy.transpose()
df_energy_tr = df_energy_tr.rename(columns={
                                   0: "AFW", 1: "ARE", 2: "AUS", 3: "BGD",
                                   4: "CHN", 5: "GBR", 6: "IND", 7: "JPN", 
                                   8: "THA", 9: "TUR", 10: "USA"})

df_co2 = pd.read_csv("CO2_emission.csv", skiprows=lambda x: x not in rows)
df_co2 = df_co2. iloc[:, columns]
df_co2 = df_co2.drop(columns={"Country Name", "Country Code"})
df_co2_tr = df_co2.transpose()
df_co2_tr = df_co2_tr.rename(columns={0: "AFW", 1: "ARE", 2: "AUS", 3: "BGD",
                             4: "CHN", 5: "GBR", 6: "IND", 7: "JPN", 8: "THA",
                             9: "TUR", 10: "USA"})

# variables declared to set the position of xticks for bar graphs
x = np.arange(len(population_df["Country Code"]))
a = np.arange(len(no2_df["Country Code"]))

# Plotting Bar graphs
def bar_population(y):
    """ This function plots bar graph for countries(x-axis)
    vs Population(y-axis).Visualization method used 
    is BAR GRAPH"""
    plt.figure(figsize=(30, 17))
    plt.bar(x-0.2, y['1990'], width=0.15, label='1990', align='edge')
    plt.bar(x-0.1, y['2000'], width=0.15, label='2000', align='edge')
    plt.bar(x+0.0, y['2010'], width=0.15, label='2010', align='edge')
    plt.bar(x+0.1, y['2019'], width=0.15, label='2019', align='edge')
    plt.xlabel("Countries", fontsize=25)
    plt.legend(fontsize=25)
    plt.title('Total Population', size=35)
    plt.xticks(x, population_df['Country Code'], fontsize=22)  # rotation=90)
    plt.savefig('population.png', bbox_inches="tight", dpi=300)
    plt.show()

def bar_no2(z):
    """ This function plots bar graph for countries(x-axis)
    vs Nitrous Oxide emissions(y-axis).Visualization method used 
    is BAR GRAPH"""
    plt.figure(figsize=(30, 17))
    plt.bar(a-0.2, z['1990'], width=0.15, label='1990', align='edge')
    plt.bar(a-0.1, z['2000'], width=0.15, label='2000', align='edge')
    plt.bar(a-0.0, z['2010'], width=0.15, label='2010', align='edge')
    plt.bar(a+0.1, z['2019'], width=0.15, label='2019', align='edge')
    plt.xlabel("Countries", fontsize=25)
    plt.legend(fontsize=25)
    plt.title('Nitrous Oxide Emissions (1000 metric tons of CO2)', size=35)
    plt.xticks(x, no2_df['Country Code'], fontsize=22)  # rotation=90)
    plt.savefig('NO2.png', bbox_inches="tight", dpi=300)
    plt.show()

# Plotting the line graphs
def line_agriculture(v):
    """ This function plots line graph for years(x-axis)
    vs Agriculture land area(y-axis).Visualization method used 
    is LINE GRAPH"""
    plt.figure(figsize=(35, 20))
    plt.plot(v.index, agriculture_df_tr['AFW'], '--', label="AFW")
    plt.plot(v.index, agriculture_df_tr['ARE'], '--', label="ARE")
    plt.plot(v.index, agriculture_df_tr['AUS'], '--', label="AUS")
    plt.plot(v.index, agriculture_df_tr['BGD'], '--', label="BGD")
    plt.plot(v.index, agriculture_df_tr['CHN'], '--', label="CHN")
    plt.plot(v.index, agriculture_df_tr['GBR'], '--', label="GBR")
    plt.plot(v.index, agriculture_df_tr['IND'], '--', label="IND")
    plt.plot(v.index, agriculture_df_tr['JPN'], '--', label="JPN")
    plt.plot(v.index, agriculture_df_tr['THA'], '--', label="THA")
    plt.plot(v.index, agriculture_df_tr['TUR'], '--', label="TUR")
    plt.plot(v.index, agriculture_df_tr['USA'], '--', label="USA")
    plt.xlabel("Years", fontsize=30)
    plt.legend(fontsize=25)
    plt.title('Agricultural land', size=30)
    # plt.xticks(x,df_agriculture_tr['Country Code'], fontsize=22)#rotation=90)
    plt.xticks(fontsize=25)
    plt.savefig('agroculture.png', bbox_inches="tight", dpi=300)
    plt.show()

def line_fossil(u):
    """ This function plots line graph for years(x-axis)
    vs Percentage of fossile consumption(y-axis).Visualization method used 
    is LINE GRAPH"""
    plt.figure(figsize=(35, 20))
    plt.plot(u.index, fossil_df_tr['AFW'], '--', label="AFW")
    plt.plot(u.index, fossil_df_tr['ARE'], '--', label="ARE")
    plt.plot(u.index, fossil_df_tr['AUS'], '--', label="AUS")
    plt.plot(u.index, fossil_df_tr['BGD'], '--', label="BGD")
    plt.plot(u.index, fossil_df_tr['CHN'], '--', label="CHN")
    plt.plot(u.index, fossil_df_tr['GBR'], '--', label="GBR")
    plt.plot(u.index, fossil_df_tr['IND'], '--', label="IND")
    plt.plot(u.index, fossil_df_tr['JPN'], '--', label="JPN")
    plt.plot(u.index, fossil_df_tr['THA'], '--', label="THA")
    plt.plot(u.index, fossil_df_tr['TUR'], '--', label="TUR")
    plt.plot(u.index, fossil_df_tr['USA'], '-', label="USA")
    plt.xlabel("Years", fontsize=30)
    plt.legend(fontsize=25)
    plt.title('Fossil Fuel Energy Consumption', size=30)
    plt.xticks(fontsize=25)
    plt.savefig('fossil.png', bbox_inches="tight", dpi=300)
    plt.show()

# Finding mean Energy consumption from 1990-2019
df_energy_tr = df_energy_tr[["AFW", "ARE", "AUS", "BGD",
                             "CHN", "GBR", "IND", "JPN",
                             "THA", "TUR", "USA"]].mean()
# FInding mean CO2 production from 1990-2019
df_co2_tr = df_co2_tr[["AFW", "ARE", "AUS", "BGD", "CHN",
                       "GBR", "IND", "JPN", "THA", "TUR", "USA"]].mean()
# Calling function line_fossil()
line_fossil(fossil_df_tr)
# Calling the line_agriculture function
line_agriculture(agriculture_df_tr)
# Calling the bar_no2 function
bar_no2(no2_df)
# Calling the bar_population function
bar_population(population_df)


