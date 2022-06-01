def total():

    monto = float(input("Ingrese el valor del producto: "))
    iva= int(input("Ingrese el IVA:"))

    if iva != 0:
        if iva > 0:
            totalpagar = ((monto*iva)/100) + monto
            return totalpagar
        else:
            return "IVA es negativo"
    else:
        totalpagar=(monto*0.21) + monto
        return totalpagar
print("El total del monto es: ", total())


#total()