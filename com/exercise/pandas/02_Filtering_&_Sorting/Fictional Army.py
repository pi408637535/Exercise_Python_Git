
import pandas as pd
import numpy as np


raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

#### Step 3. Create a dataframe and assign it to a variable called army.
army = pd.DataFrame(data=raw_data, columns=["regiment","company","deaths","battles",
                                            "size", "veterans", "readiness","armored",
                                            "deserters","origin"])

#print(army.head(1))

#Step 4. Set the 'origin' colum as the index of the dataframe
'''
army = army.set_index('origin')
print(army)
'''
army.index = army["origin"]
army = army.drop(labels=["origin"], axis=1)
print(army)

### Step 5. Print only the column veterans
print(army["veterans"])
#Step 6. Print the columns 'veterans' and 'deaths'
print(army[["veterans","deaths"]])
#Step 7. Print the name of all the columns.
print(army.columns)
# Step 8. Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
print(army.loc[["Maine","Alaska"]][["deaths","size", "deserters"]])
#Step 9. Select the rows 3 to 7 and the columns 3 to 6
print(army.iloc[3:8]) #?如何进行列切片
army.iloc[3:7, 3:6]
#Step 10. Select every row after the fourth row
print(army[4:])
#Step 11. Select every row up to the 4th row
#读不懂
army.iloc[:4]
#Step 12. Select the 3rd column up to the 7th column
army.iloc[:,3:7]
#列切片不会
#Step 13. Select rows where df.deaths is greater than 50
print(army[army["deaths"] > 50])
#Step 14. Select rows where df.deaths is greater than 500 or less than 50
print(army[ (army["deaths"] > 500) | (army["deaths"] < 50) ] )
#Step 15. Select all the regiments not named "Dragoons"
# 不会 army["regiment"].str.match("Dragoons")
army[(army['regiment'] != 'Dragoons')]
#Step 16. Select the rows called Texas and Arizona
print(army.loc[["Texas","Arizona"]])
#Step 17. Select the third cell in the row named
#不会
army.loc[["Arizona"],["company","deaths"]]
#Step 18. Select the third cell down in the column named deaths
army["deaths"][3]