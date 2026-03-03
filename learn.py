import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_json("/home/sam/Downloads/pd-project_small.json")

print(df.to_string)
print(df["Date"])