#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: naive_pattern
description: implements the naive pattern searching algorithm.
"""
from typing import List

def naive_pattern(string: str, pattern: str) -> int | List[int]:
	""" @description.
	Args:
		string (str): main string.
		pattern (str): sequence of chars. to search for in @string.
	Returns:
		index in @string indicating pattern starting point. Otherwise, -1.
	"""
	# 1. create an empty array to store indices.
	save = []
	i = 0
	# 2. loop through the main string.
	while i <= (len(string) - len(pattern)):
		j = 0
		# 3. loop through the substring
		while j < len(pattern):
			if pattern[j] != string[i + j]:
				# pattern not recognized
				break
			j = j + 1
		if j == len(pattern):
			# indices found saved.
			save.append(i)
		i = i + 1
	# 4. handle return values.
	if len(save) == 0: return -1
	return save


if __name__ == "__main__":
	# define test string
	s = "abbcabcabbbccabc"
	part = "abc"
	ls = naive_pattern(s, part)
	if type(ls) is list:
		print(s[ls[0]:ls[0]+len(part)], s[ls[1]:ls[1]+len(part)])
	else: print(ls) # meaning ls is an integer (-1)
