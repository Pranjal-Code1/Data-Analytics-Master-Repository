# def sum_and_average_tuple(n, elements):
#     # Step 1: Handle edge case for an empty tuple
#     if n == 0:
#         return 0, 0
        
#     # Step 2: Calculate the total sum of the tuple elements
#     total_sum = sum(elements)
    
#     # Step 3: Calculate the average
#     avg = total_sum / n
    
#     # Step 4: Return the results so the test runner can capture them properly
#     return total_sum, avg


# def remove_element_from_tuple(n, elements, to_remove):
#     # Step 1: Convert the tuple into a list so we can modify it
#     lst = list(elements)
    
#     # Step 2: Filter out all instances of the element to remove
#     updated_list = [item for item in lst if item != to_remove]
    
#     # Step 3: Convert the list back into a tuple and return it
#     return tuple(updated_list)

# def remove_element_from_tuple(n, elements, to_remove):
#     # Step 1: Create an empty list to store the elements we want to keep
#     new_list = []
    
#     # Step 2: Loop through each item in the original tuple
#     for item in elements:
#         # Step 3: If the item is not the one we want to remove, keep it
#         if item != to_remove:
#             new_list.append(item)
            
#     # Step 4: Convert our final list back into a tuple and return it
#     return tuple(new_list)


# def check_element_existence(n, elements, search_element):
    
#     if search_element in elements:
#         return "Found"
#     else:
#         return "Not Found"

# def max_min_tuple_elements(n, elements):
#     # Step 1: Handle edge case for an empty tuple
#     if n == 0:
#         return None, None
        
#     # Step 2: Assume the first element is both the max and min initially
#     max_element = elements[0]
#     min_element = elements[0]
    
#     # Step 3: Loop through every element in the tuple
#     for item in elements:
#         # Update max if we find a larger value
#         if item > max_element:
#             max_element = item
            
#         # Update min if we find a smaller value
#         if item < min_element:
#             min_element = item
            
#     # Step 4: Return both results
#     return max_element, min_element


# def frequency_count_tuple(n, elements):
#     # Step 1: Create an empty dictionary to store each element and its count
#     freq_dict = {}
    
#     # Step 2: Loop through each item in the tuple
#     for item in elements:
#         # If the item is already in our dictionary, increase its count by 1
#         if item in freq_dict:
#             freq_dict[item] += 1
#         # Otherwise, add it to the dictionary with a starting count of 1
#         else:
#             freq_dict[item] = 1
            
#     # Step 3: Return the completed frequency dictionary
#     return freq_dict