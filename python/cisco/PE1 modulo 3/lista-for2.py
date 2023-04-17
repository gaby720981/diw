my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list:
    total += i

print(total)

#La instrucción for especifica la variable utilizada para navegar por la lista (i) 
# seguida de la palabra clave in y el nombre de la lista siendo procesado (my_list).
#A la variable i se le asignan los valores de todos los elementos de la lista subsiguiente, 
# y el proceso ocurre tantas veces como hay elementos en la lista.
#Esto significa que usa la variable i como una copia de los valores de los elementos, 
# y no necesita emplear índices.
#La función len() tampoco es necesaria aquí.