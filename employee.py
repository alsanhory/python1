class Employee:
    nafoosa=30
    def __init__(self,name):
        self.name=name
    def saymyname(self):
        
        print(self.name)
    def saysomething(self):
        print("something else")
class Hajakida:
    def sayhello(self):
        print("just say hello")

class Retair(Employee,Hajakida):
    def __init__(self,name):
        self.name=name + " Fathername " 
        
    def saymynamde(self):
        print("You are retaired")
yathreb= Retair("Mohammed")
""" yathreb.name="Haja jaddeda" """
yathreb.saymyname()
""" print(yathreb.nafoosa) """