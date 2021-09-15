#ejemplo de como meter mas elementos al final de la lista

import os
os.system('cls')

lista = ["juan","mario","pedro","esteban","luis","roberto"]

print (type(lista))
print (lista)
lista.append("jaja")
print(lista)
cadena = "jejeje"
lista.append(cadena)
print(lista)
numero=666
lista.append(numero)
print(lista)

#Este es un claro ejemplo de que se puede meter funciones dentro de funciones
lista.append(input("ingrese numero:"))
print(lista)