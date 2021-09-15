#Este programa nos ayuda a entender como meter mas datos a una lista

import os
os.system("cls")

lista=["juan","pedro","perro","pollo","pendejo"]

def funcionmain():
    respuesta=1
    while respuesta==1:
        respuesta=(int(input("1.Ingresar dato\n2.Salir\nIngrese opcion:")))
        if respuesta==1:
            funcioningresar()
        elif respuesta==2:
            respuesta=2
        else:
            print("RESPUESTA INVALIDA")
        print(lista)

def funcioningresar():
    lista.append(input("Ingrese el nombre que vas a agregar:"))

funcionmain()