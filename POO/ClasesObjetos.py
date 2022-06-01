
class FabricaTelefonos():
    marca="Huawei"
    color="Negro"
    memRam=32
    Almcenamiento=128

    def llamar(self,mensaje):
        return mensaje

    def escucharMusica(self):
        print("Escucha musica")

telefono=FabricaTelefonos()

#print(telefono.marca)
print(telefono.llamar("Hola"))
telefono.escucharMusica()