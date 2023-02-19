"""
Implement a function that takes a number as an argument and returns a dictionary,
where a key is a number, and the value is the square of that number.
"""
from typing import Dict


def generate_squares(num: int) -> Dict[int, int]:
    dic = {}
    for i in range(1, num+1):
        dic.update({i: i*i})
    return dic


print(generate_squares(5))
