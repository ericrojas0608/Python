#self - sirve para englobar un atributo a toda la clase
#constructor (metodo init) - primer metodo que se ejecuta al crearse un objeto, se utiliza para crear los atributos de la clase

'''
class FabricaTelefonos():
    marca="Samsung"

    def ElaboraHuawei(self):
        self.marca = "Huawei"

telefono=FabricaTelefonos()
print(telefono.marca)
telefono.ElaboraHuawei()
print(telefono.marca)
'''

class FabricaTelefonos():

    #definir el constructor
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color        
        
telefono = FabricaTelefonos("Samsung","Azul")

print(telefono.marca)
print(telefono.color)