# a = [1,1.4,12j,"hello",True,print(),str()]
# #you can store anything inside a list 
# #hetrogenous Nature 

# #list can also store duplicates 
# b = [1,1,1,1,2,2,2,2,3,3,3,3]

# #list is mutable that means you can change anything 

# c = [1,2,3,4.5,5,6,7]
# #you can change 4.5 to 4 cause it is mutable

# l = [10,20,30,40,50]

# print(l[:3]) #list indexing and slicing is also here 

# a = [10,20,30,45,50]

# a[3] = 40

# print(a)


#reference copy
# a = [10,20,30,40]

# b = a 

# b[0] = 100
# print(a)
# print(b)

#shallow copy
# a = [10,20,30,40]

# b = a.copy()

# b[0] = 100

# print(a)
# print(b)

#Deep copy 

# import copy

# a = [10,20,30,40]

# b = copy.deepcopy(a)

# b[0] = 100

# print(a)
# print(b)

# import copy

# a = [[10,20], [30,40]]

# b1 = a.copy()             # shallow copy
# b2 = copy.deepcopy(a)     # deep copy

# b1[0][0] = 999
# b2[1][0] = 888

# print("Original:", a)     # [[999, 20], [30, 40]]  ← changed by shallow copy
# print("Shallow:", b1)     # [[999, 20], [30, 40]]
# print("Deep:", b2)        # [[10, 20], [888, 40]]  ← completely independent


#traversing method 1 
# a = [10,20,30,40]

# for i in a:
#     print(i)


#traversing method 2 (index)
# a = [10,20,30,40]

# for i in range(len(a)):
#     print(a[i])


# a = [10,20,30,40,67,12,13,45,17,56]

# a.sort()
# print(a)


# help(list)