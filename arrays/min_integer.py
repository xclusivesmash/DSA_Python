#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: min_integer
description: finding the minimum within an array.
"""
from typing import List

def min_number(myArray: List[int]) -> int:
	""" @description.
	Args: myArray (List[int]): list of integers.
	Returns: minimum within @myArray.
	"""
	# 1. set myArray[0] to be the minimum
	minimum = myArray[0]
	# 2. loop through the array
	for item in myArray:
		# check if the given item <= minimum
		if item <= minimum:
			# if so, set minimum to item.
			minimum = item
	# 3. return minimum
	return minimum


if __name__ == "__main__":
	# 4. initialize array
	myarray = [25,105,-7,85,13,12,19,789,27,8]
	minimum = min_number(myarray)
	print(minimum)
