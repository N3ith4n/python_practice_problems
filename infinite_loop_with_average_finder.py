#Prog30: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.

#makes an empty list where the numbers will be placed, this will be used as the basis of the loop and assigning a variable
numbers = []

#Initializes a variable to be used for solving the average later
total_number = 0

#makes a loop that will continue to ask the user a number until the inputted value is not a number and also adds 1 to a variable that will be used for the average later
try:
    while True:
        num = int(input("Give me a number = "))
        if num not in numbers:
            numbers.append(num)
            print(numbers) 
            total_number += 1
        elif num in numbers:
            numbers.append(num)
            print(numbers)
            total_number += 1
except ValueError:
    print("Invalid!")

#adds all the numbers inside the list
total = sum(numbers)

#gets the average
average = total / total_number

#prints the average
print(average)
