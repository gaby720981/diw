
#Diseñe un algoritmo. Se ingresan N cantidad de números por teclado. 
#Contar cuántas veces se ingresaron los números 8 y 11 y cuántos números distintos a estos se presentan. 
#El proceso finaliza cuando se ingresa 0.

n = int(input ("Ingrese un número o presione 0 para finalizar: "))

while n != 0:
    num = []
    num.append(n)
    n = int(input ("Ingrese un número o presione 0 para finalizar: "))

print (num)

ocho_once = []

for n in num:
    if (n==8 or n==11):
        ocho_once.append(n)
        x = len(ocho_once)
print(f"Los números 8 y 11 se ingresaron {x} veces")

