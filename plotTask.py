# Kenneth Linehan, 2022
# This program displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

# importing the required module - adapted program from https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

import numpy as np
import matplotlib.pyplot as plt
# Imported modules in order to plot functions

#I start by defining each function needed, based on task
def f(x):
    return x

def g(x):
    return x*x

def h(x):
    return x*x*x

x = np.array(range(1, 5))
## Inbuilt fuction in numpy to create an array - https://numpy.org/doc/stable/reference/generated/numpy.array.html

functions = [f, g, h]

for func in functions:
    plt.plot(func(x), label=func.__name__)

# Display legend on the plot using .legend() function.
plt.legend

#Display plot, using .show() function.
plt.show()
