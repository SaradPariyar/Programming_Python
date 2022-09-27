
# Problem 1
# Write a program that asks your name and then greets you by your name.
name = input("What is your name? ")
print("Hello, " + name + "!")

# Problem 2
# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
import math
radius = float(input("Enter the radius of circle: "))
area = math.pi * radius**2
print(f"The area of this circle is: {area:.2f}")

# Problem 3
# Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = (length + width) * 2
area = length * width
print(f"The perimeter of this rectangle is: {perimeter:.2f}")
print(f"And the area of this rectangle is: {area:.2f}")

# Problem 4
# Write a program that asks the user for three integer numbers.
# The program prints out the sum, product, and average of the numbers.
n1 = int(input("Enter 1st integer number: "))
n2 = int(input("Enter 2nd integer number: "))
n3 = int(input("Enter 3rd integer number: "))
sum = n1 + n2 + n3
product = n1 * n2 * n3
average = float(sum) / 3
print("The sum of the numbers is:", sum)
print("The product of the numbers is:", product)
print(f"The average of the numbers is: {average:.2f}")

# Problem 5
# Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user
talent = float(input("Enter the mass in talents: "))
pound = float(input("Enter the mass in pounds: "))
lot = float(input("Enter the mass in lots: "))
mass = ((talent * 20 + pound) * 32 + lot) * 13.3
mass_kg = int(mass // 1000)
mass_gram = mass % 1000
print("The weight in modern units:", mass_kg, f"kilograms and {mass_gram:.2f} grams")

# Problem 6
# Write a program that draws two random combinations of numbers for a combination lock.
import random
# a 3-digit code where each number is between 0 and 9.
d1 = str(random.randint(0,9))
d2 = str(random.randint(0,9))
d3 = str(random.randint(0,9))
print("A 3-digit code where each number is between 0 and 9: " + d1 + d2 + d3)

# a 4-digit code where each number is between 1 and 6
d1 = str(random.randint(1,6))
d2 = str(random.randint(1,6))
d3 = str(random.randint(1,6))
d4 = str(random.randint(1,6))
print("A 4-digit code where each number is between 1 and 6: " + d1 + d2 + d3 + d4)