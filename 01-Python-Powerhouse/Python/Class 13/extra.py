# def symmetric_difference_finder(n, set1, m, set2):
#     # Step 1: Convert the input lists into sets
#     s1 = set(set1)
#     s2 = set(set2)
    
#     # Step 2: Find and return the symmetric difference using the ^ operator
#     return s1 ^ s2


# def remove_duplicates_using_set(n, elements):
#     # Step 1: Convert to a set to remove duplicates, then sort it into a list
#     return sorted(list(set(elements)))


# def set_operations(n1, set1, n2, set2):
#     s1 = set(set1)
#     s2 = set(set2)

#     # Calculate operations and convert to sorted lists
#     union_res = sorted(list(s1 | s2))
#     intersection_res = sorted(list(s1 & s2))
#     difference_res = sorted(list(s1 - s2))

#     # If the platform expects a formatted string or printing:
#     print(f"Union: {union_res}")
#     print(f"Intersection: {intersection_res}")
#     print(f"Difference: {difference_res}")
    
#     # Or if it expects them returned as a tuple of lists, use:
#     # return union_res, intersection_res, difference_res


# def check_subset_superset(n1, set1, n2, set2):
#     # Step 1: Convert input lists into sets
#     s1 = set(set1)
#     s2 = set(set2)
    
#     # Step 2: Check conditions and format the output message
#     if s1 == s2:
#         result = "Set1 and Set2 are equal"
#     elif s1.issubset(s2):
#         result = "Set1 is a subset of Set2"
#     elif s1.issuperset(s2):
#         result = "Set1 is a superset of Set2"
#     else:
#         result = "No subset or superset relation"
        
#     print(result)

# def check_unique_elements(numbers):
#     # Step 1: Convert the input collection into a set to remove duplicates
#     unique_set = set(numbers)
    
#     # Step 2: Compare the length of the set with the original length
#     if len(unique_set) == len(numbers):
#         return "Unique"
#     else:
#         return "Not Unique"


# Alternative (if it expects True / False):

# def check_unique_elements(numbers):
#     return len(set(numbers)) == len(numbers)

# # Pass as a single list argument
# result = check_unique_elements([1, 2, 3, 4, 5, 1])
# print(result)  # Output: False