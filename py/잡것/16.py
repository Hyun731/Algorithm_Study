class C1:
    a : int
    b : str
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self,a,b):
        return f'{self.a} {self.b}'
    def m1(self):
        return self.a * self.b
class Car:
    engine : str
    wheel : int
    brand : str
    
    def excel(self):
        pass
    def brake(self):
        pass
car = Car() #instance
class Truck(Car):
    def __init__(self):
        super().__init__()
    def u_turn(self):
        self.excel()
