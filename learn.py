import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("/home/sam/Downloads/pd-big-project.csv", index_col="Order_ID")

print(df.to_string())

#Selection by Column
# print(df.index.is_unique)                 # False means duplicates exist
# print((df.index == "Helen Smith").sum())  # how many times she appears
# print(df.loc[990:1000, ["Customer_Name", "Product", "Quantity"]])


# #Selection By Rows
print(df.iloc[0:10, 2:6]) #Selection from rows indicated and then specific columns eg from index 3 to 6