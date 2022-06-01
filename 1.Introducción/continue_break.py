
#break - corta la iteracion y muestra recorrido hasta donde esta el break
#continue - muestra datos y salta el dato en donde esta el continue

'''
for i in range(1,11):
   
    if i==6:
        #print("Llega hasta el 5")
        continue
    print(i)
'''
'''
#ejercicio1 
for i in (range(1,11)):
    print(i)
    
n1 = int(input("Ingresa 1er. numero: "))
n2 = int(input("Ingresa 2do. numero: "))

for i in(range(n1, n2 + 1)):
    print(i) 
'''
#ejercicio2
n1 = int(input("Ingresa 1er. numero: "))
n2 = int(input("Ingresa 2do. numero: "))

for i in range(n1,n2+1):
    if i%2 == 0:
        continue
    print(i)
