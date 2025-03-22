#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: uppercase
description: converts string to uppercase
"""
import string

def uppercase(mystring: str) -> str:
	""" @description.
	Args: string (str): input string
	Returns: uppercase version of @string without .upper method.
	"""
	# diff. btw. uppercase and lowercase is 32 (based on ascii table)
	# loop through string and move each char. 32 steps.
	# then convert to char using chr (from ord(number))
	toremove = string.punctuation
	empty = "".join(chr(ord(chars) - 32) for chars in mystring if ord(chars) >= 32 and chars not in toremove)
	return empty


if __name__ == "__main__":
	# define test string
	mystring = "in god we trust. anything else we test ~ engineers"
	upperString = uppercase(mystring)
	print(upperString)
