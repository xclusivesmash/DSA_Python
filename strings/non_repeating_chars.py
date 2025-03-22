#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: non_repeating_chars
description: finds the first non-repeating char. in a string.
"""

def non_repeating(string: str) -> str:
	""" @description.
	Args: string (str): input string
	Returns: first non-repeating char in @string.
	"""
	# METHOD.
	# 1. remove all white spaces and string string.
	string = string.replace(" ", "").replace("\t", "")
	# 2. create an empty dictionary to store all chars and counts.
	myDict = {}
	# 3. loop through string
	for chars in string:
		# if char not in dict. store it and increment count
		myDict[chars] = myDict.get(chars, 1) if chars not in myDict else myDict[chars] + 1 
	# 4. check if value associated with key has one.
	non_repeating_key = None
	for key, value in myDict.items():
		if value == 1: 
			non_repeating_key = key
			break
		# if so, return the char (key) of dict.
	return myDict,  non_repeating_key


if __name__ == "__main__":
	# define test string
	mystring = "in god we trust. everything else we test ~ engineers"
	d, char = non_repeating(mystring)
	print(char)
	print(d)
