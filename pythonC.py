#este programa me va a ayudar 
#a entender como fucnionan los colores en python

import os
from colorama import Fore, init, Back
#from colorama.ansi import Back
os.system("cls")
init()

print(Fore.GREEN + "Recursos Python")
var1 = "jejeje"
print(Fore.YELLOW + "Esta cadena va de color amarillo")
print(Fore.RED+"cadena color rojo")
print(Fore.GREEN+"cadena color verde")
print(Fore.BLUE+"cadena de color azul")
print(Fore.MAGENTA+"cadena de color magenta")
print(Fore.BLUE+"cadena de color azul")
print(Fore.CYAN+"cadena de color cyan")
print(Fore.WHITE+"cadena de color blanco")
print(Fore.BLACK+Back.WHITE+"cadena de color negro")
