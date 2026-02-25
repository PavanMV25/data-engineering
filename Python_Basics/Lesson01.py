#Write a Python function that accepts two numbers. If their product is less than or equal to 1000, 
# return the product; otherwise, return their sum.
"""
def check(a,b):
    if a*b <= 1000:
    	return (a*b)
    else:
        return (a+b)

a = int(input("Enter the first number "))
b = int(input("Enter the second number "))
print(check(a,b)) 
"""
#Take an integer input from the user and print whether it is an even or an odd number.

"""
def check(a):
    if a%2 == 0:
        return "Its an even number"
    else:
        return "Its an odd number"

a = int(input("Enter the first number "))
print(check(a))
"""

#Write a function to sum all numbers in a given list, such as (8, 2, 3, 0, 7).
"""
def check(a):
	b = 0
	for i in a:
		b = b + i
	return b

a = [1,2,3,4]

print(check(a))

"""

# Prime Number Check: Create a function to check if a given number is a prime number.
"""
def check(a):
    if a%2 == 1 or a%3 == 1 or a%5 == 1 or a%7 == 1:
        print("Its a Prime Number")
    else:
        print("Its not a Prime Number")

a = int(input("Enter the number: "))
check(a)       

"""

# Iterate through the first 10 numbers (0–9). In each iteration, print the current number and the previous number.

"""
b = 0
for i in range(10):
    print(i)
    print(b)
    b = i
"""
# Display only those characters which are present at an even index number in given string.

"""
a = input("Provide the Name: ")

for i in a[0: : 2]:
    print(i)
"""

# Write a function to remove characters from a string starting from index 0 up to n and return a new string.
"""
a = input("Provide the Name: ")
n = int(input("Give the number of strings to be removed: "))
b = a[n:]
print(b)    

"""

# Write a program to swap the values of two variables, a and b, without using a third temporary variable.
"""
a = 5
b = 10
print(a,b)
a,b = b,a
print(a,b)
"""

# Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

"""
a = 5
b = 1
for i in range(1,a+1):
    b = i*b

print(b)

"""

# Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Expected ['apple', 'cherry', 'date', 'elderberry', 'fig']

fruits.pop(1)
fruits.append("fig")
print(fruits)