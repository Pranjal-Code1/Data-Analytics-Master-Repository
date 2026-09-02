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