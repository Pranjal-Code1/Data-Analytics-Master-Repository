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
