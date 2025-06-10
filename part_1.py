# 1. Return the Sum of Two Numbers
# Create a function that takes two numbers as arguments and returns their sum.
def addition(num1,num2):
    return num1 + num2

print(addition(7,3))
# 2. Return the Next Number from the Integer Passed
# Create a function that takes a number as an argument, increments the number by +1 and returns the result.
def increment(num1):
    return num1 + 1

print(increment(-3))
# 3. Convert Minutes into Seconds
# Write a function that takes an integer minutes and converts it to seconds.
def convert(minutes):
    seconds = 60
    return minutes * seconds

print(convert(2))

def convert(minutes):
    seconds = 0
    seconds = minutes * 60
    return seconds

print(convert(5))
# 4. Area of a Triangle
# Write a function that takes the base and height of a triangle and return its area.
# The area of a triangle is: (base * height) / 2
def tri_area(base,height):
    area = (base * height) / 2
    return area

print(tri_area(10,10))
# 5. Calculating cube numbers
# Write a function that takes an integer and calculating cube
def cube_nums(num):
    cube = num * num * num
    return cube

print(cube_nums(10))

def cube_nums(num):
    cube = num ** 3
    return cube

print(cube_nums(3))
# 6. Convert Hours into Seconds
# Write a function that converts hours into seconds.
def get_seconds(hours):
    seconds = 60
    minutes = 60
    return (seconds * minutes) * hours

print(get_seconds(24))
# 7. Maximum Edge of a Triangle
# Create a function that finds the maximum range of a triangle's third edge, where the side lengths are all integers.
# (side1 + side2) - 1 = maximum range of third edge.
# The side lengths of the triangle are positive integers.
def next_edge(side1,side2):
    if side1 > 0 and side2 > 0:
        if type(side1) == int and type(side2) == int:
            max_edge = (side1 + side2) - 1
            return max_edge
        else:
            return "Side lengths must be integers"
    else:
        return "Side lengths must be positive integers"
    
print(next_edge(9.5,2))
# 8. Return the Remainder from Two Numbers
# There is a single operator in Python, capable of providing the remainder of a division
# operation. Two numbers are passed as parameters. The first parameter divided by the
# second parameter will have a remainder, possibly zero. Return that value.
# The tests only use positive integers.
def remainder(num1,num2):
    if num1 > 0 and num2 > 0:
        return num1 % num2
    else:
        return "Only use positive integers "
print(remainder(0,2))
# 9. Return a String as an Integer
# Create a function that takes a string and returns it as an integer.
# All numbers will be whole.All numbers will be positive.
def string_to_int(txt):
    integer = int(txt)
    return integer
        
print(string_to_int("12232442"))

def string_to_int(txt):
    try:
        integer = int(txt)
        return integer
    except:
        return "Only integer and positive numbers are allowed"
        
print(string_to_int("12454654652"))
# 10. Convert Age to Days
# Create a function that takes the age in years and returns the age in days.
# Use 365 days as the length of a year for this challenge.
# Ignore leap years and days between last birthday and now.
# Expect only positive integer inputs.

def calc_age(age):
    days = 365
    if age >= 0 and type(age) == int:
        return days * age
    else:
        return "Expect only positive integer inputs"

print(calc_age(57))





