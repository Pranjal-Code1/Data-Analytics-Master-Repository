# For Loops Practice Questions:-

# Ques 1. Print "Hello World" n Times
# Use a loop to repeat a print statement ( "Hello World" ) based on user input count n

# a = "Hello World"
# ran = int(input("please tell me how many times you want to print :- "))
# for i in range(ran):
#     print(a)

# Ques 2. Print Numbers from 1 to n
# Display numbers in increasing order from 1 up to a given number n .

# n = int(input("Enter your number: "))
# for i in range(1,n+1):
#     print(i)

# Ques 3. Print Numbers from n to 1
# Display numbers in decreasing order from n down to 1.

# n = int(input("Enter your number: "))
# for i in range(n,0,-1):
#     print(i)

# Ques 4.Sum of Natural Numbers (1 to n)
# Take input n and calculate the total sum from 1 to n

# n = int(input("Enter your number: "))
# sum = 0
# for i in range(1,n+1,1):
#     sum+=i
#     # print(sum)

# print(sum)

# Ques 5. Factorial of a Number
# Calculate the factorial ( n! ) using a loop - multiplying numbers from 1 to n

# n = int(input("Enter your number: "))
# fac = 1
# for i in range(1,n+1,1):
#     fac*=i

# print(fac)

# Ques 6. Sum of Even & Odd Numbers in Range
# From 1 to n, find and print the sum of all even and all odd numbers separately.

# n = int(input("Enter your number: "))

# odd = 0
# even = 0

# for i in range(1,n+1,1):
#     if i%2 ==0:
#         even+=i
#     else:
#         odd+=i

# print(f"Sum of even number: {even}")
# print(f"Sum of odd number: {odd}")

# Ques 7. Print All Factors of a Number
# Display all numbers that divide the input number exactly (no remainder).

# n = int(input("Enter your number: "))

# for i in range(1,n+1,1):
#     if n%i ==0:
#         print(i)

# Ques 8. Sum of All Factors
# Add up all the factors found in the previous question (excluding or including
# - your choice).

# n = int(input("Enter your number: "))

# facSum = 0
# for i in range(1,n+1,1):
#     if n%i ==0:
#         facSum+=i

# print(f"Sum of All Factors: {facSum}")

# Ques 9. Power Calculation(a^b)
# Input base a and exponent b, and calculate the result using a loop (without using **).

# a = int(input("Enter your number: "))
# b = int(input("Enter your exponent: "))
# power = a
# for i in range(b-1):
#     power = power*a
# print(power)

# Ques 10. Prime number check
# Accept a number and check if it is divisible only by 1 and itself(i.e.,prime or not).

num = int(input("Enter your number: "))

for i in range(1,num+1):
    if num%1 ==0 and num%num ==0:
        print(f"{num} is a prime number.")
        break
    else:
        print(f"{num} is not a prime number.")