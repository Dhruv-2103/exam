import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"]=[7.5,3.5]
plt.rcParams["figure.autolayout"] = True
headers = ['Name','Age','Marks']
df=pd.read_csv('students.csv',names=headers)
df.set_index('Name').plot()
plt.show()
