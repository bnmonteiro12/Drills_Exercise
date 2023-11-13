import pandas as pd
import numpy as np
df = pd.read_csv("table1.csv")
#df.insert(0, "id", range(1,1+len(df)))
df.iloc[:,1] = 'META-' + df.iloc[:,1].astype(str)
print(df)

df.to_csv("table1.csv",index=False)
