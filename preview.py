import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
'''
with open("iris.data", 'r') as reader:
    print(reader.read())
'''
data = pd.read_csv("iris.csv")

#print(data.head())
#print(data.describe())
#print(data.info())
#print(data.groupby('Species').size())
#print(data['Species'])

colors = ('red', 'green', 'blue')
Species = ('Setosa', 'Versicolor', 'Virginica')

def main():
    setosa_width = data[data['Species'] == 'Iris-setosa']['Sepal_width']
    setosa_length = data[data['Species'] == 'Iris-setosa']['Sepal_length']
    virginica_width = data[data['Species'] == 'Iris-virginica']['Sepal_width']
    virginica_length = data[data['Species'] == 'Iris-virginica']['Sepal_length']
    versicolor_width = data[data['Species'] == 'Iris-versicolor']['Sepal_width']
    versicolor_length = data[data['Species'] == 'Iris-versicolor']['Sepal_length']
    fig, ax = plt.subplots(figsize=(6, 6))
    #ax.scatter(setosa_length, setosa_width, marker='o', c='r', s=10, alpha=0.6, label="Setosa")
    #ax.scatter(versicolor_length, versicolor_width, marker='o', c='g', s=10, alpha=0.6, label="Versicolor")
    #ax.scatter(virginica_length, virginica_width, marker='o', c='b', s=10, alpha=0.6, label="Virginica")
    
    data_to_plot = [setosa_length, versicolor_length, virginica_length]

    ax.set_title('Sepal length')
    df = ax.boxplot(data_to_plot, patch_artist=True)
    #ax.violinplot(data_to_plot)
    ax.yaxis.grid(True)
    ax.set_ylabel('cm')
    plt.setp(ax, xticks=[y+1 for y in range(len(data_to_plot))],
        xticklabels=['Setosa', 'Versicolor', 'Virginica'])
    '''
    for patch, color in zip(df['boxes'], colors):
        patch.set_facecolor(color)
    '''
    '''
    ax.set_title('Petal width vs length')
    ax.legend(loc='upper left')
    ax.set_xlabel('length(cm)')
    ax.set_ylabel('width(cm)')
    '''


    
main()
plt.show()
