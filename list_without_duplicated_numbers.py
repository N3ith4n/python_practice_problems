#Prog22: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

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

#empty lists where all the numbers required will be placed
except_duplicates = []

#a loop that appends the numbers from the list except the duplicates
for x in ten_numbers:
    if x not in except_duplicates:
        except_duplicates.append(x)

#prints the list
print(except_duplicates)
