#Este programa me ayudara a saber como trabajan las funciones de usuario
#en PYTHON, y ver como implementarlas en mis programas

'''Recuerda que en PYTHON las funcones de usurio se tienen que definir con "def" '''
def funcioncreada ():
    print ("Esta funcion muestra este mensaje.")
    print ("Solo muestra estas dos lineas.\n")

contador = 1
numeroderepeticiones = int(input("\nIngrese el numero de veces que quieres que se llame a la fucnion:"))

while contador<=numeroderepeticiones :
    print (f"Esta es la llamada #{contador}")
    funcioncreada()
    contador = contador+1

print ("El programa ha terminado")

#gracias a este programa ahora ya se como usar las funciones de ususrio en PYTHON
#es bien facil porque solo tenemos que usar la palabra def antes
#de definir el cuerpo de la funcion, recuerda los dos puntos y el indentado de la funcion