class Student:#class is the blueprint of an object
   def __init__(self,name,age,school):#constructor must have arg self
       self.name=name # Assigning the variables to the instance of the class
       self.age=age
       self.school=school
   def speak(self):
       return f"hello, my name is {self.name} and I am {self.age} years old and I love {self.school}"