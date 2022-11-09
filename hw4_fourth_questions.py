
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.
# Follow DRY principles in order to complete this exercise.

import numpy as np
import pandas as pd
import os
path = os.getcwd()

df = pd.read_csv(path + "/covid.csv", sep = ",")
df.head(10)

cases = [500,1000,5000]
country_list = list()
average_list = list()

for c in cases:
    df_filtered = df[df['Active'] > c]
    df_list = list(df_filtered['Country'])
    averages = np.mean(df_filtered['Deaths']), np.mean(df_filtered['Confirmed'])
    country_list.append(df_list)
    average_list.append(averages)

for i in range(len(country_list)):
    print('This is the list of countries with active number of cases greater than '+ str(cases[i]) + ': '
          + str(country_list[i]) + '. The average number of deaths among those countries was '
          +str(average_list[i][0])+' and the average number of confirmed cases among those countries was '
         +str(average_list[i][1])+'.')
