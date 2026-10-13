### Functional programming worktasks ###

import numpy as np
from functools import reduce 
import time

#1: Which functions are pure?

# def add_one(x):
#     return x + 1 # Pure. X is not modified, it just adds one to the variable given

# def say_hello(name):
#     print('Hello', name) # IMPURE! (Wrongly said pure initially)... Remember that any print statments are IMPURE

# def append_item_1(a_list, item): # Impure. Changes list by appending to it
#     a_list += [item]
#     return a_list

# def append_item_2(a_list, item):  #Pure. Does not change list, as it makes a new variable, so it remains pure.
#     result = a_list + [item]
#     return result


# #2: refactoring Conway's game of life:

# import numpy as np

# def step(grid):             # Steps over the grid , finds the neighbours, counts the neighbours, and modifies the state based on the neighbours
#     rows, cols = grid.shape
#     updated_grid = np.zeros_like(grid) #Initialise a grid in the same structure as original grid. Note this can also be done with np.zeros((rows,cols, dtype=np.int8))
#     for i in range(rows):
#         for j in range(cols):
#             neighbours = get_neighbours(grid, i, j)
#             count = sum(neighbours)            
#             # cells are unaffected unless they:
#             # - die of under- or overpopulation, or
#             # # - become alive if they have exactly three neighbours

#             ####### Old outdated bit ######
#             # if count < 2 or count > 3:   # NOTE: I missed something in here. As the new array is now all 0's, I need to change these steps better.
#             #     updated_grid[i, j] = 0
#             # elif count == 3:
#             #     updated_grid[i, j] = 1

#             if (count == 2 and grid[i][j] ==1) or count == 3:
#                 updated_grid[i,j]=1

#     return updated_grid

                 
# def get_neighbours(grid, i, j):
#     rows, cols = grid.shape
#     indices = np.array([(i-1, j-1), (i-1, j), (i-1, j+1),
#                         (i, j-1),             (i, j+1),
#                         (i+1, j-1), (i+1, j), (i+1, j+1)])
#     valid_indices = (indices[:, 0] >= 0) & (indices[:, 0] < rows) & \
#                     (indices[:, 1] >= 0) & (indices[:, 1] < cols)
#     return grid[indices[valid_indices][:, 0], indices[valid_indices][:, 1]]

# # Test
# grid = np.array([[0, 0, 0, 0, 0],
#                  [0, 0, 1, 0, 0],
#                  [0, 1, 1, 1, 0],
#                  [0, 0, 1, 0, 0],
#                  [0, 0, 0, 0, 0]], dtype=np.int8)
# new_grid = step(grid)
# print(new_grid)

# print()



# # our grid should show a square pattern, but doesn't
# expected_grid = np.array([[0, 0, 0, 0, 0],
#                           [0, 1, 1, 1, 0],
#                           [0, 1, 0, 1, 0],
#                           [0, 1, 1, 1, 0],
#                           [0, 0, 0, 0, 0]], dtype=np.int8)


# print(f"Expected grid", expected_grid)
# assert np.array_equal(new_grid, expected_grid)


# ## 2.b: From reading on lambda functions:

# add_one = lambda x: x + 1 # NOQA E731  #NOTE: THis is an example of assigning lambda to a variable, hence the need for a NOQA directive as this is normally considered bad practice and would split errors.

# print(add_one(1))

#3 Sum of squares


# def sum_of_squares(list_):
#     """Function that returns the sum of squares of a given number"""

#     filtered_list = filter(lambda x: x[:1] != '#', list_)
#     int_list= map(int, filtered_list)
#     squares = map(lambda x: x**2, int_list)

#     return reduce(lambda a, b: a+b, squares)


# print(sum_of_squares([0]))
# print(sum_of_squares([1]))
# print(sum_of_squares([1, 2, 3])) #NOTE: For when function worked with list of integers given
# print(sum_of_squares([-1]))
# print(sum_of_squares([-1, -2, -3]))

# print(sum_of_squares(['1', '2', '3']))
# print(sum_of_squares(['-1', '-2', '-3']))

# print(sum_of_squares(['1', '2', '3']))
# print(sum_of_squares(['-1', '-2', '-3']))
# print(sum_of_squares(['1', '2', '#100', '3']))

# print({2 * i for i in range(5)})
# print((2 * i for i in range(5)))

#4: Measuring performance using decorators

# First playing around with process_time_ns to figure out how it works

# def measure_me(n):
#     total = 0
#     for i in range(n):
#         total += i * i

#     return total


# print(time.process_time_ns())

# start = time.process_time_ns()
# result = measure_me(10)
# end = time.process_time_ns()

# print(f"Start time:", start)
# print(f"End time:", end)
# print(f"Total computation time:", end - start)


## Now attempting the decorator function 
def measure_execute_time(func):
    """A decorator function that calculates the compute time of a function supplied to it."""

    def inner(*args, **kwargs):
        start = time.process_time_ns()
        print(f"Start time:",start)
        result = func(*args,**kwargs)
        print(f"operation result:", result)
        end = time.process_time_ns()
        print(f"End time:", end)
        print(f"Total execution time:", end - start)
        return result

    return inner


# def measure_me(n):
#     total = 0
#     for i in range(n):
#         total += i * i

#     return total

# value = measure_me(1000)
# print(f"value:",value)
# print()

#measure_me = measure_execute_time(measure_me)

# Trying the 2nd syntax for decorators

@measure_execute_time
def measure_me(n):
    total = 0
    for i in range(n):
        total += i * i

    return total

print(measure_me(1000))