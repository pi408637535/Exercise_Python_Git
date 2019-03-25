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
print(euro12.shape[0])
# Step 7. View only the columns Team, Yellow Cards and Red Cards and assign them to a dataframe called discipline
discipline = euro12["Team"]
discipline = euro12["Yellow Cards"]
discipline = euro12["Red Cards"]
print(discipline)
#Step 8. Sort the teams by Red Cards, then to Yellow Cards
euro12.sort_values(by=["Red Cards", "Yellow Cards"])  #?用法对吗
print(euro12.head(1))
#Step 9. Calculate the mean Yellow Cards given per Team
print(euro12["Yellow Cards"].groupby(euro12["Team"]).mean())
#Step 10. Filter teams that scored more than 6 goals


