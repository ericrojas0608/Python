
class A():
    def primera(self):
        return "primera clase A"

class B():
    def segunda(self):
        return "segunda clase B"

class C(A , B):  #la clase A y B  son padres de la clase C
    pass

c = C()
print(c.primera())
print(c.segunda())