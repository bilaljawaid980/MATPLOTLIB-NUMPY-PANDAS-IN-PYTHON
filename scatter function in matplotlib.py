#SCATTER FUNCTION IN MATPLOTLIB
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=2*x+5
plt.title("TUTORIAL GRAPH")
plt.xlabel("FREQUENCY")
plt.ylabel("AMPLITUDE")
plt.scatter(x,y)
plt.show()
