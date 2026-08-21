# While loop Practice Questions:-

# Ques 1. Print Each Digit (Reverse Order)
#  Break a number into individual digits and print them starting from the last digit.

# a = int(input("please tell your number: "))

# while a > 0:
#     print(a % 10)
#     a = a //10
    
# Ques 2. Sum of Digits
#  Add all the digits of a number (e.g., 123 -> 1+2+3 = 6).

# a = int(input("please tell your number: "))

# sum = 0
# while a > 0:
#     sum+= a%10 #sum = sum +a%10
#     a = a //10

# print(f"Your digits sum is {s}")

#Ques 3. Reverse a Number
# Input a number and reverse its digits (e.g., 123 -> 321).

# a = int(input("please tell your number: "))

# rev = 0
# while a > 0:
#     rev = rev*10 + a%10
#     a = a //10
# print(f"Your number reverse is {rev}")

#Ques 4. Palindrome Number Check
# Check if a number reads the same forward and backward (e.g., 121, 1331).

# a = int(input("please tell your number: "))
# copy = a
# rev = 0

# while a > 0:
#     rev = rev*10 + a%10
#     a = a //10

# if rev == copy:
#     print("Yes youor number is a pallindrome")
# else:
#     print("Sorry your number is not pallindrome")

# Ques 5. Automorphic Number
# A number is automorphic if its square ends with the number itself (e.g., 52 = 25, 762 = 5776)
# Check and print result.

a = int(input("please tell your number: "))
copy = a
square = a **2

count = 0

while a > 0:
    count = count +1
    a = a //10

extract = square % (10**count)

if extract == copy:
    print("Your number is automorphic number")
else:
    print("Sorry not an automorphic number")