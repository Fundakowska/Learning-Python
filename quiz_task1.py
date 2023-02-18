'''
Write a Python program to print all the unique values of all the dictionaries in a list.
'''
from typing import Any, Dict, List, Set


def check(lst: List[Dict[Any, Any]]) -> Set[Any]:
    unique= set(value for dic in lst for value in dic.values())
    return unique


print(check([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]))
