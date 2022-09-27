#Problem 1
# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish back
# into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
size_lm = 42
zander_ln = float(input("Input the length of the zander: "))
if zander_ln < size_lm:
    below_lm = size_lm - zander_ln
    print("A zander must be 42 centimeters or longer")
    print("This fish is smaller than the size limit by ", below_lm, "cm")
    print("It must be returned to the lake")
else:
    print("This fish meets the size requirement.")

# Problem 2
# Write a program that asks the user to enter the cabin class of a cruise ship and then prints out
# a written description according to the list below. You must use an if/elif/else structure in your solution.
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class
cabin_class = input("Enter the cabin class (LUX, A, B, C): ")
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("Above the car deck, equipped with a window")
elif cabin_class == "B":
    print("Windowless cabin above the car deck")
elif cabin_class == "C":
    print("Windowless cabin below the car deck")
else:
    print("Invalid cabin class !!!")

# Problem 3
# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
gender = input("Are you male or female? ")
hmgValue = float(input("Input your hemoglobin value (g/l): "))
if gender == "male":
    if hmgValue < 134:
        print("Your hemoglobin value is low")
    elif hmgValue > 167:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")
else:
    if hmgValue < 117:
        print("Your hemoglobin value is low")
    elif hmgValue > 155:
        print("Your hemoglobin value is high")
    else:
        print("Your hemoglobin value is normal")

# Problem 4
# Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year")
else:
    print("This is not a leap year")