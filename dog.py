class Dog:
    def __init__(self,breed,name,age):
        self.breed=breed
        self.name=name
        self.age=age
    def bark(self):
        return f"my dog is a {self.breed} aged {self.age} name {self.name}"  