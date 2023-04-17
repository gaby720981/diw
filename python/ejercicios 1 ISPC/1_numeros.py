#Diseñe un algoritmo que permita ingresar una N cantidad de números. El programa se debe finalizar al ingresar 0 
#y al finalizar mostrar en pantalla la cantidad de números ingresados.

number = int(input("Ingrese un número o presione 0 para finalizar: "))

num_list =[]

while number != 0:
    num_list.append(number)
    number = int(input("Ingrese un número o presione 0 para finalizar: "))
print (len(num_list))
