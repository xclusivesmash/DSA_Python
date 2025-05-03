#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: locateIndex
description: find the index of a given element in an array.
"""
from typing import List

def locateIndex(array: List[int], item: int) -> int:
    """ @description.
    Args:
        array (List[int]): list of integers.
        item (int): item to search for in @array.
    Returns: index of @item. Otherwise, -1.
    """
    # 1. check if array is empty.
    if len(array) == []: return -1
    # 2. loop through array.
    for iCount, number in enumerate(array):
        # 3. check each element against item.
        if number == item: return iCount
    return -1


if __name__ == "__main__":
    # create test array.
    myarray = [25,105,-7,85,13,12,19,789,27,8]
    myitem = 105
    index = locateIndex(myarray, myitem)
    print(f"index: {index}, element at index: {myarray[index]}")
