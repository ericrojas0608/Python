
def Retorno():
    num1=int(input("Ingrese 1er. numero: "))
    num2=int(input("Ingrese 2do. numero: "))

    retorno =0
    if num1 > num2:
        return 1
    elif(num2 > num1):
        return 1
    else:
        return 0
    
    
print(Retorno())