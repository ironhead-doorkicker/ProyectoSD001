#Este es un programa que pregunta que operacion quieres hacer y la realiza
#por medio de una implmentecion de if, while y funciones de usuario

import os

def programa ():
    cualoperacion = int(input("1.SUMA\n2.RESTA\n3.MULTIPLICACION\n4.DIVISION\nIngrese opcion:"))
    os.system('cls')
    num1 = int(input("Ingrese numero1:"))
    num2 = int(input("Ingrese numero2:"))
    if cualoperacion==1:
        funcionsuma(num1,num2)
    elif cualoperacion==2:
        funcionresta(num1,num2)
    elif cualoperacion==3:
        funcionmultiplicacion(num1,num2)
    elif cualoperacion==4:
        funciondivision(num1,num2)
    else:
        print ("OPCION NO VALIDA.")

def funcionsuma(num1,num2):
    os.system('cls')
    print (f"El resultado de la suma {num1}+{num2}={num1+num2}")

def funcionresta(num1,num2):
    os.system('cls')
    print (f"El resultado de la resta {num1}-{num2}={num1-num2}")

def funcionmultiplicacion(num1,num2):
    os.system('cls')
    print (f"El resultado de la multiplicacion {num1}*{num2}={num1*num2}")

def funciondivision(num1,num2):
    os.system('cls')
    print (f"El resultado de la division {num1}/{num2}={num1/num2}")

os.system('cls')
respuesta = 1
while respuesta==1 :
    print ("¿Desea realizar una operacion?\n1.SI\n2.NO\nIngrese su respuesta:")
    respuesta = int(input())
    if respuesta==1:
        os.system('cls')
        programa()
    elif respuesta==2:
        respuesta = 2
    else:
        print ("OPCION NO VALIDA.")


