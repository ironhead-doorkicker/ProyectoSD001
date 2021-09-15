#en este programa vamos a aprender a usar el while en python

print ("Este programa imprime una serie de numeros entre dos numeros ingresados.\n")

num1 = int(input("Ingrese numero inicial:"))
num2 = int(input("Ingrese numero final:"))

print (f"La lista inicia en {num1}")
while num1<=num2 :
    print (num1)
    num1=num1+1
print (f"La lista finaliza en {num2}")