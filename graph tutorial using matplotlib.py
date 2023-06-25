import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
x=np.arange(1,11)
y=2*x+5
plt.title('TUTORIAL GRAPH')
plt.xlabel('FREQUENCY')
plt.ylabel('AMPLITUDE')
plt.plot(x,y)
plt.show()
