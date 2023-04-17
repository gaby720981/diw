#El método endswith() comprueba si la cadena dada termina con el argumento especificado 
# y devuelve True(verdadero) o False(falso), dependiendo del resultado.

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demostración del método endswith():
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
