#Prog16: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
 
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

#The program substracts all ten numbers then prints the difference
difference2 = n1 - (n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10)
print(difference2)


