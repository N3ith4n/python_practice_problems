#Prog25: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function

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

#sorts the list from the lowest to the highest
numbers.sort()

#prints the organized list
print(f"Here is the organized list = {numbers}")
