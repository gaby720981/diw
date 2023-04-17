
nums = [1, 2, 3, 4, 5, 6] 
print(nums)
del nums[2] #eliminar elemento de esa posición [2] y no lo devuelve
print(nums)

letras = ["a", "b", "c", "d"]
print(letras)

letras.remove("d")#eliminar un elemento específico
print(letras)

letras.append("e")#añadir un elemento
print(letras)

letras.insert(0, "z")#añadir un elemento en una posición específica
print(letras)

letras[0] = "q"#modificar valor de un elemnento
print(letras)

print(letras.pop())#eliminar el último elemento y nos devuelve el valor
print(letras.pop(1))#eliminar elemento de una ubicación específica
print(letras)

letras.clear()#eliminar todos los elementos de una lista

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list)
new_list = list.copy()
list.clear()
print(list)
print(new_list)
new_list.reverse()
print(new_list)

list3 = [18, 29, 35, 12]
print(list3)
list3.sort()#ordena elementos
print(list3)



