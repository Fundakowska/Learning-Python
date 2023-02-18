'''
Write a program which makes a pretty print of a part of the multiplication table.
Input:
row_start = 2
row_end = 4
column_start = 3
column_end = 7

Output: [[6, 8, 10, 12, 14], [9, 12, 15, 18, 21], [12, 16, 20, 24, 28]]
'''
from typing import List


def check(row_start: int, row_end: int, column_start: int, column_end: int) -> List[List[int]]:
    lista = []
    lista1 = [x for x in range(row_start, row_end+1)]
    lista2 = [x for x in range(column_start, column_end+1)]
    for i, value1 in enumerate(lista1):
        listaa = []
        for j, value2 in enumerate(lista2):
            listaa.append(value2*value1)
        lista.append(listaa)
    return lista


print(check(2, 4, 3, 7))
