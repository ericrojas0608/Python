class A():
    def __init__(self):
        self.contador= 0
    
    def incrementar(self):
        self.contador+=1
    
    def cuenta(self):
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self):
        self.__contador+=1
    
    def cuenta(self):
        return self.__contador

a = A()

print("objeto 1")
print(a.cuenta())
a.incrementar()
print(a.cuenta())

print("objeto 2")
b=B()
print(b.cuenta())
b.incrementar()
#print(b.__cont)