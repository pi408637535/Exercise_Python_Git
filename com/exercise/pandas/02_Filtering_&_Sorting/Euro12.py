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
euro12[["Team", "Yellow Cards", "Red Cards"]]
print(discipline)
#Step 8. Sort the teams by Red Cards, then to Yellow Cards
euro12.sort_values(by=["Red Cards", "Yellow Cards"])
print(euro12.head(1))
#Step 9. Calculate the mean Yellow Cards given per Team
print(euro12["Yellow Cards"].groupby(euro12["Team"]).mean())
#Step 10. Filter teams that scored more than 6 goals
print(euro12[ euro12["Goals"] > 6 ])
#Step 11. Select the teams that start with G
print(euro12[ euro12["Team"].str.startswith('G')])
#Step 12. Select the first 7 columns
euro12.head(7)
print(euro12.iloc[0:7])

#Step 13. Select all columns except the last 3.
euro12.iloc[:-3]
#Step 14. Present only the Shooting Accuracy from England, Italy and Russia

print(euro12[ euro12["Team"].isin(["England", "Italy", "Russia"]) ][['Team','Shooting Accuracy']])