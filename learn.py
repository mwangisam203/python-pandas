import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("/home/sam/Downloads/pd-big-project.csv", index_col="Order_ID")

#print(df.to_string())

#Selection by Column
print(df.index.is_unique)                 # False means duplicates exist
print((df.index == "Helen Smith").sum())  # how many times she appears
print(df.loc[990:1000, ["Customer_Name", "Product", "Quantity"]])


# #Selection By Rows
print(df.iloc[0:10, 2:6]) #Selection from rows indicated and then specific columns eg from index 3 to 6

#Accessing certain index or characters via search method
df = pd.read_csv("/home/sam/Downloads/pd-big-project.csv", index_col="Customer_Name")

Customer_Name = input("Enter customer's name: ")

try: # Try to retrieve the row that matches the customer name
    # .loc is used for label-based indexing

    print(df.loc[Customer_Name])

except KeyError:
    print(f"{Customer_Name} not in the list provided") # => type the name, if it exist, information regarding that name will be displayed, if not found, it will print an error msg




#MORE COMPLEX THAT FILTERS NAME CHARS, CAN INPUT FEW CHARS AND STILL FIND YOUR RESULTS
df = pd.read_csv("/home/sam/Downloads/pd-big-project.csv", index_col="Customer_Name")

name = input("Enter name: ")

try:
    result = df[df.index.str.contains(name, case=False)]

    if result.empty:
        raise ValueError("Name not found")

    print(result)

except Exception as e:
    print("Error:", e)

    #NB On the above code block with filters does the following
# Ask the user to enter a name to search in the DataFrame index
# The try block attempts to find rows where the index contains the entered text
# df.index.str.contains() allows partial name matching and case-insensitive search
# If no rows are found, a ValueError is raised to indicate "Name not found"
# If matches exist, only the Product and Quantity columns are displayed
# The except block catches any error (e.g., no match found) and prints a friendly message