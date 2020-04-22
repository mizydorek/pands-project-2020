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
    setosa_width = data[data['Species'] == 'Iris-setosa']['Petal_width']
    setosa_length = data[data['Species'] == 'Iris-setosa']['Petal_length']
    virginica_width = data[data['Species'] == 'Iris-virginica']['Petal_width']
    virginica_length = data[data['Species'] == 'Iris-virginica']['Petal_length']
    versicolor_width = data[data['Species'] == 'Iris-versicolor']['Petal_width']
    versicolor_length = data[data['Species'] == 'Iris-versicolor']['Petal_length']
    fig, ax = plt.subplots(figsize=(12, 6))
    #ax.scatter(setosa_length, setosa_width, marker='o', c='r', s=10, alpha=0.6, label="Setosa")
    #ax.scatter(versicolor_length, versicolor_width, marker='o', c='g', s=10, alpha=0.6, label="Versicolor")
    #ax.scatter(virginica_length, virginica_width, marker='o', c='b', s=10, alpha=0.6, label="Virginica")
    
    data_to_plot[setosa_width, versicolor_width, virginica_width]

    ax.violinplot(data_to_plot)
    
    '''
    ax.set_title('Petal width vs length')
    ax.legend(loc='upper left')
    ax.set_xlabel('width(cm)')
    ax.set_ylabel('length(cm)')
    '''
    
main()
plt.show()
