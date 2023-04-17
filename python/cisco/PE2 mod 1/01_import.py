import math
print(math.sin(math.pi/2)) #se desea imprimir el valor de sin((½π)

#dos namespace pueden coexistir:
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))
print(math.sin(math.pi/2))


from math import sin, pi #importacion selectiva
print(sin(pi/2))

from module import * #importa todas las entidades(forma general)

import module as alias #aliasing:renombrar el modulo

import math as m

print(m.sin(m.pi/2))

from module import name as alias #renombrar la identidad

dir (module) #revela todos los nombres proporcionados a través de un módulo en particular.

