# Ques 1.Key with Maximum Value:
# You are given a dictionary containing key-value pairs where all the values are integers.
# Your task is to find the key that has the maximum value and return it. 
# If there are multiple keys with the same maximum value, return any one of them. If the dictionary is empty, return "Empty Dictionary".

# def key_with_max_value(d):
#     if not d:
#         return "Empty Dictionary"
    
#     max_key = None
#     max_value = float('-inf')  # Start with negative infinity so any value is larger
    
#     for i in d:
#         if d[i] > max_value:
#             max_value = d[i]
#             max_key = i
            
#     return max_key

#Ques 2. Check Key Existence:
# You are given a dictionary and a key as input. Your task is to check whether 
# the given key exists in the dictionary or not. If the key exists, print "Key exists".
# Otherwise, print "Key does not exist".

# def check_key_existence(d, key):
#     if key in d:
#         return "Key exists"
#     else:
#         return "Key does not exist"


#Ques 3. Safe Key Removal:
# You are given a dictionary and a key. Your task is to safely remove the key from 
# the dictionary - that is, if the key exists, remove it and print the updated dictionary.
# If the key does not exist, print "Key not found" instead of raising an error.

# def safe_key_removal(d, key):
#     if key in d:
#         del d[key]
#         return d
#     else:
#         return "Key not found"


#Ques 4. Invert Dictionary:
# You are given a dictionary containing key-value pairs. Your task is to invert 
# the dictionary - that is, make each value a key and each key a value. If multiple keys have the same value, 
# keep only one of them in the inverted dictionary. Assume that all values are hashable (i.e., can be used as keys).

# def invert_dictionary(d):
#     inverted = {}
#     for key, value in d.items():
#         inverted[value] = key
#     return inverted


# Ques 5. Find Commom Keys:
# You are given two dictionaries as input. Your task is to find 
# the common keys that appear in both dictionaries. If there are no common keys, 
# print an empty list []. The order of keys in the output does not matter.

# def find_common_keys(dict1, dict2):
#     return list(dict1.keys() & dict2.keys())


#Ques 6.Remove Empty or NOne Values:
# You are given a dictionary that may contain empty strings ("") None values,
#  or valid key-value pairs. Your task is to remove all keys that have None or an empty string as 
# their value and print the cleaned dictionary. If all values are removed, print an empty dictionary {}.

# def remove_empty_or_none_values(d):
#     keys_to_delete = [k for k, v in d.items() if v is None or v == ""]
    
#     for k in keys_to_delete:
#         del d[k]
        
#     return d

#Ques 7. Create Dictionary from Lists:

# def create_dict_from_lists(keys, values):
#     return dict(zip(keys, values))

#Ques 8. Count Key-Value Pairs in Nested Dict:
# Write a Python program to count the total number of key-value 
# pairs in a nested dictionary. If the dictionary contains another dictionary
# as a value, you must recursively count the pairs inside it as well.

# def count_key_value_pairs(data):
#     count = 0
#     for key, value in data.items():
#         count += 1  # Count the current pair
#         if isinstance(value, dict):
#             count += count_key_value_pairs(value)  # Recursively count nested dictionary pairs
#     return count

#Ques 9. Sort Dictionary by Values:
# Write a Python program to sort a dictionary by its values in 
# ascending order. If two values are equal, maintain their original
# order (stable sorting). Return the sorted dictionary as output.

# def sort_dict_by_values(data):
#     # Sort items based on the value (item[1]) rather than the key (item[0])
#     sorted_items = sorted(data.items(), key=lambda item: item[1])
#     return dict(sorted_items)


#Ques 10. Print Keys with Even Values:
# Write a Python program to print all keys from a dictionary 
# whose values are even numbers. If no even values exist, 
# return an empty list.

# def keys_with_even_values(data):
#     result = []
    
#     # Loop through every key and value in the dictionary
#     for key, value in data.items():
#         # Check if the value is a number (integer) and is even
#         if isinstance(value, int) and value % 2 == 0:
#             result.append(key)
            
#     return result


#Ques 11. Merge List of Dictionaries:
# Write a Python program to merge a list of dictionaries into a single dictionary. 
# If a key appears in multiple dictionaries, the latest value should be kept 
# (i.e., the one from the last dictionary in the list).

# def merge_list_of_dicts(dict_list):
#     merged_dict = {}
    
#     for d in dict_list:
#         for key, value in d.items():
#             merged_dict[key] = value
            
#     return merged_dict

#Ques 12. Group Values by Common Key:
# Write a Python program to group values from a list of dictionaries based on their common keys. 
# If multiple dictionaries contain the same key, their values should be combined into a list 
# under that key in the final dictionary.

# def group_values_by_key(dict_list):
#     result = {}

#     for d in dict_list:
#         for key, value in d.items():
#             if key not in result:
#                 result[key] = []
#             result[key].append(value)
            
#     return result

#Ques 13. Find Keys in Nested Dictionary Recursively:
# Write a Python program to find all keys in a nested dictionary recursively. 
# The program should return a list of all unique keys, regardless of how deeply
# they are nested within other dictionaries.

# def find_keys_recursive(data):
#     keys_list = []
    
#     for key, value in data.items():
#         keys_list.append(key)
#         if isinstance(value, dict):
#             keys_list.extend(find_keys_recursive(value))
            
#     return keys_list