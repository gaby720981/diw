from random import random  #numeros aleatorios

for i in range(5):
    print(random())  #producirá cinco valores pseudoaleatorios

print("**************************************")

# La función seed() es capaz de directamente establecer la semilla del generador. Variantes:

# seed() - establece la semilla con la hora actual.
# seed(int_value) - establece la semilla con el valor entero int_value.  

from random import random, seed

seed(0)

for i in range(5):
    print(random())

print("**************************************")

from random import randrange, randint

# randrange(fin)
# randrange(inico, fin)
# randrange(inicio, fin, incremento)
# randint(izquierda, derecha)

print(randrange(10), end=' ')
print(randrange(0, 15), end=' ')
print(randrange(0, 50, 1), end=' ')
print(randint(0, 12))

print("**************************************")

from random import randint

for i in range(10):
    print(randint(1, 10), end=',') #hay valores repetidos

print("**************************************")

from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list)) # elige un elemento "aleatorio" de la lista
print(sample(my_list, 5)) # crea una lista (una muestra) que consta del elemento elementos_a_elegir (que por defecto es 1) "sorteado" de la secuencia de entrada.
print(sample(my_list, 10))


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

# Python3 program to demonstrate the practical application
# choice()

# import random module
import random

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in range(5):
	print(random.choice(list1)) #Imprime cualquier número aleatorio 5 veces de una lista dada.
