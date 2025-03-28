#Prog19: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
 
#makes an empty list where all numbers from 0 to 100 will be placed
one_to_100 = []

#makes a loop that appends(inputs) numbers 0 to 100 to the empty list
for x in range(101):
    one_to_100.append(x)

#makes another empty list where all numbers divisible by five(ending in zero or five) will be placed
numbers_not_divisible_by_five = []

#makes another loop that detects which numbers are divisible by five and appends them to the second list
for a in one_to_100:
    if a %5 != 0 and a %10 != 0: 
        numbers_not_divisible_by_five.append(a)

#prints the second list
print(numbers_not_divisible_by_five)
