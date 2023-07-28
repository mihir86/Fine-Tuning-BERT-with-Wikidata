import csv
import pandas as pd
import numpy as np

df = pd.read_csv("query.csv")
print(df)

d1=[]
d2=[]
d3=[]

for i in range(3485):
    sp = 0
    for j in range(len(df['itemLabel'][i])):
        if df['itemLabel'][i][j] == ' ':
            sp = sp+1
    if sp==0:
        d1.append([df['item'][i],df['itemLabel'][i]])
    elif sp==1:
        d2.append([df['item'][i],df['itemLabel'][i]])
    else:
        d3.append([df['item'][i],df['itemLabel'][i]])

df1 = pd.DataFrame(d1, columns = ['item', 'itemLabel'])
df2 = pd.DataFrame(d2, columns = ['item', 'itemLabel'])
df3 = pd.DataFrame(d3, columns = ['item', 'itemLabel'])

print(df1)
print(df2)
print(df3)

df1.to_csv("List_1.csv")
df2.to_csv("List_2.csv")
df3.to_csv("List_3.csv")
