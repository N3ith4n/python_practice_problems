#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
#and
#Prog17: Create a program that ask user to input 10 numbers. Print how many are even numbers.
 
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
 
#The program detects the number of odd and even numbers using a loop
numbers = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10]
record = [int(item) for item in numbers]
odd = 0
even = 0

for x in record:
    if x %2 == 1:
        odd += 1
    elif x %2 == 0:
        even += 1

#Prints the total number of odd and even numbers
print(f"There are a total of {odd} odd numbers")
print(f"There are a total of {even} odd numbers")
