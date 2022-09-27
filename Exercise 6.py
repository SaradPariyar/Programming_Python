# Problem 1
# Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.
import random
def dice_Roll():
    return random.randint(1,6)
numb = dice_Roll()
while numb != 6:
    print(numb)
    numb = dice_Roll()
print(numb)

# Problem 2
# Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified
# function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the
# dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked
# from the user at the beginning.
import random
def dice_Roll(sides):
    return random.randint(1,sides)
num_sides = int(input("How many sides the dice has? "))
numb = dice_Roll(num_sides)
while numb != num_sides:
    print(numb)
    numb = dice_Roll(num_sides)
print(num_sides)

# Problem 3
# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative value.
def gallon_Ltr(gallons):
    return gallons * 3.785
print("Input negative number to exit")
num_Gallon = float(input("How many gallons? "))
while num_Gallon >= 0:
    print(f"Equal to {gallon_Ltr(num_Gallon):.4f} litters")
    num_Gallon = float(input("How many gallons? "))

# Problem 4
# Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in
# the list. For testing, write a main program where you create a list, call the function, and print out the value it returned.

def sum_list(int_list):
    sumResult = 0
    for i in int_list:
        sumResult += i
    return sumResult
list_pd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of a list is: ",sum_list(list_pd))

# Problem 5
# Write a function that gets a list of integers as a parameter. The function returns a second list that is
# otherwise the same as the original list except that all uneven numbers have been removed. For testing, write a main
# program where you create a list, call the function, and then print out both the original as well as the cut-down list.
def return_list(int_list):
    new_list = []
    for i in int_list:
        if i % 2 == 0:
            new_list.append(i)
    print("Old list: ", int_list)
    print("New list: ", new_list)
list_pd = [1,2,3,4,5,6,7,8,9,10]
return_list(list_pd)

# Problem 6
# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of
# the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program
# asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for
# money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.
import math
def Pizza_pr_cal(diameter, price,name):
    area_Pizza = math.pi * diameter/2 * diameter/2
    print("The price per square meter of pizza",name,f": {price / (area_Pizza * 0.0001):.3f}")
    return price / (area_Pizza * 0.0001)
diam1 = float(input("Input the diameter of pizza 1 in cm: "))
price1 = float(input("Input the price of pizza 1 in euro: "))
diam2 = float(input("Input the diameter of pizza 2 in cm: "))
price2 = float(input("Input the price of pizza 2 in euro: "))
if Pizza_pr_cal(diam1,price1,1) < Pizza_pr_cal(diam2,price2,2):
    print("Pizza 1 is cheaper than pizza 2")
elif Pizza_pr_cal(diam1,price1,1) > Pizza_pr_cal(diam2,price2,2):
    print("Pizza 2 is cheaper than pizza 1")
else:
    print("Same price")