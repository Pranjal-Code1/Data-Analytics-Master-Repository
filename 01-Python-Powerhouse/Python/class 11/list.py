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


# 8. Linear Search
# Search for a given element by checking each element one by one.

# a = [23,67,123,1,54,7,98,45,23,13,6,68]

# search = 67

# for i in range(len(a)):
#     if a[i] == search:
#         print(f"Element found at index {i}")
#         break
# else:
#     print("Sorry no such element exist")


# 9. Binary Search
# Efficiently search for an element in a sorted list using the divide-and-conquer approach.

# a = [12,14,16,23,25,34,37,45,48,59,68,70]

# search = 13

# start = 0
# last = len(a)-1
# mid = (start + last)//2

# while start <= last:
#     if a[mid] == search:
#         print(f"element found at index {mid}")
#         break
#     elif a[mid] < search:
#         start = mid + 1
#         mid = (start + last)//2
    
#     elif a[mid] > search:
#         last= mid -1
#         mid = (start + last)//2
# else:
#     print("sorry no such element exist")


# 10. Bubble Sort
# Sort the list by repeatedly swapping adjacent elements if they are in the wrong order.


# a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]

# for j in range(len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a[i+1]:
#             a[i],a[i+1] = a[i+1],a[i]

# print(a)

# 11. Selection Sort
# Sort the list bv selectina the smallest element in each pass and placing it in the correct
# positinn

# a = [56,234,23,24,46,6878,9,674,52,3,12,13,368]

# for i in range(len(a)-1):
#     j = i+1
#     min = i
#     for k in range(j,len(a)):
#         if a[k] <a[min]:
#             min = k
    
#     a[i],a[min] = a[min],a[i]

# print(a)