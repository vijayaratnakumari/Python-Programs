#Example 1: Using for loop

# Python program to count Even
# and Odd numbers in a List

# list of numbers
 list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

    # checking condition
    if num % 2 == 0:
        even_count += 1

    else:
        odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)


#Example 2: Using while loop

# Python program to count Even and Odd numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

even_count, odd_count = 0, 0
num = 0

# using while loop
while (len(list1) > num):

    # checking condition
    if list1[num] % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    # increment num
    num += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)



#Example 3 : Using Python Lambda Expressions

# list of numbers
   list1 = [10, 21, 4, 45, 66, 93, 11]

odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))

# we can also do len(list1) - odd_count
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)



#Example 4 : Using List Comprehension

# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

only_odd = [num for num in list1 if num % 2 == 1]
odd_count = len(only_odd)

print("Even numbers in the list: ", len(list1) - odd_count)
print("Odd numbers in the list: ", odd_count)
