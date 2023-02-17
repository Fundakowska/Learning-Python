'''
Implement a function get_pairs(lst: List) -> List[Tuple] which returns a list of tuples containing pairs of elements.
The pairs should be formed as in the example. If there is only one element in the list, return [] instead.
'''
from typing import Any, Tuple, List


def get_pairs(lst: List[Any]) -> List[Tuple[Any, Any]]:
    if len(lst) == 1:
        lst2 = []
    else:
        lst2 = []
        for i in range(1, len(lst)):
            lst2.append((lst[i-1], lst[i]))
    return lst2


print(get_pairs([1, 2, 3, 8, 9]))
