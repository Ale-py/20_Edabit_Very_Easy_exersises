# 11. Find the Perimeter of a Rectangle
# Create a function that takes length and width and finds the perimeter of a rectangle.
def find_perimeter(length,width):
    lens = length * 2
    wids = width * 2
    return lens + wids

print(find_perimeter(2,9))
# 12. Power Calculator
# Create a function that takes voltage and current and returns the calculated power.
def get_power(voltage,current):
    return voltage * current

print(get_power(480,20))
# 13. Sum of Polygon Angles
# Given an n-sided regular polygon n, return the total sum of internal angles (in degrees).
# n will always be greater than 2.The formula (n - 2) x 180
def sum_polygon(n):
    if n > 2:
        return (n - 2) * 180
    else:
        return "This is not a polygon"

print(sum_polygon(6))
# 14. To the Power of _____
# Create a function that takes a base number and an exponent number and returns the calculation.
# All test inputs will be positive integers.
def calculate_exponent(num,exp):
    return num ** exp
    
print(calculate_exponent(8,4))

def calculate_exponent(num,exp):
    if num > 0 and exp > 0:
        result = num * num
        for e in range(exp-1):
        
            result = num * result
        result = result / num    
        return int(result)
    else:
        return "All test inputs will be positive integers"

print(calculate_exponent(8,4))
# 15. Boolean to String Conversion
# Create a function that takes a boolean variable flag and returns it as a string.
def bool_to_string(flag):
    return f"\"{flag}\""

print(bool_to_string(False))
# 16. Return the First Element in a List
# Create a function that takes a list containing only numbers and return the first element.
def get_first_value(list):
    return list[0]

print(get_first_value([-500,0,50]))
# 17. Football Points
# Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
# wins get 3 points. draws get 1 point. losses get 0 points
# Inputs will be numbers greater than or equal to 0.
def football_points(wins,draws,losses):
    win_points = wins * 3
    draw_points = draws * 1
    if wins >= 0 and draws >= 0 and losses >= 0:
        return win_points + draw_points
    else:
        return "Inputs will be numbers greater than or equal to 0."
print(football_points(-1,0,2))
# 18. The Farm Problem
# In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:
# chickens = 2 legs , cows = 4 legs , pigs = 4 legs
# The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.
# The order of animals passed is animals(chickens, cows, pigs).
def animals(chickens,cows,pigs):
    chicken_legs = chickens * 2
    cow_legs = cows * 4
    pig_legs = pigs * 4
    total_legs = chicken_legs + cow_legs + pig_legs
    if chickens >= 0 and cows >= 0 and pigs >= 0:
        return total_legs
    else:
        return "Inputs will be numbers greater than or equal to 0."
print(animals(2,2,-2))
# 19. Basic Variable Assignment
# A student learning Python was trying to make a function. His code should concatenate a
#  passed string name with string "Edabit" and store it in a variable called result. He needs your help to fix this code.
def name_string(name):
    s = "Edabit"
    result = name + s
    return result

print(name_string("python"))
# 20. Convert Hours and Minutes into Seconds
# Write a function that takes two integers (hours, minutes), converts them to seconds, and adds them.
def convert(hours,minutes):
    minutes_to_seconds = minutes * 60
    hours_to_minutes = hours * 60
    
    return (hours_to_minutes * 60) + minutes_to_seconds

print(convert(0,10))

