# class Animal:
#     gender = "Male" # class attribute

#     def __init__(self,name,age):
#         self.name = name #instance attribute
#         self.age = age  #instance attribute

#     def info(self):  #instance method
#         print("this is a method")
    
#     @classmethod
#     def clmethod(cls): #class method
#         print(f"{cls.gender} is your gender")
    
#     @staticmethod
#     def hello():  #static method
#         print("hello I am a static method")



# obj = Animal("Lion",12)

# obj.info()

# obj.clmethod()

# obj.hello()


#make a student regestration system ask for name, age, number, blood group register 3 students 

# class Regestration():
#     def __init__(self,name,age,number,blood):
#         self.name = name
#         self.age = age
#         self.number = number
#         self.blood = blood

#     def info(self):
#         print(f"hello your name is {self.name}\nyour age is {self.age}\nyour number is {self.number}\nyour blood group is {self.blood}")

# student1 = Regestration("Vansh",24,916736432,"B+")
# student2 = Regestration("Ansh",22,9901646451,"A+")
# student3 = Regestration("Harsh",23,9102606414,"O-")

# student2.info()
# student3.info()