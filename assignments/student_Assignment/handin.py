#   The Datasheet used for this assignment can be downloaded from the following site -> https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies
from os import sep
from unittest import result
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#   Taks 1. Find the top 10 highest grossing Disney movies measured by world sales.
print('\n----------   Task 1  ---------- \n \n Top 10 Disney movies World Sales in Dollars \n')

#   First Thought! -> We can find all disney movies by searching on the Distributor. Then we can filter once agian on the World Sales (in $) collum. 
data = pd.read_csv('./Highest Holywood Grossing Movies.csv', skiprows=0)                                #   Importing the csv file and saving it's data to our data variable.
disney_mov = data[(data['Distributor']=='Walt Disney Studios Motion Pictures')]                         #   Creating a dataframe based on Walt Diseney movies.
disney_mov.loc[:,('World Sales (in $)')].astype('int')                                                  #   Converting world sales to int and excluding all other info from the csv file.
print(disney_mov.sort_values('World Sales (in $)', ascending=False).head(10)[['World Sales (in $)']])   #   Sorts the values based on decending order so that the highest grossing comes first and then we only take top 10.

#   Task 2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on).
print('\n----------   Task 2  ---------- \n \n A pie chart of which licenses is used by the Highest Holywood Grossing Movies \n Pie chart can be viewed at .\License_Chart_Task2.png')
#   First Thought! -> We need to create a PandaSeries that only contains License data and count that data togheter and then make a pie chart on out of that Series.
#ds_license = pd.Series(data['License'])                                                                 #   Creating a Pd.Series from our csv data only taking license data and saving it to a variable.
#ds_license_count = ds_license.value_counts()                                                            #   Here we count / Sum up that data and saves it to another variable.
#ds_license_count.plot(kind='pie', autopct='%1.0f%%')                                                    #   Now we can make our pie chart of license data, based on those summed values.

#   Taks 3. Get the percentage of PG rated movies between 2001 and 2015
print('\n----------   Task 3  ---------- \n \n Percent of PG rated movies between 2001 and 2015 \n')

#   First Thought! -> Here we need to get license and release date into a dataframe then we have to split month and date away from year so we can filter based on those specific year range, after that we need to calculate the percentage.
df1 = pd.DataFrame(data, columns = ['License','Release Date'])                                          #   Creating our dataFrame and selecting the only two collums we need.
df1[['Release Date', 'Year']] = df1['Release Date'].str.split(',', 1, expand=True)                      #   Here we strip month and date from year on the comma.
df1_filter = df1[(df1['Year'] >= ' 2001') & (df1['Year'] < ' 2015')]                                    #   Sorts our dataframe to only include data in a specific year range.
df1 = df1_filter['License'].value_counts(normalize=True).mul(100).round(1).astype(str) + '%'            #   Counts all the different licenses and convert that into percentage.
print('PG = ' + df1.iloc[1])                                                                            #   Here we print the result and make sure we only print PG percentage.

#   Taks 4. Calculate the average of world sales for each genre and visualize the data with a bar chart.
print('\n----------   Task 4  ---------- \n \n testing \n')

#   First Thought! -> 
result = {}
df2 = pd.DataFrame(data, columns = ['World Sales (in $)', 'Genre'])
df3 = (df2['Genre'].str.split("'", expand=True)
                         .replace(',', '')
                         .apply(pd.value_counts, axis=1)
                         .fillna(0)  
                         .astype(int))

y = df3[df3.columns[1:22]].copy()
y1 = y.sum().to_dict()
z = y.mul(df2["World Sales (in $)"], axis=0)
x = z.sum().to_dict()
for (i, v), (i2, v2) in zip(
    y1.items(), x.items()
    ):
    avg = v2 / v
    result[i] = avg

print(result)