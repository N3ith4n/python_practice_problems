#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
 
#makes an empty list where all numbers from 0 to 100 will be placed
one_to_100 = []
 
#makes a loop that appends(inputs) numbers 0 to 100 to the empty list
for x in range(101):
    one_to_100.append(x)

#makes another empty list where all numbers without 0 will be placed
numbers_without_zero = []

#makes another loop that detects which numbers have zero and appends them to the second list
for a in one_to_100:
    if a %10 != 0:
        numbers_without_zero.append(a)

#prints the second list
print(numbers_without_zero)
