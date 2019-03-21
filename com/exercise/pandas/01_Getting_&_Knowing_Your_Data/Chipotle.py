import pandas as pd
import numpy as np

file_path = "/Users/piguanghua/Downloads/chipotle.tsv"
chipo = pd.read_csv(file_path, sep = '\t')
print(chipo.head(10))
print(chipo.size)
print(chipo.shape)
print(chipo.columns.values.tolist())  #获取列名
print(chipo.index.values.tolist())

print("被下单数最多商品")
print(chipo['quantity'].idxmax())  #某列最大值所在的行
print(chipo.iloc[chipo['quantity'].idxmax()])
print("------------------------")
c = chipo[['item_name','quantity']].groupby(['item_name'],as_index=False).agg({'quantity':sum})
c.sort_values(['quantity'],ascending=False,inplace=True)
print(c.head())

print("------------------------")

#自己完成
sum_max = chipo["quantity"].groupby(chipo["item_name"]).sum()

print(sum_max.sort_values(ascending=False).head())

print("被下单数最多商品 end")
print("----------------------------------------------------")

print(chipo['item_name'].unique().size) #Step 12

#Turn the item price into a float
dollarizer = lambda x: float(x[1:-1])
chipo["item_price"] = chipo["item_price"].apply(dollarizer)

print(chipo['item_price'].dtypes) #Step 13 ?

chipo[["item_price"]] = chipo[["item_price"]].astype(np.str)
print(chipo['item_price'].dtypes)
print("------------------------")
print( (chipo['item_price'] * chipo['quantity']).sum() )

print("Step 14 end")

#Step 15. How many orders were made in the period?
print(chipo['order_id'].value_counts().count())
print("Step 15 End")

#Step 16. What is the average revenue amount per order?
chipo["revenue"] = chipo['item_price'] * chipo['quantity']



chipo['revenue'] = chipo['quantity'] * chipo['item_price']
dollarizer = lambda x: float(x[0:4])
chipo['revenue'] = chipo['revenue'].apply(dollarizer)
print(chipo["revenue"].groupby(chipo["order_id"]).mean())
print("Step 16 End")

#Step 17. How many different items are sold?
print(chipo['item_name'].value_counts().count())
