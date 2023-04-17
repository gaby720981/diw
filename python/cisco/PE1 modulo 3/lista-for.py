my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)

#A la lista se le asigna una secuencia de cinco valores enteros.
#La variable i toma los valores 0, 1,2,3, y 4, y luego indexa la lista, seleccionando los elementos siguientes: 
# el primero, segundo, tercero, cuarto y quinto.
#Cada uno de estos elementos se agrega junto con el operador += a la variable suma, 
# dando el resultado final al final del bucle.
#Observa la forma en que se ha empleado la función len(), 
# hace que el código sea independiente de cualquier posible cambio en el contenido de la lista.