#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: vowel_count
description: count vowels and consonants in a string.
"""
import string
from typing import List

def count_vowels_and_consonants(string: str) -> List[int]:
	""" @description.
	Args: string (str): input string.
	Returns: vowel and consonant count.
	"""
	# 1. set counter and vowels
	vows = 0
	cons = 0
	vowels = "aeiou"
	# 2. loop through the string (remember character array)
	for i in range(0, len(string), 1):
		current_char = string[i]
		# 3. test the current char. is contained within vowels
		if current_char in vowels:
			vows = vows + 1
		else: cons = cons + 1
	# 4. count vowels and consonants likewise
	return vows, cons


if __name__ == "__main__":
	# test string
	string_ascii = string.ascii_letters
	# print(string_ascii)
	v, c = count_vowels_and_consonants(string_ascii)
	print("vowel count: {} \nconsonant count: {}".format(v, c))
