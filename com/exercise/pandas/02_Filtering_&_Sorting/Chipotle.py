import pandas as pd
import numpy as np

file_path = "/Users/piguanghua/Downloads/chipotle.tsv"
chipo = pd.read_csv(file_path, sep = '\t')
#Step 4. How many products cost more than $10.00?
print(chipo.head(1))
dollarizer = lambda x: float(x[1:-1])
chipo["item_price"] = chipo["item_price"].apply(dollarizer)
print( chipo[chipo["item_price"] > 10].head() )

#Error
chipo_drop_duplicated = chipo.drop_duplicates(["quantity","item_name"])
chipo_filter = chipo_drop_duplicated["quantity"] == 1
chipo_filter = chipo_drop_duplicated[chipo_filter]
print(chipo_filter[chipo_filter["item_price"] > 10]["item_name"].nunique())


#Step 5. What is the price of each item?
chipo_drop_duplicated = chipo.drop_duplicates(["quantity","item_name"])
chipo_filter = chipo_drop_duplicated["quantity"] == 1
chipo_filter = chipo_drop_duplicated[chipo_filter]
chipo_one_prod = chipo_drop_duplicated[["item_name","item_price"]]

#Step 6. Sort by the name of the item
print("---------------------------------------")
chipo_remove_duplicated = chipo.drop_duplicates("item_name")
chipo_remove_duplicated.sort_values(by="item_name")
print( chipo_remove_duplicated["item_name"].head())

#Step 7. What was the quantity of the most expensive item ordered?
print("---------------------------------------")
print(chipo["quantity"].groupby(chipo["order_id"]).max().sort_values(ascending=False).head())

#Step 8. How many times were a Veggie Salad Bowl ordered?
print("---------------------------------------")
print(chipo["item_name"].value_counts()["Veggie Salad Bowl"])

#Step 9. How many times people orderd more than one Canned Soda?
chipo_filter = chipo[ (chipo["item_name"] == "Canned Soda") & ( chipo["quantity"]  > 1)]
print(len(chipo_filter))

