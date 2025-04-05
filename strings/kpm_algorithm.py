#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: kmp_algorithm
description: implements the kpm_algorithm.
"""
from typing import List

def lps_table(string: str) -> List[int]:
	""" creates an LPS table for the kmp algorithm.
	Args: string (str): input pattern for which to create a table.
	Returns: list representation of the lps table.
	"""
	# create an empty table (list in this case)
	table = [0]*len(string)
	i = 1
	length = 0
	while i < len(string):
		if string[i] == string[length]:
			length = length + 1
			table[i] = length
			i = i + 1
		else: # not a match
			if length != 0: length = table[length - 1]
			else:
				table[i] = 0
				i = i + 1
	# return the necessary table.
	return table


def KMP_algorithm(string: str, pattern: str) -> int:
	""" @description.
	Args:
		string (str): main string from which to search.
		pattern (str): pattern to look for in @string.
	Returns: Index of the start of pattern. Otherwise, -1.
	"""
	table = lps_table(pattern)
	xx = 0 # track the table indices.
	for x in range(0, len(string), 1):
		# compare the values at respective indices.
		if string[x] == pattern[xx]:
			xx = xx + 1
			# check for stoping condition if pattern found.
			if xx == len(table) and pattern[xx - 1] == string[x]:
				# return starting index for pattern.
				return (x - len(pattern) + 1)
		else:
			# change the xx value from lps table.
			xx = table[xx]
	return -1


if __name__ == "__main__":
	# define test string and pattern
	pat = "hhj"
	mystring = "dabcabdabcabc"
	index = KMP_algorithm(mystring, pat)
	print("starts at {}: {}".format(index, mystring[index:index+len(pat)]))
