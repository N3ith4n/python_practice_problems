#Prog14: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point
 
#Asks the user for the two numbers and directly converts it into an integer
n1 = int(input("Give me some numbers, first one = "))
n2 = int(input("second one = "))

#The program divides the two numbers and prints the quotient but without the decimal point
quotient = n1 // n2
print(quotient)
