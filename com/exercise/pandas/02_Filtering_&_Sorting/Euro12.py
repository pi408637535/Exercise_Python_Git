import pandas as pd
import numpy as np

file_path = "/Users/piguanghua/Downloads/Euro_2012_stats_TEAM.csv"
euro12 = pd.read_csv(file_path, sep = ',')
print(euro12.head(1))
#Step 4. Select only the Goal column.
print(euro12["Goals"])
#Step 5. How many team participated in the Euro2012?
print(euro12["Team"].value_counts().count())
#Step 6. What is the number of columns in the dataset?
