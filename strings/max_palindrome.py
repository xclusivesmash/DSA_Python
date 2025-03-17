#!/usr/bin/env python3
"""
author: Siphamandla Matshiane
module: max_palindrome
description: the maximum palindrome obtained from a product of 2 digit numbers is
9009. The number include 91 and 99. Find the maximum palindrome from a product of
3-digit numbers.
"""
from typing import List

def is_palindromic(number: int) -> bool:
    """ @description.
    Args: number (int): input number to check
    Returns: True is number is palindromic. Otherwise, False.
    """
    or_number = str(number)
    check = False
    if or_number == or_number[::-1]:
        check = True
    return check

def max_palindrome(numOfDigits: int) -> List[int]:
    """ @description.
    Args: numsOfDigits (int): number of digits.
    Returns: numbers based on @numsOfDigits.
    """
    # 1=> 1 - 9
    # 2=> 10 - 99
    # 3=> 100 - 999
    start = 10**(numOfDigits - 1)
    ending = 10**(numOfDigits)
    # set initial maximum to zero
    maximum = 0
    p1 = 0
    p2 = 0
    for i in range(start, ending, 1):
        for ii in range(start, ending, 1):
            product = i * ii
            # check if product is palindromic
            check = is_palindromic(product)
            if check and product > maximum:
                maximum = product
                # set operands
                p1 = i
                p2 = ii
    return maximum, p1, p2

if __name__ == "__main__":
    # test values : answer = 913 * 993 = 906609
    numsOfDigits = 3
    palindrome, x, xx = max_palindrome(numsOfDigits)
    print(palindrome, x, xx)
