#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: chars_occurences
description: remove all occurences of a character in string
"""

def remove_occurences(string: str, charToRemove: str) -> str:
	""" @description.
	Args:
		string (str): string to check the occurence of @charToRemove.
		charToRemove (str): character to remove.
	Returns: @string without charToRemove.
	"""
	# Method
	# create an empty string
	temp = ""
	# loop through @string
	for char in string:
		# for each char in string, make sure it is not charToRemove
		# and append it to the empty string
		if char != charToRemove:
			temp += char
	# return string without charToRemove.
	string = temp
	return string


if __name__ == "__main__":
	# test string
	myString = "Hellow my good code!"
	charToRemove = "o"
	new = remove_occurences(myString, charToRemove)
	print("Old string: {}\nNew String: {}".format(myString, new))
