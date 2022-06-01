

class Calculadora():
    def __init__(self):        
        self.num1 = int(input("Ingrese 1er. valor: "))
        self.num2 = int(input("Ingrese 2do. valor: "))

    def suma(self):
        self.suma = self.num1+self.num2
        print("La suma es: ", self.suma)
    
    def resta(self):
        self.resta = self.num1 - self.num2
        print("La resta es: ", self.resta)

    def producto(self):
        self.producto = self.num1 * self.num2
        print("El producto es: ", self.producto)

    def divide(self):
        self.divide = self.num1 / self.num2
        print("La division es: ", self.divide)

calcular = Calculadora()
calcular.suma()
calcular.resta()
calcular.producto()
calcular.divide()