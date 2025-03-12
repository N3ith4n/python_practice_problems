#Prog24: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number

#makes an empty list where the numbers will be placed, this will be used as the basis of the loop
numbers = []

#makes a loop that will continue to ask the user a number until the inputted value is not a number
try:
    while True:
        num = int(input("Give me a number = "))
        if num not in numbers:
            numbers.append(num)
            print(numbers) 
        elif num in numbers:
            numbers.append(num)
            print(numbers) 
except ValueError:
    print("Invalid!")

#finds the lowest number in the list
lowest = min(numbers)

#prints the lowest number in the list
print(f"The lowest number out of all the numbers you gave is {lowest}")
