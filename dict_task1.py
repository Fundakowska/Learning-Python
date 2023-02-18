'''
Write a Python program to count the frequency of each character in a string (ignore the case of letters).
'''
from typing import Dict


def get_dict(s: str) -> Dict[str, int]:
    all_freq = {}
    for i in s.lower():
        if i in all_freq:
            all_freq[i] += 1
        else:
            all_freq[i] = 1

    return all_freq


print(get_dict('Oh, it is python'))
