"""
Define a function linear_seq(sequence) which converts a passed sequence to a sequence without nested sequences.
"""
from typing import Any, List


def linear_seq(sequence: List[Any]) -> List[Any]:
    lista = []
    for i in sequence:
        if type(i) == int:
            lista.append(i)
        else:
            a = linear_seq(i)
            for j in a:
                lista.append(j)
    return lista


sequence = [1, 2, 3, [4, 5, (6, 7)]]

print(linear_seq(sequence))
