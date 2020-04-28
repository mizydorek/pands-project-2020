import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("iris.csv")

colors = ('red', 'green', 'blue')
species = ('Setosa', 'Versicolor', 'Virginica')
setosa = data[data['Species'] == 'Iris-setosa']

fig, ax = plt.subplots(1,3, figsize=(18, 9))
data.plot(kind='hist', ax=ax[0], grid=True)
plt.show()


'''
# heatmap
plt.figure(figsize=(10,11))
sns.heatmap(data.corr())
plt.plot()
'''
