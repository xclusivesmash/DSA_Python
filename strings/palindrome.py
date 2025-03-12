#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: palindrome
description: a palindrome reads the same both forwards
and backwards. E.g. "racecar", or "0110110". The program determines if
a given input string is a palindrome or not.
"""

def is_palindrome(s: str) -> bool:
	""" @description.
	Args: s (str): input string
	Returns: True if s is palindromic. Otherwise, False.
	"""
	# input check
	if type(s) is not str:
		raise TypeError("s must be a string!")
	# 1. reverse the string
	check = False # used for boolean check
	reversed_string = s[::-1]
	# 2. compare it against the unreversed
	if s == reversed_string:
		check = True
	# 3. return an approrpiate boolean
	return check


if __name__ == "__main__":
	# 4. set test string
	string = "0110110"
	decision = is_palindrome(string)
	print(decision)
