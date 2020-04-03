import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
'''
with open("iris.data", 'r') as reader:
    print(reader.read())
'''
data = pd.read_csv("iris.csv")

print(data.head())
#print(data.describe())
#print(data.info())