
class FabricaTelefonos():
    def __init__(self, marca, *colores, **modelos):
        self.marca=marca
        self.colores=colores
        self.modelos=modelos
        print(self.marca)
        print(self.colores)
        print(self.modelos)

'''
telefono= FabricaTelefonos("Alcatel","Negro","Azul", m1=500, m2=505, ml=325)
print(telefono.marca)
print(telefono.colores)
print(telefono.modelos)
'''

telefono = FabricaTelefonos("Alcatel","Negro","Azul", "Blanco", m1=500, m2=505, ml=325)
print(type(telefono.marca))
print(type(telefono.modelos))
print(type(telefono.colores))