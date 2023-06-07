import pandas as pd

# Task 1
series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print("# Task 1:")
print(series, "\n")

# Task 2
value = series['d']
print("# Task 2:", value, "\n")

# Task 3
value = series[1]
print("# Task 3:", value, "\n")

# Task 4
series['f'] = 6
print("# Task 4:")
print(series, "\n")

# Task 5
series_slice = series['c':'e']
print("# Task 5:")
print(series_slice, "\n")

# Task 6
marks = {'col1': [1, 5, 3.7], 'col2': [2, 3, 4.8]}
df = pd.DataFrame(marks, columns=['col1', 'col2'])
print("# Task 6:")
print(df, "\n")

# Task 7
value = df.at[2, 'col1']
print("# Task 7:", value, "\n")

# Task 8
df.at[1, 'col2'] = 9
print("# Task 8:")
print(df, "\n")

# Task 9
subset = df.iloc[1:3]
print("# Task 9:")
print(subset, "\n")

# Task 10
df['col3'] = df['col1'] * df['col2']
print("# Task 10:")
print(df, "\n")
