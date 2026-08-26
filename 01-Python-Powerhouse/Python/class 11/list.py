# # LISTS Practice Set:
# # 1. Sum & Average of List
# # Create a list of numbers, then calculate and print the total sum and average.

# a = [10,20,30,40,50]

# sum = 0
# # for i in range(len(a)):
# for i in a:
#     sum = sum + i

# print(f"sum of your list numbers is {sum}")
# print(f"average of your list numbers are {sum/len(a)}")

# 2. Maximum Element with Index
# Find the largest element in the list along with its position (index).

# a = [1,45,23,89,45,90,12,36,82]

# max = a[0]
# index = 0

# for i in range(len(a)):
#     if a[i] > max:
#         max = a[i]
#         index = i

# print(f"Your maximum element is {max} at index {index}")

# 3. Second Greatest Element
# Identify the second-largest element in the list without sorting directly.

# a = [1,45,23,89,45,93,1,91,12,36,82]

# max = a[0]
# index = 0
# sec_max = a[0]
# sec_index = 0

# for i in range(len(a)):
#     if a[i] > max:
#         sec_max = max
#         max = a[i]

#         sec_index = index
#         index = i
#     elif a[i] > sec_max:
#         sec_max = a[i]
#         sec_index = i

# print(f"Your Second maximum element is {sec_max} at index {sec_index}")

# 4. Check if List is Sorted (Increasing)
# Verify whether the list elements are in ascending order.

# a = [12,13,14,15,16,17,14,23,24,25,36,78,90] 

# for i in range(len(a)-1):
#     if a[i] < a[i+1]:
#         continue
#     else:
#         print("your list is not sorted")
#         break

# else:
#     print("your list is sorted")

# 5. Left Rotation by 1
# Shift all elements one position to the left, with the first element moving to the end.

# # for left rotation:
# a = [10,20,30,40,50]

# for i in range(len(a)-1):
#     a[i],a[i+1] = a[i+1],a[i]

# print(a)

# # for right rotation:
# a = [10,20,30,40,50]

# for i in range(len(a)-1,0,-1):
#     a[i],a[i-1] = a[i-1],a[i]

# print(a)

# 6. Left Rotation by k
# Generalize the previous problem: rotate the list k times to the left.

# k = int(input("how many times you want to rotate "))
# a = [10,20,30,40,50]

# for i in range(k):
#     for i in range(len(a)-1):
#         a[i],a[i+1] = a[i+1],a[i]

# print(a)

# 7. Reverse List (In-Place)
# Reverse the entire list without using extra space (i.e., swap elements).

# a = [10,20,30,40,50]
# b = len(a)-1

# for i in range(len(a)//2):
#     a[i],a[b] = a[b],a[i]
#     b = b -1

# print(a)