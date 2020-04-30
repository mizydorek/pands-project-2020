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
setosa = data[data['Species'] == 'Iris-setosa']
versicolor = data[data['Species'] == 'Iris-versicolor']
virginica = data[data['Species'] == 'Iris-virginica']

