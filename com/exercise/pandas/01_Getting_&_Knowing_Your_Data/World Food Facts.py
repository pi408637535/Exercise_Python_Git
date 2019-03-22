import pandas as pd
import numpy as np

file_path = "/Users/piguanghua/Downloads/en.openfoodfacts.org.products.tsv"
food = pd.read_csv(file_path, sep='\t')
#Step 4. See the first 5 entries
print(food.head(5))
#Step 5. What is the number of observations in the dataset?
print(food.product_name.value_counts().count())
#Step 6. What is the number of columns in the dataset?
#Step 7. Print the name of all the columns.
print(food.columns.values.tolist())
#Step 8. What is the name of 105th column?
print(food.columns.values.tolist()[105])
#Step 9. What is the type of the observations of the 105th column
food.dtypes['-glucose_100g']
#Step 10. How is the dataset indexed?
#print(food.index)
print("---------------------------------")

#Step 11. What is the product name of the 19th observation?
print(food.iloc[19][1])