
class A():
    def __init__(self):
        #el guion bajo indica que son encapsulados
        self._cuenta=0
        self._contador=0

    #metodo GET
    @property #esto indica que va ser tomado como un metodo GET, ejecuta el metodo abajo como si fuera un atributo
    def cuenta(self):
        return self._cuenta

    #metodo SET
    @cuenta.setter
    def cuenta(self,cuenta):
        self._cuenta =cuenta
    
    @property
    def contador(self):
        return self._contador

a = A()
#como buena practica se debe llamar al metodo de la clase y no al atributo
print(a.cuenta) #ejecuta el metodo cuenta() sin parentesis como si fuera un atributo esto lo hace mediante la instruccion @property
a.cuenta = 20
print(a.cuenta)
print(a.contador)
