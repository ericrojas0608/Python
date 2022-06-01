
class Animales():
    def __init__(self, nombre):
        self.nombre = nombre


class Perro(Animales):
    def __init__(self, nombre, sonido):
        super().__init__(nombre) #esto hereda completamente la clase
        self.sonido = sonido

perro = Perro("Firulais", "Guaoo!")
print(perro.nombre)
print(perro.sonido)