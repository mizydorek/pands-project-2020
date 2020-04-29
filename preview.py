# Maciej Izydorek 
# GMIT G00387873
# Fisher's Iris dataset
# A script to analyse Iris dataset and output information about species

# neccessary libraries 
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# import iris data set
data = pd.read_csv("iris.csv")

# global variables
colors = ('red', 'green', 'blue')
species = ('Setosa', 'Versicolor', 'Virginica')
setosa = data[data['Species'] == 'Iris-setosa']
versicolor = data[data['Species'] == 'Iris-versicolor']
virginica = data[data['Species'] == 'Iris-virginica']
attr = ['Sepal_length','Sepal_width','Petal_length','Petal_width']

# main menu
def displayMenu():
    print('Main Menu:')
    print('1. Info')
    print('2. Species')
    print('3. Details')
    print('4. Histogram')
    print('5. Box plot')
    print('6. Scatter plot')
    print('7. Violin plot')
    print('8. Pairplot plot')
    print('9. Quit')
    choice = input('Enter a number: ')
    return choice

def info():
    # basic info shape of dataset
    print(data.info(), '\nShape: ', data.shape)

def species():
    # Size and count of each species 
    print(data.groupby('Species').size())
    print(data.groupby('Species').count()) 

def details():
    # Dataset summary and attribute summary for each species. 
    print(data.describe())
    # save summary to txt file
    data.describe().to_csv("summary.txt", sep=',')
    print(data[['Sepal_length','Species']].groupby('Species').describe())
    print(data[['Sepal_width','Species']].groupby('Species').describe())
    print(data[['Petal_length','Species']].groupby('Species').describe())
    print(data[['Petal_width','Species']].groupby('Species').describe())

def histogram():
    
    data.groupby('Species').hist()
    plt.show()
    plt.close()

def boxPlot():

    # boxplot using sepal width across all species 
    sns.boxplot(x="Species", y="Sepal_width", data=data)
    # plot settings 
    plt.title('Sepal width')
    plt.xlabel('')
    plt.ylabel('Sepal width (cm)')
    # save to file 
    plt.savefig('plots/boxplot_sepal_width.png')
    plt.show()
    # clean up
    plt.close()
 
    # boxplot using sepal length across all species 
    sns.boxplot(x="Species", y="Sepal_length", data=data)
    # plot settings 
    plt.title('Sepal length')
    plt.xlabel('')
    plt.ylabel('Sepal length (cm)')
    plt.savefig('plots/boxplot_sepal_length.png')
    plt.show()
    # clean up
    plt.close()

    # boxplot using petal width across all species 
    sns.boxplot(x="Species", y="Petal_width", data=data)
    # plot settings 
    plt.title('Petal width')
    plt.xlabel('')
    plt.ylabel('Petal width (cm)')
    plt.savefig('plots/boxplot_petal_width.png')
    plt.show()
    # clean up
    plt.close()

    # distribution of petal length 
    # boxplot using petal length across all species 
    sns.boxplot(x="Species", y="Petal_length", data=data)
    # plot settings 
    plt.title('Petal length')
    plt.xlabel('')
    plt.ylabel('Petal length (cm)')
    plt.savefig('plots/boxplot_petal_length.png')
    plt.show()
    # clean up
    plt.close()

