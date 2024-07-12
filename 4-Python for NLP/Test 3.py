# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:59:13 2024

@author: Test_3
"""

#write a python function which takes the two lists
def have_common_element(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6, 7]
print(have_common_element(list1, list2))  # Output: True

list3 = ['a', 'b', 'c']
list4 = ['d', 'e', 'f']
print(have_common_element(list3, list4))  # Output: False

#######################################################################

#Write a Python program to reverse a string.

str='Mansi'
print("Original String is:",str)
print("Reversed String",str[::-1])

######################################################################

#Write a Python program to iterate over dictionaries using for loops.

# Example dictionary
_dict1 = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York',
    'occupation': 'Engineer'
}

# Iterating over keys
print("Iterating over keys:")
for key in _dict1:
    print(key)

# Iterating over values
print("\nIterating over values:")
for value in _dict1.values():
    print(value)

# Iterating over key-value pairs
print("\nIterating over key-value pairs:")
for key, value in _dict1.items():
    print(f"{key}: {value}")

# Iterating over keys and accessing values
print("\nIterating over keys and accessing their values:")
for key in _dict1:
    print(f"{key}: {_dict1[key]}")
#########################################################################

#Using dict comprehension and a conditional argument create 
#a dictionary from the current dictionary where only the key:value pairs 
#with value above 2000 are taken to the new dictionary.

# Example dictionary
current_dict = {
    'item1': 1050,
    'item2': 2005,
    'item3': 3050,
    'item4': 2500,
    'item5': 7500
}

# Using dict comprehension to filter items with value > 2000
filtered_dict = {k: v for k, v in current_dict.items() if v > 2000}

print("Filtered Dictionary:", filtered_dict)

#Filtered Dictionary: {'item2': 2005, 'item3': 3050, 'item4': 2500, 'item5': 7500}


##########################################################################

#open the file data.txt using file operations.

# Open the file data.txt and read its content
import pandas as pd

technologies={
    "Courses":["Spark","Pandas","Hadoop"],
    "Fees":[20000,30000,40000],
    "Duration":["30 Days","30 Days","30 Days"],
    "Discount":[10,11,12]
    }

df=pd.DataFrame(technologies)
df
#convert DataFrame into the csv file
df.to_txt("data_file.txt")
#to create DataFrmae from 
df=pd.read_txt("data_file.txt")
df

#############################################################################33

#Define a array ,data = array([11, 22, 33, 44, 55]) find 0 th index 4 th index data

import numpy as np

# Define the array
data = np.array([11, 22, 33, 44, 55])

# Access 0th and 4th indices
zero_index = data[0]
fourth_index = data[4]

print("0th Index:", zero_index)
print("4th Index:", fourth_index)

#############################################################################

#Write a Python program to filter a list of integers using Lambda. 
#Original list of integers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] Even numbers 
#from the said list: [2, 4, 6, 8, 10] Odd numbers from the said list: [1, 3, 5, 7, 9]

# Original list of integers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda to filter even and odd numbers
even_numbers = list(filter(lambda x: x % 2 == 0, original_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))

print("Even numbers from the list:", even_numbers)
print("Odd numbers from the list:", odd_numbers)

######################################################################################

#Write a Pandas program to create the specified columns and rows from a given data frame.
"""name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh'] 
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19] 
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1] 
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'] 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


"""
import pandas as pd
import numpy as np

# Define the data
data = {
    'name': ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Create the DataFrame
df = pd.DataFrame(data, index=labels)

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Specify the columns to select
columns_to_select = ['name', 'score']

# Specify the rows to select
rows_to_select = ['a', 'c', 'e', 'g']

# Create the new DataFrame with specified columns and rows
new_df = df.loc[rows_to_select, columns_to_select]

# Display the new DataFrame
print("\nSelected Columns and Rows DataFrame:")
print(new_df)

##################################################################

#Define a array data = array([11, 22, 33, 44, 55]) and slice it from 1 to 4

import numpy as np

# Define the array
data = np.array([11, 22, 33, 44, 55])

# Slice the array from index 1 to 4
sliced_data = data[1:4]

# Print the sliced array
print("Sliced array:", sliced_data)

#######################################################################

#Write a NumPy program to test if any of the elements of a given array are non-zero. 

import numpy as np

# Sample array
arr = np.array([0, 0, 1, 0, 0])

# Test if any of the elements are non-zero
result = np.any(arr)

# Print the result
print("Is there any non-zero element in the array?", result)

###############################################################################

#Write a Python program to plot two or more lines and set the line markers.

import matplotlib.pyplot as plt

# Sample data
languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 23.7, 8.8, 8, 7.7, 6.7]

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(languages, popularity, color=['blue', 'orange', 'green', 'red', 'purple', 'brown'])

# Add title and labels
plt.title('Popularity of Programming Languages')
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')

# Show the bar chart
plt.show()

######################################################################

#to display the marker

import matplotlib.pyplot as plt

# Data
x = [1, 4, 5, 6, 7]
y = [2, 6, 3, 6, 3]

# Plot
plt.plot(x, y, 'r:', marker='o', markerfacecolor='blue', markersize=15)

# Labels and title
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Display marker')

# Show plot
plt.show()


