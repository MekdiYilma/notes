# DSI Notes
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


# Relevant Links
* [Visualizing `scipy.stats` distributions](https://stackoverflow.com/questions/37559470/what-do-all-the-distributions-available-in-scipy-stats-look-like)