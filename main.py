import pandas as pd
import matplotlib.pyplot as plt  

# Create a dictionary with daily calorie intake
calories = {
    "day1": 1780,
    "day2": 1986,
    "day3": 2200,
    "day4": 1800,
    "day5": 1650,
    "day6": 2360,
    "day7": 1450
}

# Convert dictionary into a Pandas Series
# Keys become index labels
# Values become the data
series = pd.Series(calories)

# Access day4 using label-based indexing (.loc)
# Increase its value by 450 calories
series.loc["day4"] += 450

# Print entire Series
print("Full Series:\n", series)

# Access specific value using label (.loc)
print("\nCalories on day4:", series.loc["day4"])

# Access using position-based indexing (.iloc)
# iloc[1] means second position (index 1)
print("\nSecond day using iloc:", series.iloc[1])

# Boolean filtering: show days with calories >= 2000
print("\nDays >= 2000 calories:\n", series[series >= 2000])

# Boolean filtering: show days with calories <= 2000
print("\nDays <= 2000 calories:\n", series[series <= 2000])



# DataFrame => Tabular structures with rows and columns (2D)
data = {"Name": ["Stacy", "Glenn", "Moris", "Juliet", "Collins"],
        "Age": [19, 32, 28, 25, 21]
        }
df = pd.DataFrame(data, index=["player1", "player2", "player3", "player4", "player5"])

#Adding a new column
df["Position"] = ["striker", "goalie", "midfielder", "defender", "winger"]

#Adding a new row

new_row = pd.DataFrame([{"Name": "Henry", "Age": 23, "Position": "Striker"}], index=["player6"])

df = pd.concat([df, new_row])

print(df)

print(df.loc["player3"])  #=> location by label
print(df.iloc[[3, 4]])