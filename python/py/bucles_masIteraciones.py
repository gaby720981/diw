frutas = ["banana", "manzana", "durazno", "ciruela", "uva", "sandía", "pera"]

# for fruta in frutas:
#     if fruta == "manzana":
#         continue
#     print(f"Me voy a comer una {fruta}")

#evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if fruta == "uva":
        break


numeros = [2, 4, 6, 8]

#for en una linea de codigo
numeros_duplicados = [x*2 for x in numeros]
print (numeros_duplicados)
