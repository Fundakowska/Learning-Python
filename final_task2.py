"""
Implement a function split_by_index(s: str, indexes: List[int]) -> List[str]
which splits the s string by indexes specified in indexes.
The wrong indexes must be ignored"""
from typing import List


def split_by_index(s: str, indexes: List[int]) -> List[str]:
    sentence_list = []
    start = 0
    for j in indexes:
        if j > len(s):
            continue
        else:
            sentence_list.append(s[start:j])
            start = j
    sentence_list.append(s[start:])
    return sentence_list


print(split_by_index("no luck", [42, 2]))
