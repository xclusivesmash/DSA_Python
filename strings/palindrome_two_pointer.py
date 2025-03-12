#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: palindrome_two_pointer
description: a palindrome reads the same both forwards
and backwards. E.g. "racecar", or "0110110". The program determines if
a given input string is a palindrome or not. 
"""

def is_palindrome(s: str) -> bool:
	""" @description.
	Args: s (str): input string
	Returns: True if s is poalindromic. Otherwise, False.
	"""
	# input check
	if type(s) is not str: raise TypeError("s must be a string!")
	# 1. initialize the pointers
	i = 0
	j = len(s) - 1
	# 2. loop through the string ib both ways
	while (i < j):
		# 3. compare items at the pointers
		if s[i] != s[j]:
			return False
		# 4. increment i
		i = i + 1
		# 5. decrement j
		j = j - 1
	# 6. return an approrpiate boolean
	return True


if __name__ == "__main__":
	# set test string
	string = "0110110"
	check = is_palindrome(string)
	print(check)
