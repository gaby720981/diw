from platform import platform
 
 #platform permite acceder a los datos de la plataforma subyacente, es decir, hardware, sistema operativo e información sobre la versión del intérprete.

print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine #nombre genérico del procesador

print(machine())

from platform import processor #devuelve una cadena con el nombre real del procesador
 
print(processor())

from platform import system #devuelve el nombre genérico del sistema operativo en una cadena.

print(system())

from platform import version #versión del sistema operativo

print(version())

# Si necesitas saber que versión de Python está ejecutando tu código, 
# puedes verificarlo utilizando una serie de funciones dedicadas, aquí hay dos de ellas:

# python_implementation() → devuelve una cadena que denota la implementación de Python 
# (espera CPython aquí, a menos que decidas utilizar cualquier rama de Python no canónica).

# python_version_tuple() → devuelve una tupla de tres elementos la cual contiene:
# -La parte mayor de la versión de Python.
# -La parte menor.
# -El número del nivel de parche.

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

