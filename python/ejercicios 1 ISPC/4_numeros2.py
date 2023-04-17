numbers = []
others = []
n = 1
while n!=0:
     n = int(input("Ingresa un numero o 0 para salir: "))
     if n in [8,11]:
          numbers.append(n)
     else:
          others.append(n)


print("Numeros 8 y 11: ",len(numbers),"\nOtros:",len(others))