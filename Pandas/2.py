import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
        ["Гайка", "Gadget Hackwrench", "mouse", None],
        ["Дейл", "Dale", "chipmunk", "1"],
        ["Рокфор", "Monterey Jack", "mouse", "0.8"],
        ["Чип", "Chip", "chipmunk", "0.2"]]

df = pd.DataFrame(data, columns=["ru_name", "en_name", "class", "cheer"])
df["cheer"] = pd.to_numeric(df["cheer"], errors="coerce").astype(float)

# Task 1
print("# Task 1:")
print(df, "\n")

# Task 2
num_rows = len(df)
print("# Task 2:")
print(num_rows, "\n")

# Task 3
num_filled_cells = df["cheer"].count()
print("# Task 3:")
print(num_filled_cells, "\n")

# Task 4
cell_value = df.at[2, "en_name"]
print("# Task 4:")
print(cell_value, "\n")

# Task 5
df1 = df.iloc[1:4, 0:3]
print("# Task 5:")
print(df1, "\n")

# Task 6
df.columns = ["ru_name", "en_name", "class", "cheer"]
print("# Task 6:")
print(df, "\n")

# Task 7
df["logcheer"] = np.log(df["cheer"])
print("# Task 7:")
print(df, "\n")

# Task 8
x = df["class"].unique()
y = df["class"].value_counts(sort=False)

plt.bar(x, y)
plt.title("Class Distribution")
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.show()