def scatterPlot():

    fig, ax = plt.subplots(figsize=(12, 6))
    # scatterplot of sepal across all species 
    ax.scatter(setosa['Sepal_length'], setosa['Sepal_width'], marker='o', c='r', s=10, alpha=0.6, label="Setosa")
    ax.scatter(versicolor['Sepal_length'], versicolor['Sepal_width'], marker='o', c='g', s=10, alpha=0.6, label="Versicolor")
    ax.scatter(virginica['Sepal_length'], virginica['Sepal_width'], marker='o', c='b', s=10, alpha=0.6, label="Virginica")
    # Scatter plot settings
    ax.set_title('Sepal width vs length')
    ax.legend(loc='upper left')
    ax.set_xlabel('length(cm)')
    ax.set_ylabel('width(cm)')
    # save to file 
    plt.savefig('plots/scatterplot_sepal.png')
    plt.show()
    plt.close()

    fig, ax = plt.subplots(figsize=(12, 6))
    # scatterplot of sepal across all species 
    ax.scatter(setosa['Petal_length'], setosa['Petal_width'], marker='o', c='r', s=10, alpha=0.6, label="Setosa")
    ax.scatter(versicolor['Petal_length'], versicolor['Petal_width'], marker='o', c='g', s=10, alpha=0.6, label="Versicolor")
    ax.scatter(virginica['Petal_length'], virginica['Petal_width'], marker='o', c='b', s=10, alpha=0.6, label="Virginica")
    # Scatter plot settings
    ax.set_title('Petal width vs length')
    ax.legend(loc='upper left')
    ax.set_xlabel('length(cm)')
    ax.set_ylabel('width(cm)')
    # save to file 
    plt.savefig('plots/scatterplot_petal.png')
    plt.show()
    plt.close()

def violinPlot():

    fig, ax = plt.subplots(1,2, figsize=(14, 6))

    # violin plot using petal length and width across all species 
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
    plt.savefig('plots/violinplot_petal.png')
    plt.show()
    # clean up
    plt.close()

def main():
    setosa_width = data[data['Species'] == 'Iris-setosa']['Sepal_width']
    setosa_length = data[data['Species'] == 'Iris-setosa']['Sepal_length']
    virginica_width = data[data['Species'] == 'Iris-virginica']['Sepal_width']
    virginica_length = data[data['Species'] == 'Iris-virginica']['Sepal_length']
    versicolor_with = data[data['Species'] == 'Iris-versicolor']['Sepal_width']
    versicolor_length = data[data['Species'] == 'Iris-versicolor']['Sepal_length']

    c = data.corr()

    iris = data[['Sepal_width','Sepal_length']]  
    sns.heatmap(iris)

    fig, ax = plt.subplots(figsize=(6, 6))

    '''
    # Draw scatter plots to check distribution across all species according to Petal and Sepal
    ax.scatter(setosa_length, setosa_width, marker='o', c='r', s=10, alpha=0.6, label="Setosa")
    ax.scatter(versicolor_length, versicolor_width, marker='o', c='g', s=10, alpha=0.6, label="Versicolor")
    ax.scatter(virginica_length, virginica_width, marker='o', c='b', s=10, alpha=0.6, label="Virginica")
    '''
    sns.kdeplot(data['Sepal_width'], shade=True, color='r')
    sns.kdeplot(data['Sepal_length'], shade=True, color='b')
    sns.kdeplot(data['Petal_width'], shade=True, color='g')
    sns.kdeplot(data['Petal_length'], shade=True, color='a')

    data_to_plot = [setosa_length, versicolor_length, virginica_length]

   


    '''
    sns.distplot(data_to_plot, hist = False, kde = True,
                 kde_kws = {'shade': True, 'linewidth': 3}, 
                  label = Species)
    '''
    '''
    ax.set_title('Sepal length')
    df = ax.boxplot(data_to_plot, patch_artist=True)
    #ax.violinplot(data_to_plot)
    ax.yaxis.grid(True)
    ax.set_ylabel('cm')
    plt.setp(ax, xticks=[y+1 for y in range(len(data_to_plot))],
        xticklabels=['Setosa', 'Versicolor', 'Virginica'])

    '''
    '''
    for patch, color in zip(df['boxes'], colors):
        patch.set_facecolor(color)
    '''
    '''
    # Scatter plot settings
    ax.set_title('Petal width vs length')
    ax.legend(loc='upper left')
    ax.set_xlabel('length(cm)')
    ax.set_ylabel('width(cm)')
    '''

choice = displayMenu()
while choice != '9':
    if choice == '1':
        info()
    elif choice == '2':
        species()
    elif choice == '3':
        details()
    elif choice == '4':
        histogram()
    elif choice == '5':
        boxPlot()
    elif choice == '6':
        scatterPlot()
    elif choice == '7':
        violinPlot()
    elif choice == '8':
        pairPlot()
    elif choice != '9':
        print('\nplease select one of the option')
    print('\n')
    choice = displayMenu()


'''   
main()
plt.show()
'''