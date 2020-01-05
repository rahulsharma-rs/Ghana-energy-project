import os
import glob
import pandas as pd

path='data/year*.pkl'

flist=glob.glob(pathname=path)
lst1=[]
lst=[]
for d in flist:
    df=pd.read_pickle(d)
    lst1.append(df.columns.tolist())
    lst.append(df)
clolist=['Actual Load','Available Generation','Forecast Load','Hour','Hour1','Managed Forecast Load','datetime']

data=pd.concat(lst)
data.index=data.datetime
data.sort_index(inplace=True)
data.to_pickle("./data/data2010to2019.pkl")
print("x")