#usind data iloc function for calling specific rows and columns
import pandas as pd
data=pd.read_csv('Data.csv')
value=data.iloc[:,-1]
print(value)
#for nested data call
val=data.iloc[0:5]
print(val)
#for nested row and column call
valu=data.iloc[0:,0:5]
print(val)
