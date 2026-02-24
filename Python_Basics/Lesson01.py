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