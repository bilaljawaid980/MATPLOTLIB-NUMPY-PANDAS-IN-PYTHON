import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data=pd.read_csv('Data.csv')

age=data.iloc[0:,1].values

#converting age in months
age=age*12


salary=data.iloc[0:,2].values
#increasing 10000 salary
salary=salary+10000

x=age
y=salary
plt.title('GRAPH ')
plt.xlabel('AGE')
plt.ylabel('SALARY')
plt.plot(x,y)
plt.show()

