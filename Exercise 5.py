# Problem 1
# Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
import random
Dice_num = int(input("How many dice to roll? "))
sum_Roll = 0
for i in range (Dice_num):
    sum_Roll += random.randint(1,6)
print("Sum of all dices is: ", sum_Roll)

# Problem 2
# Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
print("Please input at least 5 numbers !!!")
list_Num = []
num = input("Input a number: ")
while num != "":
    list_Num.append(int(num))
    num = input("Input a number: ")
list_Num.sort(reverse=True)
print("The first 5 greatest numbers are:")
for i in range (5):
    print(list_Num[i], end=" ")

# Problem 3
# Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# For example, number 13 is a prime number as can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.
print("")
num = int(input("Input an integer number: "))
half_Num = num // 2
divisible = False
for i in range (2, half_Num+1):
    if num % i == 0:
        divisible = True
        break
if divisible == False:
    print("This is a prime number")
else:
    print("This is not a prime number")

# Problem 4
# Write a program that asks the user to enter the names of five cities one by one (use a for loop for reading
# the names) and stores them into a list structure. Finally, the program prints out the names of the cities one by one,
# one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.
list_City = []
print("Please enter the name of 5 cities")
for i in range(5):
    list_City.append(input("Name of a city: "))
for i in range(5):
    print(list_City[i])