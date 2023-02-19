"""
Create generic union and intersect functions to work with sets.
The functions must accept an arbitrary number of arguments of different types: list, tuple, and set.
Each function must return the value of the set type.
"""


def union(*args) -> set:
    lst = []
    for lista in args:
        for el in lista:
            lst.append(el)
    return set(lst)


def intersect(*args) -> set:
    dct = dict()
    lista1 = []
    for lista in args:
        for el in lista:
                if el in dct:
                    dct[el] += 1
                else:
                    dct[el] = 1
    for key in dct:
        if dct[key] == len(args):
            lista1.append(key)
    return set(lista1)


print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))
