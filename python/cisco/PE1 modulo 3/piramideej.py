bloques = int(input("Ingrese el número de bloques:"))
altura=0
nivel=1
while nivel<=bloques:
    bloques-=nivel
    nivel+=1
    altura+=1
 
 
print("La altura de la pirámide:", altura)