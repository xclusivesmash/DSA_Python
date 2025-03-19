#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: anagrams
description: check if two words are anagrams.
definition: anagram is a word constructed by using the letters of another.
e.g. "rescue" and "secure"
"""

def anagrams_check(first: str, second: str) -> bool:
	""" @description.
	Args:
		first (str): first word.
		second (str): second word.
	Returns: True if @second can be constructed using letters of @first.
	"""
	# 1. check if the words are of the same length
	if len(first) != len(second):
		# if not, return False: fail case !
		return False
	else:
		# 2. loop through the first word
		i = 0
		check = False
		while (i < len(first)):
			# 3. check if the occurance of the second word chars. is
			# contained within the first word.
			chars = second[i]
			if chars in first:
				check = True
			# if not: return False
				# once check is false, return False:
				# else keep checking.
			else:
				check = False
				return check
			i = i + 1
	return check


if __name__ == "__main__":
	# test variables
	one = "secure"
	two = "rescue"
	checker = anagrams_check(one, two)
	print(checker)
