# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 10:03:18 2024

@author: Hp
"""

"""
Write a python program to print all even numbers from a given list of
numbers in the same order and stop printing any after 237 in the sequence.
Sample numbers list:
numbers = [
 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,
328, 615, 953, 345,
 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866,
950, 626, 949, 687, 217,
 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,
843, 831, 445, 742, 717, 958,743, 527]"""

numbers = [
 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978,
328, 615, 953, 345,
 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866,
950, 626, 949, 687, 217,
 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379,
843, 831, 445, 742, 717, 958,743, 527]

for number in numbers:
    if number == 237:
        print(number)
        break
    if number % 2 == 0:
        print(number)

#-------------------------------------------------------------------

"""Write a python program to find a list of integers with exactly two
occurrences of nineteen and at least three occurrences of five. Return True
otherwise False.
e.g. Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
"""
def check_conditions(nums):
    count_nineteen = nums.count(19)
    count_five = nums.count(5)
    
    if count_nineteen == 2 and count_five >= 3:
        return True
    else:
        return False

# Test cases
nums1 = [19, 19, 15, 5, 3, 5, 5, 2]
nums2 = [19, 15, 15, 5, 3, 3, 5, 2]

print(check_conditions(nums1))  # Output: True
print(check_conditions(nums2))  # Output: False

#---------------------------------------------------------------
"""
Write a python program to find numbers that are greater than 10 and have
odd first and last digits.
e.g: Input:
[1, 3, 79, 10, 4, 1, 39, 62]
Output:
[79, 39]
Input:
[11, 31, 77, 93, 48, 1, 57]
Output:
[11, 31, 77, 93, 57]
"""

def odd_first_last_digits(numbers):
    result = []
    
    for num in numbers:
        if num > 10:
            num_str = str(num)
            first_digit = int(num_str[0])
            last_digit = int(num_str[-1])
            
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                result.append(num)
    
    return result

# Test cases
numbers1 = [1, 3, 79, 10, 4, 1, 39, 62]
numbers2 = [11, 31, 77, 93, 48, 1, 57]

print(odd_first_last_digits(numbers1))  # Output: [79, 39]
print(odd_first_last_digits(numbers2))  # Output: [11, 31, 77, 93, 57]

#--------------------------------------------------------------

"""
Q4. Write a python program to find the largest negative and smallest positive
numbers (or 0 if none).
e.g. Input:
[-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
Output:
[-6, 2]"""

def find_numbers(numbers):
    largest_negative = None
    smallest_positive = None
    
    for num in numbers:
        if num < 0:
            if largest_negative is None or num > largest_negative:
                largest_negative = num
        elif num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
    
    # Handle cases where no negative or positive numbers were found
    if largest_negative is None:
        largest_negative = 0
    if smallest_positive is None:
        smallest_positive = 0
    
    return [largest_negative, smallest_positive]

# Test case
numbers = [-12, -6, 300, -40, 2, 2, 3, 57, -50, -22, 12, 40, 9, 11, 18]
result = find_numbers(numbers)
print(result)  # Output: [-6, 2]

#---------------------------------------------------------------------
"""
Write a Python program that matches a string that has an a followed by
zero or more b's."""

import re

def match_pattern(s):
    pattern = r'^a(b*)$'
    if re.match(pattern,s):
        return True
    else:
        return False

# Test cases
print(match_pattern("ab"))      # True
print(match_pattern("abb"))     # True
print(match_pattern("a"))       # True
print(match_pattern("ac"))      # False
print(match_pattern("b"))       # False
print(match_pattern("abc"))     # False

