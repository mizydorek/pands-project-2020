import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# import iris data set
data = pd.read_csv("iris.csv")

# global variables
filename = 'info.txt'
colors = ('red', 'green', 'blue')
Species = ('Setosa', 'Versicolor', 'Virginica')



#print(data.head())
#print(data.describe())
#print(data.info())
#print(data.groupby('Species').size())
#print(data['Species'])

# main menu
def displayMenu():
    print('Main Menu:')
    print('1. Info')
    print('2. Species')
    print('3. Data')
    print('4. Histogram')
    print('5. Box plot')
    print('6. Scatter plot')
    print('7. Violin plot')
    print('8. Pairplot plot')
    print('9. Quit')
    choice = input('Enter a number: ')
    return choice

def saveToFile():
    with open(filename) as writer:
        writer 

def info():
    toPrint = ('\n--- INFO ---',data.info(), '\n--- SHAPE ---\n',data.shape)
    print(toPrint)



def main():
    setosa_width = data[data['Species'] == 'Iris-setosa']['Sepal_width']
    setosa_length = data[data['Species'] == 'Iris-setosa']['Sepal_length']
    virginica_width = data[data['Species'] == 'Iris-virginica']['Sepal_width']
    virginica_length = data[data['Species'] == 'Iris-virginica']['Sepal_length']
    versicolor_width = data[data['Species'] == 'Iris-versicolor']['Sepal_width']
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
        details()
    elif choice == '3':
        histogram()
    elif choice == '4':
        boxPlot()
    elif choice == '5':
        scatterPlot()
    elif choice == '6':
        densityPlot()
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