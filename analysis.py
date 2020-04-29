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



colors = ['red', 'tan', 'lime']

data.hist(bins=15,
                 color='steelblue',
                 edgecolor='black', linewidth=1.0,
                 xlabelsize=10, ylabelsize=10,
                 figsize=(10,9),
                 grid=False,

                 by='Species'
                 )



plt.show()
# clean up
plt.close()
'''
#fig, axes = plt.subplots(2,2, figsize=(12, 8))
'''

'''
# boxplot using sepal width across all species 
sns.pairplot(data, hue='Species', markers="o", 
    plot_kws= { 'alpha': 0.8, 's': 8})

# save to file 
#plt.savefig('plots/violinplot_iris.png')
plt.show()
# clean up
plt.close()
'''
 '''
    for patch, color in zip(df['boxes'], colors):
        patch.set_facecolor(color)
    '''

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
