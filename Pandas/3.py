import pandas as pd

# Task 1
df = pd.read_csv('wr88125.txt', sep=';')
df.columns = ['index', 'year', 'month', 'day', 'min_t', 'average_t', 'max_t', 'rainfall']
for column in df.columns[4:]:
    df[column] = pd.to_numeric(df[column], errors='coerce')
print('Task 1:')
print(df)
print()

# Task 2
df.drop('index', axis=1, inplace=True)
print('Task 2:')
print(df)
print()

# Task 3
print('Task 3:')
print(df.info())
print()

# Task 4
row_sums = df.isnull().sum(axis=1)
max_missing_row_index = row_sums.idxmax()
print('Task 4:')
print(df.loc[max_missing_row_index, 'year'])
print()

# Task 5
df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
df.drop(['year', 'month', 'day'], axis=1, inplace=True)
print('Task 5:')
print(df)
print(df['date'].dtype)
print()

# Task 6
lst = []
days_count = 0
for i in df.index:
    days_count = days_count + 1 if i != df.index[0] and df['rainfall'][i - 1] == 0 else 0
    lst.append([df['max_t'][i] - df['min_t'][i], days_count])

df['diff_t'] = [item[0] for item in lst]
df['days_count'] = [item[1] for item in lst]
print('Task 6:')
print(df)
print()

# Task 7
max_drought_period = df[df['days_count'] == df['days_count'].max()]
print('Task 7:')
print(max_drought_period)
print()

# Task 8
lst2 = []
year = df['date'][df.index[0]].year
avg_t = 0
count = 0
rainfall = 0
for i in df.index:
    if df['date'][i].year == year:
        avg_t += df['average_t'][i]
        rainfall += df['rainfall'][i]
        count += 1
    else:
        lst2.append([year, avg_t / count, rainfall])
        avg_t = df['average_t'][i]
        rainfall = df['rainfall'][i]
        year = df['date'][i].year
        count = 1
df8 = pd.DataFrame(lst2, columns=['year', 'avg_t', 'rainfall'])
print('Task 8:')
print(df8)
print()
print('Most warm:')
print(df8[df8['avg_t'] == df8['avg_t'].max()]['year'])
print()
print('Most cold:')
print(df8[df8['avg_t'] == df8['avg_t'].min()]['year'])
print()
print('Most rainy:')
print(df8[df8['rainfall'] == df8['rainfall'].max()]['year'])
print()
print('Most dry:')
print(df8[df8['rainfall'] == df8['rainfall'].min()]['year'])
print()

# Task 9
print('Task 9:')
print(df[df['average_t'] < -30])
print(df[(df['average_t'] > 27) & (df['days_count'] > 3)])
