#Prog11: Create a program that ask user to input 2 numbers. Print the smaller number.
 
#Asks the user for the two numbers and directly converts it into an integer
n1 = int(input("Give me some numbers, first one = "))
n2 = int(input("second one = "))

#The program that sees which one is the smaller number and prints it
if n1 <= n2:
    print(f"{n1} is the smaller number")
elif n2 <= n1:
    print(f"{n2} is the smaller number")

