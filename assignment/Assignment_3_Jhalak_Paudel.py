## Question 01

# Create a function to calculate the area of a Rectangle.

"""
Input: l as length and b as breadth
Output: Area in the basis of l and b
"""

def area_rectangle(length, breadth):
    return length * breadth
length = 20
breadth = 20
area = area_rectangle(length, breadth)
print(area)

## Question 02
"""
Write a function in order to simulate the equation of the straight line.Take slope of the line and the y - intercept as inputs and then
Compute the value of y for any value of x that the user enters.Input: Slope, Intercept, X
Output: y for the above values using y = slope * X  + intercept
"""
def equation_of_straight_line(slope, intercept, x):
    return slope * x + intercept

y = equation_of_straight_line(5, 4,  2 )
print(y)

## Question 03

# Write a function in order to convert the temperature from Celsius scale to the Fahrenheit Scale.Please
# use the internet in order to find the corresponding formulae.
"""
Input: Temperature in the
Celsius
Scale.
Output: Temperature in Fahrenheit
Scale
"""
def temperature_in_fahrenheit(celcius):
    return celcius * 9 / 5 + 32, "degree fahrenheit"
celcius = temperature_in_fahrenheit(5)
print(celcius)

## Question 04
"""
Find the maximum difference between the two consecutive elements in a list.
You are given a list of integers.Write a Python program to find the maximum difference between two consecutive
elements in the list using a brute - force approach.The difference is defined as the absolute value of the
difference between two consecutive elements.
"""
# Input: Enter a List
# Output: Max difference between two consecutive elements
def max_difference(list1):
    differences = [abs(list1[i] - list1[i - 1]) for i in range(len(list1))]
    return max(differences)

list1 = [10, 11, 15, 3]
print(max_difference(list1))

def max_difference2(list1):
    dif = 0
    length = len(list1)
    for i in range(length-1):
        value = abs(list1[i] - list1[i+1])
        if value > dif:
            dif = value
    return dif
list1 = [10, 11, 15, 3]
print(max_difference2(list1))

"""
Example
 01:
 > Input: lst = [1, 7, 3, 10, 5]
 > Output: 7
 The maximum difference is between 3 and 10
(i.e., | 3 - 10 | = 7)`.

Example 02:
> Input: lst = [10, 11, 15, 3]
> Output: 12
 maximum difference is between 15 and 3
(i.e., | 15 - 3 | = 12)`.
"""
## Question 05

# You are given two integers n and m.Your task is to find the GCD of these two numbers.The GCD is the largest
# positive integer that divides both numbers without leaving a remainder.Do not use any built - in functions and do
# not use recursion.
# Input: Two integers n and m, where 1 <= n, m <= 10 ^ 9.
# Output: An integer representing the GCD of n and m.

def gcd(a, b):
    divisor = 1
    minimum = min(a, b)
    for i in range(2,minimum+1):
        if (i>divisor) and a%i==0 and b%i==0:
            divisor = i
    return divisor
a = 12
b = 24
print(gcd(a, b))

#chinese remainder theorem

import math
a=3
b=7
result = math.gcd(a, b)
print(result)

"""
# Example 1
# Input: n = 48, m = 18
# Output: 6

# Example 2
# Input: n = 56, m = 98
# Output: 14

"""
## Question 06
# You are given a positive integer num.Your task is to check whether num is a perfect square or not.A perfect
# square is an integer that is the square of an integer(e.g., 1, 4, 9).Return True if num is a perfect
# square, and False otherwise.


"""
# Example
Input: A single positive integer num where 1 <= num <= 10 ^ 9. Output: Return True if num is a perfect
square, otherwise return False.

Valid Square Input: num = 16 Output: True
Invalid Square Input: num = 14 
"""
import math
def perfect_square(num):
    perfect = math.sqrt(num)
    if perfect == int(perfect):
        return True
    else:
        return False
num = 14
print(perfect_square(num))


## Question 07
# Implement a function `linear_search` that performs a linear search on a list to find a given value.The
# function should return the index of the first occurrence of the value in the list, or -1 if the value is not found.
# ** Parameters: ** - `arr`: A list of elements(can be empty) - `target`: The value to search for in the list
# ** Return: ** - The index of the first occurrence of the target value(0 - based), or -1 if not found

def linear_search(num, target):
    for i in num:
        if i == target:
            return "is in the list"
    else:
        return "-1"
num = [1, 2, 3, 4, 5]
target = 0
print(linear_search(num, target))


#enuerator:
# array = [1, 2, 3, 4, 5]
# name = [2]
# for (index,value) in enumerate(array):
    # print(index, value)
    # if value == array[index]:
    #     Print True
    # else:
    #     Print "-1"



