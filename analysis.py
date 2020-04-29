import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("iris.csv")

colors = ('red', 'green', 'blue')
species = ('setosa', 'versicolor', 'virginica')
setosa = data[data['Species'] == 'Iris-setosa']
versicolor = data[data['Species'] == 'Iris-versicolor']
virginica = data[data['Species'] == 'Iris-virginica']
attr = ('Sepal_length','Sepal_width','Petal_length','Petal_width')

fig, ax = plt.subplots(1,2, figsize=(14, 6))

# boxplot using sepal width across all species 
sns.violinplot(x="Species", y="Petal_width", data=data,ax=ax[0])
sns.violinplot(x="Species", y="Petal_length", data=data, ax=ax[1])
# plot settings 
plt.setp(ax[0], 
    xlabel='',
    ylabel='Petal width (cm)', 
    title='Petal width', 
    xticklabels=['Setosa', 'Versicolor', 'Virginica'])
plt.setp(ax[1], 
    xlabel='',
    ylabel='Petal length (cm)', 
    title='Petal length', 
    xticklabels=['Setosa', 'Versicolor', 'Virginica'])
# save to file 
plt.savefig('plots/violinplt_petal.png')
plt.show()
# clean up
plt.close()



'''
ax.set_title('Sepal length')
# df = ax.boxplot(data_to_plot, patch_artist=True)
ax.violinplot(data_to_plot)
ax.yaxis.grid(False)
ax.set_ylabel('cm')
plt.setp(ax, xticks=[y+1 for y in range(len(data_to_plot))],
    xticklabels=['Setosa', 'Versicolor', 'Virginica'])
plt.show()
'''

'''
fig, ax = plt.subplots(1,3, figsize=(18, 9))
data.plot(kind='hist', ax=ax[0], grid=True)
plt.show()
'''

'''
# heatmap
plt.figure(figsize=(10,11))
sns.heatmap(data.corr())
plt.plot()
'''
