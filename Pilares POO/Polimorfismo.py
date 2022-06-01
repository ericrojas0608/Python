
#modificacion de metodos cuando se heredan de otras clases

class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Guao")

class Pez(Animales):
    def hablar(self):
        print("Yo no hablo")

animal= Animales("miau!")
animal.hablar()

perro = Perro("nada")
perro.hablar()

pez = Pez("nada")
pez.hablar()