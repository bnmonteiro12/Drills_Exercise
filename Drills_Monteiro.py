import pandas as pd
import numpy as np
import random as random
df = pd.read_csv("table1.csv")
#df.insert(0, "id", range(1,1+len(df)))
#df.iloc[:,1] = 'META-' + df.iloc[:,1].astype(str)
#df.insert(2, "Random", [random.randint(0,1) for i in range(0,len(df))])
tdf = df.T
print(tdf.head())
print(df)

df.to_csv("table1.csv",index=False)