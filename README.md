# Programming and Scripting - Project 2020

Repository contains my project for Programming and Scripting modul at GMIT. For more info [see here](https://github.com/ianmcloughlin/project-pands-2020/blob/master/project.pdf). All resources and references can be found in references section. 


### To do list 
- [x] ~Readme markdown~
- [x] ~Reasearch about Ronald Fisher and his Iris dataset~
- [x] ~Introduction~
- [x] ~Sir Ronald Fisher~
- [x] ~Fisher's Iris data set~
- [x] ~Iris dataset photo~
- [x] ~Preparation~
- [x] ~Box plots~
- [x] ~scatter plots~
- [x] ~violin plots~
- [x] ~Pair plots~

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

Firstly, we can print basic information and dimension of the data.

```python
data.info()
data.shape
```

Dataset contains the range index of 150 entries and 5 columns. There is non null values and data types are float64 and object. 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.info.png" width="60%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.shape.png" width="60%" />

Preview of data

```python
data.head()
```

Function returns first n rows of dataset. By default shows first five rows.

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
It shows min, max, mean, std and quantile values. 
All attributes are in centimeters and range between 0 and 8.

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.describe.png" width="60%" />

Going further deep in details we can display every attribute according to each species by grouping them separately.

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

Having a basic idea about the dataset now we can extend that with some vizualizations. This will give us much clearer idea of the distribution of input attributes. 

#### Histogram 

Histogram presentation of all attributes (both petal and sepal width and length) allows visualization of data distribution across all species. 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/setosa.hist.png" width="33%" /> <img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/versicolor.hist.png" width="33%" /> <img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/virginica.hist.png" width="33%" />

#### Box plot 

By using box plots we can detect and identify outliers. Outlier is a point or set of points that are different from others. They can be on both end sides (low and high). Shown below are the box plots of all attributes across all species. 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/plots/boxplot_petal_length.png" width="50%" /><img src="https://github.com/mizydorek/pands-project-2020/blob/master/plots/boxplot_petal_width.png" width="50%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/plots/boxplot_sepal_length.png" width="50%" /><img src="https://github.com/mizydorek/pands-project-2020/blob/master/plots/boxplot_sepal_width.png" width="50%" />

It can be seen that there are very few of outliers and it  will not have an impact on our analysis. We can clearly noticed that there is distinct difference in distributions for both Petal width and length across species. Setosa’s petal length and width makes setosa differing from other species. Sepal width seems to be the most similar across all of them. 

#### Scatter plot 

Also known as Relational plots. We often use scatter plots to find some correlation between variables. The correlation can help us understand our data more and see relationship between attributes. 

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/plots/scatterplot_sepal.png" width="100%" />

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/plots/scatterplot_petal.png" width="100%" />

In terms of sepal length vs width setosa appears to be  the only specie that differs in distinctive way from the others. Versicolor and virginica are a little more varied and overlapping together. Examining the petal length vs width we can observe linear regression across all the species. The plot also shows that this a good way to differentiate between species where setosa again differs the most from other species. 

#### Violin plot 

Belongs to categorial plots and is also necessary in data exploration step, as can be used to observe how different classes of variable are distributed in dataset.

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/plots/violinplot_iris.png" width="100%" />

The violin plots clearly show that based on petal length and width setosa's shape is completly different from other two species. Versicolor and virginica have considerably longer petal than setosa. We can distinguish significant dissimilarity between Setosa's petal and sepal. The differentiation is smaller in species versicolor and virginica. We can also observed that virginica has the highest median in sepal length, petal length and width while sepal width is the most similar across all species and highly concentrated around the median.

#### Pair plot 

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

Pandas

- [https://realpython.com/pandas-dataframe/](https://realpython.com/pandas-dataframe/)

- [https://realpython.com/pandas-python-explore-dataset/](https://realpython.com/pandas-python-explore-dataset/)

- [https://backtobazics.com/python/pandas-describe-method-dataframe-summary/](https://backtobazics.com/python/pandas-describe-method-dataframe-summary/)

Histogram
- [https://realpython.com/python-histograms/](https://realpython.com/python-histograms/)