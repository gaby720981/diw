bloques = int(input("Introduzca el número de bloques disponibles: "))
 
altura = 0
 
utilizados = 0
por_fila = 1
 
while True:
    utilizados += por_fila
    if utilizados > bloques:
        break
 
    altura += 1
    por_fila += 1
 
 
print("La altura de la pirámide es de: ", altura)