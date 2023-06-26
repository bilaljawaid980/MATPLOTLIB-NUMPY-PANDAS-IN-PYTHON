import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv('House price.csv')
area=data.iloc[:,0].values
area=area/1000
price=data.iloc[:,1].values
price=price*300
x=area
y=price
plt.xlabel('AREA')
plt.ylabel('PRICE')
plt.title("FIRST TASK")
plt.scatter(x,y)
plt.show()
