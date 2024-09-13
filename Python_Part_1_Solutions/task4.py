"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    length = len(ints)
    list2 = []
    for i in range(length):
        if i==0:
            val = ints[i]**2 
            list2.append(val)
        else:
            val = ints[i]**2 - ((ints[i-1]**2) - ints[(i-1)])
            list2.append(val)
    return list2


calculate_power_with_difference([1, 2, 3])

        

