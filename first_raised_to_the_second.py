#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
 
#Asks the user for the two numbers and directly converts it into an integer
n1 = int(input("Give me some numbers, first one = "))
n2 = int(input("second one = "))

#The program gets the first number then raises the second number to get the result
exponent = n1 ** n2
print(exponent)
