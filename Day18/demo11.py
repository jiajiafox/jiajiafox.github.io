import pandas as pd
import numpy as np
df=pd.DataFrame([('name','age','none'),
                 ('Tom',18,'haha'),
                 ('jason',25,pd.NA),
                 ('mary',17,'hihi')])
print(df.to_numpy())

