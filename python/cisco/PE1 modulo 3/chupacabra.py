secret = input ("Ingrese la palabra secreta: ")

while True:
    if secret != "chupacabra":
        secret = input ("Ingrese la palabra secreta: ")
    if secret == "chupacabra":
        break 
print ("¡Has dejado el bucle con éxito!")
