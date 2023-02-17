'''
Implement a function foo(List[int]) -> List[int] which, given a list of
integers, returns a new list such that each element at index i of the new list
is the product of all the numbers in the original array except the one at i.
'''

from typing import List


def foo(nums: List[int]) -> List[int]:
    temp = [x*0 for x in range(len(nums))]
    product = 1
    for element in nums:
        product = product * element

    for i in range(len(nums)):
       temp[i] = int(product/nums[i])
    return temp


print(foo([1, 2, 3, 4, 5]))
