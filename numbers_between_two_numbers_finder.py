#Prog20: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
 
#Asks the user for the two numbers and directly converts it into an integer
n1 = int(input("Give two more numbers = "))
n2 = int(input("Last one = "))

#makes an empty list where all the numbers between n1 and n2 will be placed
in_between = []

#makes a loop that gets the numbers between n1 and n2 and appends it to the empty list
for b in range(n1 + 1, n2):
    in_between.append(b)

#prints the list
print(in_between)
