# This script extract a python list from a data frame column in a CSV file
# In other words in helps dealing from Python to R

import pandas as pd
df = pd.read_csv('/Users/Ofix/Documents/Fac/internat/Recherche/projets/synchro/synchroData/Monrado/Data/CSV/FilesName.csv')
saved_column = df.indexList #you can also use df['column_name']
print(saved_column.tolist())
