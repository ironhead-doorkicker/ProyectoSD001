#Este programa nos ayuda a pedir un numero y ese va ser el numero de elementos que vamos a 
#meter en una lista de python

import os
os.system("cls")

contador=0
numerodeelementos=0
lista = []

numerodeelementos = int(input("Ingrese el numero de elementos que quiere ingresar a la lista:"))
os.system("cls")
while contador < numerodeelementos :
    datoingresado = input(f"Ingrese el elemento {contador+1}:")
    lista.append(datoingresado)
    contador = contador+1
print("La lista ingresada es:",lista)
