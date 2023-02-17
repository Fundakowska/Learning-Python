'''
Implement a function get_tuple(num: int) -> Tuple[int] which returns a tuple of a given integer's digits.
'''
from typing import Tuple


def get_tuple(num: int) -> Tuple[int]:
    splited = list(str(num))
    a = [int(x) for x in splited]
    end = tuple(a)
    return end

print(get_tuple(87178291199))
