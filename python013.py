#Este programa nos muestra los numeros pares entre dos numeros 

num1 = int(input("Ingrese el numero inicial:"))
num2 = int(input("Ingrese el numero final:"))
while num1<=num2 :
    if (num1%2)==0 :
        print (num1)
    num1 = num1+1
print ("Final de la serie.")