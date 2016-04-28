# This script extract a python list from a data frame column in a CSV file
# In other words in helps dealing from Python to R

import pandas as pd
df = pd.read_csv('/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/Git/INCANT/Data/CSV/studyInfoData/indexList.slideddata.csv')
saved_column = df.x #you can also use df['column_name']
print(saved_column.tolist())
