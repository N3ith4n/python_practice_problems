#Prog18: Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
 
#makes an empty list where all numbers from 0 to 100 will be placed
one_to_100 = []

#makes a loop that appends(inputs) numbers 0 to 100 to the empty list
for x in range(101):
    one_to_100.append(x)

#makes another empty list for all odd numbers this time
odd = []

#makes another loop that detects which numbers are odd in the 1st list
for i in one_to_100:
    if i %2 == 1:
        odd.append(i)

#prints the list with all the odd numbers
print(odd)
