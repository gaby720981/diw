from mimetypes import init


variable = "Variable de mi módulo"

def funcion ():
    print ("Función de mi módulo")

class Clase ():
    def __init__(self):
        print("Clase de mi módulo")

if __name__ == "__main__": #se ejecuta sólo cuando se use como programa principal (ejecutando el propio módulo)
    print ("Este módulo hace una tarea por su cuenta")

import math as m

print("Número pi:", m.pi)
print("Número e:", m.e)

print("Suelo:", m.floor(m.pi))
print("Potencia:", m.pow(2,10))
print("Raiz cuadrada:", m.sqrt(16))
print("Factorial:", m.factorial(4))
print("Logaritmo base 10:", m.log10(1000))

import random as r

print(dir(r))
print("Aleatorio entre [0,1):", r.random())
print("Aleatorio entre [a,b]", r.uniform (-10,10))
print("Integer aleatorio entre [a,b]:", r.randint(-10,10))

baraja = ["Corazón", "Diamante", "Trébol", "Pica"]
print("Baraja:", baraja)
print("Elemento aleatorio:", r.choice(baraja))
r.shuffle(baraja)
print("Baraja mezclada:", baraja)


