import mi_modulo

print(mi_modulo.variable)

mi_modulo.funcion()

mi_modulo.Clase()

#podemos usar la sentecia as para renombrar el módulo
#y facilitarnos la llamada a su contenido

import mi_modulo as mo

print(mo.variable)

mo.funcion()

mo.Clase()

#podemos importar solo cierto contenido

from mi_modulo import variable

print(variable)

#podemos importar varios elementos (incluso renombrar lo que importemos)

from mi_modulo import variable as va, funcion as fu

print(va)
fu()

#(es una buena practica importar sólo lo que vayamos a usar, concretamente con módulos muy grandes.)

#NAMESPACE: conjunto de todos los nombre definidos 
# (variables, funciones, clases) que se pueden visualizar en una lista con la función integrada "dir".

import mi_modulo as mo
print (dir(mo))

print(mo.__name__) 



