numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4) #Un nuevo elemento puede ser añadido al final de la lista existente. 
#Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

print(len(numbers)) #puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.

print(numbers)

###

numbers.insert(0, 222) ##puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.
#El primer argumento muestra la ubicación requerida del elemento a insertar.
#El segundo es el elemento a insertar.

print(len(numbers))
print(numbers)