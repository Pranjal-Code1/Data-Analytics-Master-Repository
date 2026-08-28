# def replace_even_with_zero(lst):
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0:
#             lst[i] = 0
#     return lst


# def split_list_in_halves(numbers):
#     # Find the midpoint (if odd, the extra element goes to the first half using ceiling division or integer math)
#     mid = (len(numbers) + 1) // 2
    
#     first_half = numbers[:mid]
#     second_half = numbers[mid:]
    
#     # Print each half on a separate line as space-separated values
#     # print(*(first_half))
#     # print(*(second_half))
    
#     return first_half, second_half


# def swap_first_last_elements(numbers):
#     # Check if the list has at least 2 elements to swap
#     if len(numbers) >= 2:
#         # Swap the first element (index 0) with the last element (index -1)
#         numbers[0], numbers[-1] = numbers[-1], numbers[0]
        
#     # Print the result as space-separated values
#     # print(*(numbers))
#     return numbers


# def solve(input):
#     data = input.split()
    
#     # 1. Get the number of elements
#     n = int(data[0])
    
#     # 2. Extract the list elements using a normal loop
#     lst = []
#     for i in range(1, n + 1):
#         lst.append(int(data[i]))
        
#     # 3. Get the element to remove from the next position
#     x = int(data[n + 1])
    
#     # 4. Remove the first occurrence of x if it exists
#     if x in lst:
#         lst.remove(x)
        
#     # 5. Print elements separated by spaces
#     print(*(lst))


# def count_elements_above_average(numbers):
#     # Step 1: Turn items into numbers
#     nums = []
#     for x in numbers:
#         nums.append(float(x))
        
#     # Step 2: Find total sum
#     total_sum = 0
#     for num in nums:
#         total_sum = total_sum + num
        
#     # Step 3: Find average
#     avg = total_sum / len(nums)
    
#     # Step 4: Count elements above average
#     count = 0
#     for num in nums:
#         if num > avg:
#             count = count + 1
            
#     # Step 5: Return the count instead of printing
#     return count
    

# def find_all_sublists(lst):
#     # Step 1: Create an empty list to store all our sublists
#     sublists = []
    
#     # Step 2: Pick the starting point of the sublist
#     for i in range(len(lst)):
#         # Step 3: Pick the ending point of the sublist
#         for j in range(i + 1, len(lst) + 1):
#             # Step 4: Slice the list from start to end and add it to our collection
#             sublists.append(lst[i:j])
            
#     # Step 5: Return the final list of all sublists
#     return sublists


# def product_of_list_elements(numbers):
#     # Write your code here
#     product = 1

#     for i in range(len(numbers)):
#         product *= numbers[i]
#     return product


# def print_unique_elements(numbers):
#     unique_nums = []
#     for num in numbers:
#         if numbers.count(num) == 1:
#             unique_nums.append(num)
            
#     return unique_nums


# def sum_of_list_elements(numbers):
#     # Write your code here
#     sum = 0

#     for i in range(len(numbers)):
#         sum += numbers[i]
#     return sum


# def merge_lists_alternately(list1, list2):
#     # Step 1: Create an empty list to hold our merged result
#     merged = []
    
#     # Step 2: Find the length of both lists
#     len1 = len(list1)
#     len2 = len(list2)
    
#     # Step 3: Find which list is longer to know how many times to loop
#     max_len = max(len1, len2)
    
#     # Step 4: Loop through up to the maximum length
#     for i in range(max_len):
#         # If there are still elements in list1, add one
#         if i < len1:
#             merged.append(list1[i])
#         # If there are still elements in list2, add one
#         if i < len2:  #We use two independent if statements because both lists need to be checked at the same time during every single step (loop iteration):
#             merged.append(list2[i])
            
#     # Step 5: Return the merged list
#     return merged


# def find_two_greatest(numbers):
#     # Step 1: Handle edge case if the list is too short
#     if len(numbers) < 2:
#         return "List must have at least two numbers"
        
#     # Step 2: Initialize our two greatest variables with very small numbers
#     first_great = float('-inf')
#     sec_great = float('-inf')
    
#     # Step 3: Loop through every number in the list
#     for num in numbers:
#         # If the current number is bigger than the first greatest
#         if num > first_great:
#             sec_great = first_great      # The old first becomes the second
#             first_great = num            # The new number becomes the first
#         # Otherwise, if it's bigger than the second greatest (and not a duplicate of first)
#         elif num > sec_great and num != first_great:
#             sec_great = num
            
#     # Step 4: Return or print the two greatest numbers
#     # print(first_great, sec_great)
#     return first_great, sec_great


# def find_two_greatest(numbers):
#     unique = []

#     for num in numbers:
#         if num not in unique:
#             unique.append(num)

#     unique.sort(reverse=True)

#     if len(unique) == 1:
#         return (unique[0],)
#     else:
#         return (unique[0], unique[1])


# def average_of_list_elements(numbers):
#     total = 0

#     for num in numbers:
#         total += num

#     average = total / len(numbers)

#     return round(average, 2)  #25.00 (The important part is round(average, 2), which rounds the answer to 2 decimal places.)