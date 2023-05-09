#iterar listas
animales = ["perro", "gato", "loro", "cocodrilo"]
numeros = [52, 16, 78, 46]

# for animal in animales:
#     print (animal)

#salida: 
# perro
# gato
# loro
# cocodrilo

for animal in animales:
     print (f"Ahora la variable animal es igual a: {animal}")
     #"animal" es una variable que se crea solamente para utilizar en el bloque de código.

#salida:
#Ahora la variable animal es igual a: perro
# Ahora la variable animal es igual a: gato
# Ahora la variable animal es igual a: loro
# Ahora la variable animal es igual a: cocodrilo

#recorre la lista numeros y multiplica cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print (resultado)

#iterando elementos de listas del mismo tamaño
for numero, animal in zip (numeros, animales):
    print (f"recorriendo lista 1: {numero}")
    print (f"recorriendo lista 2: {animal}")
    
#obtener indice de una lista
for num in enumerate (numeros):
    indice = num[0]
    valor = num[1]
    print(f"el indice es: {indice} y el valor es: {valor}")

#funciona igual para tuplas y conjuntos