# # Ques 1. Write a Python program that defines a function to display a welcome message for a user. 
# # The program should take the user's name as input and print a welcome message in the format: Welcome, <name>!

# def welcome_message(name):
#     return f"Welcome, {name}!"

# #Ques 2. Muitiplication Table Function:  Write a Python program that defines a function 
# # to print the multiplication table of a given number up to 10. The program should take an
# # integer as input and display its multiplication table in the standard format.

# def print_table(n):
#     for i in range(1, 11):
#         print(f"{n * i}")

# #Ques 3. Inner Function Multiply & Square:
# # Write a Python program that defines a function containing an inner function to perform two tasks: 
# # Multiply two numbers. Square the result of that multiplication. The program should take
# # two integers as input and print the square of their product.

# def multiply_and_square(a, b):
#     def inner_mult():
#         return a * b
    
#     result = inner_mult() ** 2
#     print(result)


# #Ques 4. Armstrong Number Function:
# # Write a Python program that defines a function to check whether a given number is an
# # Armstrong number or not. An Armstrong number (also called a narcissistic number) is a
# # number that is equal to the sum of its own digits each raised to the power of the number
# # of digits. Example: 153 -> 13 + 53 + 33 = 153> Armstrong Number

# def check_armstrong(n):
#     num_str = str(n)
#     num_digits = len(num_str)
#     total = sum(int(digit) ** num_digits for digit in num_str)
    
#     if total == n:
#         print("Armstrong Number")
#     else:
#         print("Not Armstrong Number")

# #Ques 5. Inverted Triangle Pattern Function:
# # Write a Python program that prints an inverted right-angled triangle pattern using asterisks (*). 
# # The program should take an integer n as input, representing the number of rows, and
# # print the pattern accordingly. For example, if n = 5, the pattern will look like this:
# # *****
# # **** 
# # ***
# # **
# # *

# def inverted_triangle(n):
#     for i in range(n, 0, -1):
#         print("*" * i)

# #Ques 6. Longest Consecutive Sequence:
# # Write a Python program that finds the length of the longest consecutive sequence in a list of integers. 
# # A consecutive sequence means numbers that appear in continuous order (for example, [1, 2, 3, 4]). The elements may appear
# # unsorted in the input list, but you need to find the maximum streak of consecutive numbers.For example, 
# # Given [100, 4, 200, 1, 3, 2], the longest consecutive sequence is [1, 2, 3, 4], so the output should be 4.

# def longest_consecutive(nums):
#     if not nums:
#         return 0
        
#     num_set = set(nums)
#     max_len = 0
    
#     for n in num_set:
#         # Check if it's the start of a sequence
#         if (n - 1) not in num_set:
#             current_num = n
#             current_len = 1
            
#             while (current_num + 1) in num_set:
#                 current_num += 1
#                 current_len += 1
                
#             max_len = max(max_len, current_len)
            
#     return max_len