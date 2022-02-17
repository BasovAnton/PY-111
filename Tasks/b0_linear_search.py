"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    print(arr)
    index_min_elem = 0
    for i in range(len(arr)):
        if arr[index_min_elem] > arr[i]:
            index_min_elem = i
    return index_min_elem
