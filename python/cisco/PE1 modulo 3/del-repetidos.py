from ast import Break


list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]


for i in range(len(list)):
    if (list[i] == list[i+1]):
       list.remove(i)

    
print("La lista con elementos únicos:")
print(list)

