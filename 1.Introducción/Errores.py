

while True:
    try:
        edad=int(input("Ingrese la edad: "))
        print("Tu edad es: ",edad)
        break
    except:
        print("ingresaste valor incorrecto")
    