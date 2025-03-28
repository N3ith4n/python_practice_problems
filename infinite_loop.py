#Prog23: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

#makes an empty list where the unique numbers will be placed, this will be used as the basis of the loop
numbers = []

#makes a loop that will continue to ask the user a number until the inputted value is not a number
try:
    while True:
        num = int(input("Give me a number = "))
        if num not in numbers:
            print("Unique")
            numbers.append(num)
            print(numbers)
        elif num in numbers:
            print("Duplicate")
except ValueError:
    print("Invalid!")
