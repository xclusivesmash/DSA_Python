#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module; max_integer
description: finding the max. int. in a given array.
"""
from typing import List

def max_number(myArray: List[int]) -> int:
	""" @description.
	Args: myArray (List[int]): array of ints.
	Returns: max int. in @myArray
	"""
	# 1. set maximum to zero
	maximum = 0
	# 2. loop through the list
	for number in myArray:
		# 3. compare each item to maximum.
		# if maximum >= item:
		if number >= maximum:
			# set item to be maximum
			maximum = number
	# 4. return maximum
	return maximum


if __name__ == "__main__":
	# 5. initiate array
	myarray = [25,105,-7,85,13,12,19,789,27,8]
	maxi = max_number(myarray)
	print(maxi)
