#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: frequency
description: count frequency of each character.
"""

def frequency(string: str) -> dict:
	""" @description.
	Args: string (str): input string.
	Returns: dictionary with a count for each character.
	"""
	# METHOD.
	# 1. create an empty dictionary
	my_dict = {}
	# 2. loop throught the string
	for char in string:
		# 3. count the occurence of each char.
		if char not in my_dict:
			# 4. store the char. along with its occurence.
			my_dict[char] = 1
		else: my_dict[char] += 1
		# note, the same could have been achieved through the following:
		# my_dict[char] = 1 if char not in my_dict else my_dict[char] += 1
	# 5. return the dictionary
	return my_dict


if __name__ == "__main__":
	# define test string
	myString = "In God we trust. Everything else we test ~ engineers"
	dictionary = frequency(myString)
	print(dictionary)
