#Prog21: Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
#and
#Prog26: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

#Asks the user for the ten numbers and directly converts it into an integer
n1 = int(input("Give me some numbers, first one = "))
n2 = int(input("second one = "))
n3 = int(input("third = "))
n4 = int(input("fourth = "))
n5 = int(input("fifth = "))
n6 = int(input("sixth = "))
n7 = int(input("seventh = "))
n8 = int(input("eight = "))
n9 = int(input("ninth = "))
n10 = int(input("tenth = "))

#a list where each all the inputted numbers will be placed
ten_numbers = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]

#empty lists where all the numbers with and without a duplicate will be seperately placed
unique = []
duplicates = []

#a loop that checks which numbers are a duplicate and which doesn't have a duplicate and appends it to the empty list
for x in ten_numbers:
    if x not in unique:
        unique.append(x)
    elif x in unique:
        unique.remove(x)
        duplicates.append(x)
            
#prints the lists
print(f"The numbers that don’t have duplicates are {unique}")
print(f"The numbers that have duplicates are {duplicates}")
