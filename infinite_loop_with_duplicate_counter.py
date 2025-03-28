#Prog27: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.

#makes an empty dictionary store all the inputted number by the user, it being a dictiionary is necessary to count how many duplicates a number has
numbers = {}

#makes a loop that will continue to ask the user a number until the inputted value is not a number and also has the function that counts the duplicates of a number
try:
    while True:
        num = int(input("Give me a number = "))

        if num in numbers:
            numbers[num] += 1
        else:
            numbers[num] = 1
    
except ValueError:
    print("Invalid!")

#finds the number with the most duplicates
most_duplicate_number = max(numbers, key=numbers.get)

#prints the number with the most duplicates
print(f"The number with the most duplicates is {most_duplicate_number}, which appears {numbers[most_duplicate_number]} times.")
