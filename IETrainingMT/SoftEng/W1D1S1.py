import numpy as np

def attach_names(data, names):
    """Function that makes a datastructure containing patient records. """
    assert len(data) == len(names) # This ensures that the length of the data and names are the same
    data_list = [] # Initialize a list to hold our output

    for data_row, name in zip(data, names, strict=True): # Here we use zip to go through data and names at the same time. Note you need "data_row" AND "name" to tell zip what you are appending together
        data_list.append({'name': name,
                          'data': data_row})

    return data_list

####### Task 1: Simple functions and appending data
patients = [
    {
        'name': 'Alice',
        'data': [1., 2., 3.],
    },
    {
        'name': 'Bob',
        'data': [4., 5., 6.],
    },
]

# print(patients)

# print()

# data = np.array([[1., 2., 3.],
#                  [4., 5., 6.]])

# data_list = attach_names(data, ['Alice', 'Bob'])
# print(f"Output:", data_list)

##### Task 2: Classes 

class Book:
    """Class to store info on different books and their authors"""
    def __init__ (self, book_title, author):
        self.book_title = book_title
        self.author = author


    def __str__(self):
        return self.book_title + ' by ' + self.author


book = Book('A Book', 'Me')

print(book)

