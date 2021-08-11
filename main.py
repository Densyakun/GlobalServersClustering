import pandas as pd

MAX_PING = 5

df = pd.read_csv('pings.csv', usecols=[0, 1, 4], na_values=-1.).dropna(subset=['avg'])
l = max(df['source'].max(), df['destination'].max())

a = df[df['avg'] <= MAX_PING]
list = []
for i in range(1):
    b = a['source'] == i
    c = a['destination'] == i
    print(a[b | c])
    if len(a[b]) == 0 and len(a[c]) == 0:
        list.append([0, i, []])
    else:
        list.append([a[b | c]['avg'].sum(), i, []])
