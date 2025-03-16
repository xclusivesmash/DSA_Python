#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: reverse_string
description: reverses a string without using str[::-1]
"""

def reverse_string(string: str) -> str:
	""" @description.
	Args:
		string (str): input string to reverse.
	Return:
		reversed string (str).
	"""
	# 1. set pointers
	i = 0
	j = len(string) - 1
	# 1.1 create an empty list
	myList = [0]*len(string)
	# 2. loop through the string
	while i < j:
		# 3. swap the values at their respective places.
		myList[i] = string[j]
		myList[j] = string[i]
		# increment i
		i = i + 1
		# decrement j
		j = j - 1
	# 4. return the reversed string.
	return ''.join(myList)


if __name__ == "__main__":
	# define test string
	mystring = "hellow world"
	reversed_string = reverse_string(mystring)
	print(reversed_string)
