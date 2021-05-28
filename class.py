class Car:
    def __init__(self,make,color,registration,model):
        self.make=make
        self.color=color
        self.registration=registration
        self.model=model
    def accelaration (self,acceleration):
        self.accelaration=acceleration
        return f" my {self.make}, {self.model},{self.color} car has an acceleration of {self.acceleratio }"
    def hoot(self):
        return "All cars hoot when started"