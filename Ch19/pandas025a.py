import pandas025
df2=pandas025.df1
self_def_key = [0, 1, 2, 3, 3, 4, 5, 7]
print(df2.groupby(self_def_key).size())
print(df2.groupby([df2['key1'], df2['key2']]).size())
grouped1 = df2.groupby('key1')
print(grouped1.mean())
grouped2 = df2['data1'].groupby(df2['key1'])
print(grouped2.mean())