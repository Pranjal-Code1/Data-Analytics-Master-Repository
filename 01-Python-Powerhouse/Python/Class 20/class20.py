# class Factory:
#     a = "hello I am an attribute"
#     def hello(s):
#         print("hello I am a method")

# obj = Factory() #obj becomes an object who can access anythin inside the class till now
# obj2 = Factory()

# print(obj.a)
# obj2.hello()


# class Student:
#     def show():  # 0 parameters defined
#         print("Hello")

# s = Student()
# s.show()  # Raises TypeError because Python passes 's' automatically!


# class Student:
#     def show(self):  # 'self' receives the object instance
#         print("Hello from student!")

# s = Student()
# s.show()  # Works perfectly!