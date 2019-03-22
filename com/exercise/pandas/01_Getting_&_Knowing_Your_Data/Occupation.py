import pandas as pd
import numpy as np

file_path = "/Users/piguanghua/Downloads/u.user"
users = pd.read_csv(file_path, sep = '|')
print(users.index)
#Step 4. See the first 25 entries
print(users.iloc[25:26])
#Step 5. See the last 10 entries
print(users.tail(10))
#Step 6. What is the number of observations in the dataset?
print(users["user_id"].value_counts().count())
#Step 7. What is the number of columns in the dataset?
print(users.columns.values.tolist())
#Step 8. Print the name of all the columns.
pass
#Step 9. How is the dataset indexed?
print(users.index.values.tolist())
#Step 10. What is the data type of each column?
print(users.columns)
#Step 11. Print only the occupation column
print(users["occupation"])
#Step 12. How many different occupations there are in this dataset?
print(users["occupation"].value_counts().count())
print(users.occupation.nunique())
#Step 13. What is the most frequent occupation?
print(users["occupation"].value_counts().head(1))
#Step 14. Summarize the DataFrame.
#Step 15. Summarize all the columns
#Step 16. Summarize only the occupation column


#Step 17. What is the mean age of users?
print(users["age"].mean())
#Step 18. What is the age with least occurrence?
print(type(users["age"].groupby(users["occupation"]).min()))
print(users["age"].groupby(users["occupation"]).min().sort_values() )