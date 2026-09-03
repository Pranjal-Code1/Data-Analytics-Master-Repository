#lambda expression 

# square = lambda a : print(a**2)

# square(12)

# add = lambda x,y : x+y

# print(add(12,12))

#map 

#purpose Apply function to every item of an iterable and return a new iterable

#syntax = map(function , iterable)

# def square(x):
#     return x**2

# a = [1,2,3,4]
# l = map(square,a)
# print(list(l))

#Filter 
#purpose - Filter items from an iterable boased on a condition 

#syntax - filter(function,iterable)

# a = [1,2,3,4,5,6]

# l = filter(lambda x : x%2 == 0,a)

# print(list(l))

#zip
#purpose : Combine multiple iterables into pairs of elements.

#syntax = zip(iterable 1,iterable2, ....)

# name = ["Akarsh","Rahul","Priya"]
# ages = [24,22,23]

# comb = zip(name,ages)

# print(dict(list(comb)))


# a = [1,2,3,4,5,6,7,8,9]

# l = [i for i in a if i % 2 == 0]

# print(l)

# a = [1,2,3,4,5,6,7,8,9]

# l = {i for i in a if i %2 ==0}

# print(l)

# a = [1,2,3,4,5,6,7,8,9]

# l = {i:i**2 for i in a if i%2 ==0}

# print(l)

# Generators in Python

# Purpose: Generators are a special type of iterator that generate items one by one instead of storing the entire sequence in memory.

# Why use them:

# Saves memory for large datasets

# Efficient for lazy evaluation (compute values only when needed)

# def my_generator():
#     for i in range(5):
#         yield i

# gen = my_generator()
# print(next(gen))
# print(next(gen))
# print(list(gen))


# sequence = (x**2 for x in range(5))

# print(next(sequence))
# print(next(sequence))
# print(next(sequence))

# def my_decorator(func):
#     def wrapper():
#         print("hello I will print before")
#         func()
#         print("hello I will print after")
#     return wrapper

# @my_decorator
# def say_hello():
#     print("hello")


# say_hello()

# def decorate(func):
#     def wrapper(a,b):
#         print("Your 2 numbers addition is : ")
#         func(a,b)
#         print("thankyour for using us")
#     return wrapper

# @decorate
# def addition(a,b):
#     print(a+b)

# addition(12,12)