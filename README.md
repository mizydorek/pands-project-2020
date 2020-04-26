# Programming and Scripting - Project 2020

Repository contains my project for Programming and Scripting modul at GMIT. For more info [see here](https://github.com/ianmcloughlin/project-pands-2020/blob/master/project.pdf). All resources and references can be found in references section. 


### To do list 
- [x] ~Readme markdown~
- [x] ~Introduction~
- [x] ~Sir Ronald Fisher~
- [x] ~Fisher's Iris data set~
- [x] ~Iris dataset photo~
- [x] ~Preparation~
- [x] ~Box plots~
- [x] ~scatter plots~
- [x] ~violin plots~
- [x] ~density plots~

## Table of contents
* [Introduction](#introduction)
* [Preparations](#Preparations)
* [Data Visualization](#Data-Visualization)
* [Histogram](#Histogram)
* [References](#References)


## Sir Ronald Aylmer Fisher (17 February 1890 – 29 July 1962) 

Sir Ronald Aylmer Fisher was a British statistican, evolutionary biologist and geneticist, born in 1890 in London and died in 1962 in Adelaide, Australia. Described by Richard Dawkins as "the father of modern and experminetal design and the greatest of Dariwn's successors". Credited for numerous aspects of experimental design and modern statistical theory. 

<img src="https://www.sciencehistory.org/sites/default/files/styles/rte_full_width/public/rte/fisher_as_young_man.jpg?itok=yGmWp2qk" width="200px" />

**Few Intresting Facts about R. Fisher**

- Author of modern version of maximum likelihood method (MLE) between 1912 - 1922
- became a statistician at Rothamsted Experimental Station in 1919 where by having access to biological data he invents the tool of modern experimental design
- Creator of the F distribution and method of analysis of variance (ANOVA)
- Writer of 7 books, which *Statistical Methods for Research Workers* and *The Design of Experiments* are considered to be most influential books on statistical methods of the 20th century's.
- knighted by Queen Elizabeth in 1952, becoming Sir Ronald Aylmer Fisher.

## Fisher's Iris data set

Introduced by Ronal Fisher in 1936 in his paper *The use of multiple measurements in taxonomic problems* the Iris flower data set is a multivariate data set which was used to developed a linear discriminant model. Consists of three species of Iris flower (Iris setosa, Iris virginica, Iris versicolor) and four attributes from each specie: the length and the width of the sepals and petals, in centimeters. 

<img src="https://thegoodpython.com/assets/images/iris-species.png" width="100%"/>

### Preparations

Lets first import the necessary libraries

```python
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
```

and data from csv file.

```python
data = pd.read_csv("iris.csv")
```

### Dataset Summary

Now it is time to take a look at the data. 

Firstly, we can print basic information and dimension of the dataset.

```python
data.info()
data.shape
```

Dataset contains the range index of 150 entries and 5 columns. There is non null values and data types are float64 and object. 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.info.png" width="60%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.shape.png" width="60%" />

Sample of data

```python
data.head()
```

By default output shows first five rows.

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.head.png" width="60%" />

Explore more about species

```python
data.groupby('Species').size() 
data.groupby('Species').count() 
```

Each specie (class) contains 50 samples with 4 attributes (sepal length, sepal width, petal length, petal width). 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.groupby.png" width="60%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/species.count.png" width="60%" />

Lets take a look on summarize, dispersion and shape of dataset distribution.

```python
data.describe()
```

All attributes are in centimeters and range between 0 and 8.

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.describe.png" width="60%" />

Now more deep in details grouped by species.

```python
data[['Sepal_length','Species']].groupby('Species').describe()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/sepal.length.png" width="60%" />

```python
data[['Sepal_width','Species']].groupby('Species').describe()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/sepal.width.png" width="60%" />

```python
data[['Petal_length','Species']].groupby('Species').describe()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/petal.length.png" width="60%" />

```python
data[['Petal_width','Species']].groupby('Species').describe()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/petal.width.png" width="60%" />

### Data Visualization

Having a basic idea about the dataset now we can extend that with some vizualizations. This gives us much clearer idea of the distribution of input attributes. 

#### Histogram 

Histogram presentation of all attributes (both petal and sepal width and length) allows visualization of data distribution across all species.

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/setosa.hist.png" width="33%" /> <img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/versicolor.hist.png" width="33%" /> <img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/virginica.hist.png" width="33%" />

#### Box plot 

By using box plots we can detect and identify outliers. Outlier is a point or set of points that are different from others. They can be on both end sides (low and high). Shown below are the box plots of all attributes across all species. 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/boxplot.petal.length.png" width="50%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/boxplot.petal.width.png" width="50%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/boxplot.sepal.length.png" width="50%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/boxplot.sepal.width.png" width="50%" />

#### Scatter plot 

We often use scatter plots to find some correlation between variables. The scatter plots below are plotted accordingly to see relationship between attributes. 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/scatter.petal.png" width="100%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/scatter.sepal.png" width="100%" />

## References 

README markdown:

- [https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)
- [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#links)

Sir Ronald Aylmer Fisher (17 February 1890 – 29 July 1962) 

- [https://en.wikipedia.org/wiki/Ronald_Fisher](https://en.wikipedia.org/wiki/Ronald_Fisher)
- [https://www.famousscientists.org/ronald-fisher/](https://www.famousscientists.org/ronald-fisher/)
- [https://www.britannica.com/biography/Ronald-Aylmer-Fisher](https://www.britannica.com/biography/Ronald-Aylmer-Fisher)

Fishers's Iris data set

- [https://en.wikipedia.org/wiki/Iris_flower_data_set](https://en.wikipedia.org/wiki/Iris_flower_data_set)
- [https://archive.ics.uci.edu/ml/datasets/iris](https://archive.ics.uci.edu/ml/datasets/iris)