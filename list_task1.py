'''
Write a Python program that accepts a sequence of words as input and prints the unique words in a sorted form.
'''

from typing import List, Tuple


def sort_unique_elements(str_list: Tuple[str]) -> List[str]:
    lista = []
    for word in str_list:
        if word not in lista:
            lista.append(word)
    lista = sorted(lista)
    return lista


x = ('red', 'white', 'black', 'red', 'green', 'black')
y = (1, 2, 3, 4, 5, 56, 7)
print(sort_unique_elements(x))
print(sort_unique_elements(y))