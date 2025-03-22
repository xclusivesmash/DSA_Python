#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: whitespace
description: removes all whitespaces from a string.
"""

def white_space(string: str) -> str:
	""" @description.
	Args: string (str): input string from which to remove whitespaces.
	Returns: new string without whitespaces.
	"""
	# 1. create an empty string
	temp = ""
	# 2. loop through the string
	for chars in string:
		# if character == "": skip
		if chars == " " or chars == '\t': continue
		else: temp = temp + chars
		# otherwise: append it to the empty created string
	# 3. return the newly created string
	string = temp
	return string


if __name__ == "__main__":
	# define test string
	mystring = "hey there\t\t mate"
	expected_output = "heytheremate"
	output = white_space(mystring)
	print(output)
