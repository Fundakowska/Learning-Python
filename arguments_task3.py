"""
Implement a function that receives a changeable number of dictionaries (keys - letters, values - numbers) and combines them into one dictionary.
Dict values should be summarized in case of identical keys
"""
from typing import List, Dict


def combine_dicts(*args: List[Dict[str, int]]) -> Dict[str, int]:
    dct = dict()
    for diction in args:
        for el in diction:
            if el in dct:
                dct[el] += diction[el]
            else:
                dct[el] = diction[el]
    return dct


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2, dict_3))
