# Programming and Scripting - Project 2020

Repository contains my project for Programming and Scripting modul at GMIT. For more info [see here](https://github.com/ianmcloughlin/project-pands-2020/blob/master/project.pdf). All resources and references can be found in references section. 


### To do list 
- [x] ~Readme markdown~
- [x] ~Introduction~
- [x] ~Sir Ronald Fisher~
- [x] ~Fisher's Iris data set~
- [x] ~Iris dataset photo~
- [x] ~Preview~

## Table of contents
* [Introduction](#introduction)

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

### Content 

The data set contains of 150 samples of three classes (species). Each class contains 50 samples with 4 attributes (sepal length, sepal width, petal length, petal width). 

### Preview of Data 

Import data from csv file.

```python
import pandas as pd 

data = pd.read_csv("iris.csv")
```

Preview of header

```python
data.head()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.head.png" width="60%" />

```python
data.info()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.info.png" width="60%" />

```python
data.groupby('Species').size()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.groupby.png" width="60%" />

```python
data.describe()
```

<img src="https://github.com/mizydorek/pands-project-2020/blob/master/images/data.describe.png" width="60Ť%" />



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