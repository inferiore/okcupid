import pandas as pd
import json as j

df = pd.DataFrame({'key': ['A', 'B', 'B', 'A', 'B', 'A']
                   ,'data': [1,1,2,3,4,5,]
                 ,'key2': ['B', 'B', 'B', 'A', 'B', 'B']

                       }, columns=['key','key2', 'data'])
print (df)
print(df.groupby(['key2','key']).sum())
