my_list = [] #crear lista vacía
swapped = True #hay intercambio
num = int(input("¿Cuántos elementos deseas ordenar?: ")) #variable cantidad de elementos

for i in range(num): #bucle en num
    val = float(input("Ingresa un elemento de la lista: ")) #lista elementos
    my_list.append(val) #agregar elementos a la lista

while swapped: #ordenar si True
    swapped = False #no hay intercambios
    for i in range(len(my_list) - 1): #bucle en longitud - 1
        if my_list[i] > my_list[i + 1]: #si es mayor que adyascente
            swapped = True #hay intercambio
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] #ejecutar intercambio

print("\nOrdenada:")
print(my_list)