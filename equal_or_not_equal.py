#Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
#and
#Prog12: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.
 
#Asks the user for the two numbers
n1 = int(input("Give me some numbers, first one = "))
n2 = int(input("second one = "))
 
#The program that sees if the two numbers are equal or not and prints 'equal' or 'not equal'
if n1 == n2:
    print("The two numbers you gave are equal")
else:
    print("The two numbers you gave are not equal")
