# DSI Notes

# Python Intro

Data Types 

Mutable: Lists, Sets, Dictionaries

Immutable: Tuples, integers, floats, strings

Jupyter
esc + b/a (enter cells below and above)
esc +m  = converts to a markdown cell

### Loops
initial_lst = range(-10,10)

abs_for_loop = []

for elem in initial_lst:
    abs_for_loop.append(abs(elem))

### Map

dir(list) #provides list of methods that can be used for the type 
map? #provide direction on how to use methods
shift+tab #provide direction on how to use methods

abs_map = map(abs,initial_lst)
list(abs_map)

### List Comprehension
abs_lstcomp = [abs(elem) for elem in initital_lst]

### Data Type Verification
is_instance(x, int) 
type(x) == int 

### Tuple

my_tuple = (1,) # if we remove the comma it becomes an int
.index(elem) #returns the location of the elem
tuple assignment does not work because tuple is immutable (e.g., my_tuple[0] = 2 would throw an error)


### Dictionaries

d['key']
d.get('key','if error return this')
from collections import defaultdict
d_default = default(lambda: 'value not found')
d_default.update(d)
d['key'] = 'new value' #dictionary assignment


### Sets

store unique elements

# Numpy

x.reshape(-1,5) # modify the given array, x, into certain rows and five columns but python is set to figure how how many rows 


* Numpy arrays can hold one and only one type of data.
* Numpy arrays are super efficient both in terms of memory footprint and computational efficiency.
* Numpy arrays have a size, and the size cannot be changed. (x.size) **
* Numpy arrays have a shape, which allows them to be multi-dimensional (examples forthcoming).
* One major difference between arrays and lists is that arrays cannot be extended. (e.g, x.append is an error)
* Broadcasting can only be performed when the shape of each dimension in the arrays are equal and/or one has the dimension size of 1.


**Although the total size of an array cannot be changed, the shape of the array can be changed, as long as this change of shape does not create or destroy elements



# Machine Learning Workflows

### Cross Validation

### K-fold cross Validation

### Bootstrap



# Sorting Algorithms

### Bubble sort

### 

# Relevant Links
* [Visualizing `scipy.stats` distributions](https://stackoverflow.com/questions/37559470/what-do-all-the-distributions-available-in-scipy-stats-look-like)
* [Git Branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
* [Git Branch Workflows](https://buddy.works/blog/5-types-of-git-workflows)
* [Git Adding a Remote](https://docs.github.com/en/github/using-git/adding-a-remote)
* [Normal Distribution](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/more-on-normal-distributions/v/introduction-to-the-normal-distribution)
* [Seeing Theory](https://seeing-theory.brown.edu/basic-probability/index.html)
* [Make the Most Out of your `pandas.read_csv()`](https://medium.com/analytics-vidhya/make-the-most-out-of-your-pandas-read-csv-1531c71893b5)
* [Fundamentals of Machine Learning for Predictive Data Analytics](https://mitpress.mit.edu/books/fundamentals-machine-learning-predictive-data-analytics)


## Additional Resources for DS
* [Kaggle Competitions](https://www.kaggle.com/learn/python)
* [LeetCode](https://leetcode.com/)
* [Udemy](https://www.udemy.com/)
* []()

## Grad School 
* [Stanford HCP Program](https://gradadmissions.stanford.edu/programs/hcp)
* [Stanford How to Apply](https://statistics.stanford.edu/admissions/ms/external/how-apply)



# Bash Scripting 

### Bash profile location on OSX
`~./bash_profile`

### Make a bash function

```bash
function gitadder() {
    git pull
    git add .
    dt =$(date '+%d/%m/%Y %H:%M:%S');
    git commit -m "Updated: $(date '+%a %M:%H %h %d % Y')"
    git push
}

```

