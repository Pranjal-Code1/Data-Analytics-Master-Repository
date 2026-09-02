# Dictionary Logic Building Questions

# 771. Jewels and Stones
# class Solution:
#     def numJewelsInStones(self, jewels: str, stones: str) -> int:
#         d = {}
#         for i in stones:
#             if i in d.keys():
#                 d[i] +=1
#             else:
#                 d[i] = 1
        
#         count = 0
#         for i in d.keys():
#             if i in jewels:
#                 count +=d[i]
        
#         return count

# 1832. Check if the Sentence Is Pangram
# class Solution:
#     def checkIfPangram(self, sentence: str) -> bool:
#         d = {}
#         for i in sentence:
#             if i in d.keys():
#                 d[i] +=1
#             else:
#                 d[i] = 1
        
#         if len(d.keys()) == 26:
#             return True
#         else:
#             return False

# 2351. First Letter to Appear Twice

# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         d = {}
#         for i in s:
#             if i in d.keys():
#                 return i
#             else:
#                 d[i] = 1
        
# 1748. Sum of Unique Elements

# class Solution:
#     def sumOfUnique(self, nums: List[int]) -> int:
#         d = {}

#         for i in nums:
#             if i in d.keys():
#                 d[i] +=1
#             else:
#                 d[i] = 1
        
#         sum = 0
#         for i in d.keys():
#             if d[i] == 1:
#                 sum+=i
        
#         return sum
        
# 2418. Sort the People

# class Solution:
#     def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#         d = {}

#         for i in range(len(names)):
#             d[heights[i]] = names[i]
        
#         d = sorted(d.items(), key= lambda x: x[0], reverse = True)

#         for i in range(len(d)):
#             names[i] = d[i][1]

#         return names


# Ques . Check if Two Strings Have Same Frequency Map
# Compare character frequencies of two strings and check if they match.

# s1 = "aabbcc"
# s2 = "baccab"

# if len(s1) == len(s2):
#     d = {}
#     for i in s1:
#         if i in d.keys():
#             d[i] +=1
#         else:
#             d[i] = 1
#     for i in s2:
#         if i in d.keys():
#             d[i] -=1
#         else:
#             print("an extra element was found")
            
#     for i in d:
#         if d[i] !=0:
#             print("sorry your element are not same")
#             break
#         else:
#             print("your string are same")


# else:
#     print("not same")   

#Find Duplicates in Array Using HashSet
# Detect and print elements that appear more than once in the array.
# a = [1,1,3,3,5,5,5,6,6,1,2,3,4,5,6,7,8,9,0]
# d= {}

# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1

# for i in d:
#     if d[i] >1:
#         print(i)


# Leetcode 2404 - Most Frequent Even Element
# Find the even number with the highest frequency; return the smallest one if t

# class Solution:
#     def mostFrequentEven(self, nums: List[int]) -> int:

#         d= {}

#         for i in nums:
#             if i%2 ==0:
#                 if i in d.keys():
#                     d[i] +=1
#                 else:
#                     d[i] = 1
        
#         if not d:
#             return -1
        
#         max_f = max(d.values())

#         cand = [num for num, freq in d.items() if freq == max_f]

#         return min(cand)

# Leetcode 2283 - Check if Number Has Equal Digit Count and Digit Value
# Determine if the count of each digit matches its value in the string.

# class Solution:
#     def digitCount(self, num: str) -> bool:
#         d = {}

#         for i in num:
#             if i in d.keys():
#                 d[i] +=1
#             else:
#                 d[i] = 1
            
#         for i in range(len(num)):
#             if d.get(str(i),0) == int(num[i]):
#                 continue
#             else:
#                 return False
#         return True

#Ques. Intersection of Two Arrays
# Return all unique elements that appear in both arrave

# a= [1,2,3,2,3,4,5]
# b= [2,2,3,3,4,4]

# j = []
# d= {}

# for i in a:
#     if i in d.keys():
#         d[i] +=1
#     else:
#         d[i] = 1

# for i in d.keys():
#     if i in b:
#         j.append(i)

# print(j)