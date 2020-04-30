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
filename = 'summary.txt'
setosa = data[data['Species'] == 'Iris-setosa']
versicolor = data[data['Species'] == 'Iris-versicolor']
virginica = data[data['Species'] == 'Iris-virginica']

# main menu
def displayMenu():
    print('Main Menu:')
    print('1. Info')
    print('2. Species')
    print('3. Summary')
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
    print('Iris dataset')
    print('Shape of dataset: {}'.format(data.shape))
    print('Size of dataset: {}'.format(data.size))
    print(data.info())

def species():
    # Size and count of each species 
    print(data.groupby('Species').size())
    print(data.groupby('Species').count()) 

def summary(filename):
    # Dataset summary and attribute summary for each species. 
    print(data.describe())
    # save summary to txt file
    with open(filename, "w") as writer:
    # Write summary of data frame to file
        writer.write('Iris dataset\n\n')
        writer.write('Shape of dataset: {}\n'.format(data.shape))
        writer.write('Size of dataset: {}\n\n'.format(data.size))
        writer.write('Size of {}\n\n'.format(data.groupby('Species').size()))
        writer.write('Summary of dataset:\n {}\n\n'.format(data.describe()))
        writer.write('Summary of Setosa:\n {}\n\n'.format(setosa.describe()))
        writer.write('Summary of Versicolor:\n {}\n\n'.format(setosa.describe()))
        writer.write('Summary of Virginica:\n {}\n\n'.format(setosa.describe()))
        writer.write('Summary of Sepal length:\n {}\n\n'.format(data[['Sepal_length','Species']].groupby('Species').describe()))
        writer.write('Summary of Sepal width:\n {}\n\n'.format(data[['Sepal_width','Species']].groupby('Species').describe()))
        writer.write('Summary of Petal length:\n {}\n\n'.format(data[['Petal_length','Species']].groupby('Species').describe()))
        writer.write('Summary of Petal width:\n {}'.format(data[['Petal_width','Species']].groupby('Species').describe()))
def histogram():
    # draw histogram for all attributes across all species 
    data.hist(bins=20,
    edgecolor='black', 
    linewidth=1.0,
    xlabelsize=10, 
    ylabelsize=10,
    figsize=(10,9),
    grid=False 
)
    # save to file 
    plt.savefig('plots/histogram.png')
    plt.show()

    # clean up
    plt.close()

def boxPlot():

    species = ['Setosa', 'Versicolor', 'Virginica']
    fig, ax = plt.subplots()
    # boxplot using sepal width across all species 
    sns.boxplot(x="Species", y="Sepal_width", data=data)
    # plot settings 
    plt.title('Sepal width')
    plt.xlabel('')
    ax.set_xticklabels(species)
    plt.ylabel('Sepal width (cm)')
    # save to file 
    plt.savefig('plots/boxplot_sepal_width.png')
    plt.show()
    # clean up
    plt.close()
 
    fig, ax = plt.subplots()
    # boxplot using sepal length across all species 
    sns.boxplot(x="Species", y="Sepal_length", data=data)
    # plot settings 
    plt.title('Sepal length')
    plt.xlabel('')
    ax.set_xticklabels(species)
    plt.ylabel('Sepal length (cm)')
    plt.savefig('plots/boxplot_sepal_length.png')
    plt.show()
    # clean up
    plt.close()

    fig, ax = plt.subplots()
    # boxplot using petal width across all species 
    sns.boxplot(x="Species", y="Petal_width", data=data)
    # plot settings 
    plt.title('Petal width')
    plt.xlabel('')
    ax.set_xticklabels(species)
    plt.ylabel('Petal width (cm)')
    plt.savefig('plots/boxplot_petal_width.png')
    plt.show()
    # clean up
    plt.close()

    fig, ax = plt.subplots()
    # distribution of petal length 
    # boxplot using petal length across all species 
    sns.boxplot(x="Species", y="Petal_length", data=data)
    # plot settings 
    plt.title('Petal length')
    plt.xlabel('')
    ax.set_xticklabels(species)
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

    fig, axes = plt.subplots(2,2, figsize=(12, 8))

    # boxplot using sepal width across all species 
    sns.violinplot(x="Species", y="Petal_width", data=data,ax=axes[0,0])
    sns.violinplot(x="Species", y="Petal_length", data=data, ax=axes[0,1])
    sns.violinplot(x="Species", y="Sepal_width", data=data,ax=axes[1,0])
    sns.violinplot(x="Species", y="Sepal_length", data=data, ax=axes[1,1])

    # plot settings 
    plt.setp(axes[0, 0], 
        xlabel='',
        ylabel='Petal width (cm)', 
        title='Petal width', 
        xticklabels=['Setosa', 'Versicolor', 'Virginica'])
    plt.setp(axes[0, 1], 
        xlabel='',
        ylabel='Petal length (cm)', 
        title='Petal length', 
        xticklabels=['Setosa', 'Versicolor', 'Virginica'])
    plt.setp(axes[1, 0], 
        xlabel='',
        ylabel='Sepal width (cm)', 
        title='Sepal width', 
        xticklabels=['Setosa', 'Versicolor', 'Virginica'])
    plt.setp(axes[1, 1], 
        xlabel='',
        ylabel='Sepal length (cm)', 
        title='Sepal length', 
        xticklabels=['Setosa', 'Versicolor', 'Virginica'])
    # save to file 
    plt.savefig('plots/violinplot_iris.png')
    plt.show()
    # clean up
    plt.close()

def pairPlot():
    
    # pairplot for whole dataset 
    sns.pairplot(data, hue='Species', markers="o", 
        plot_kws= {'alpha': 0.8, 's': 14})

    # save to file 
    plt.savefig('plots/pairplot_iris.png')
    plt.show()
    # clean up
    plt.close()

choice = displayMenu()
while choice != '9':
    if choice == '1':
        info()
    elif choice == '2':
        species()
    elif choice == '3':
        summary(filename)
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