"""
Define a function seq_sum(sequence) which allows counting the sum of elements.
Elements of all nested sequences should be included.
"""

from typing import List, Tuple, Union


def seq_sum(sequence: Union[List, Tuple]) -> int:
    sum = 0
    for i in sequence:
        if type(i) == int:
            sum += i
        else:
            sum += seq_sum(i)
    return sum


sequence = [1, 2, 3, [4, 5, (6, 7)]]
print(seq_sum(sequence))
