# Demonstrando el método index():
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# El método index() busca la secuencia desde el principio, 
# para encontrar el primer elemento del valor especificado en su argumento.

# El método devuelve el índice de la primera aparición del argumento,
# (lo que significa que el resultado más bajo posible es 0, mientras que el más alto es la longitud del argumento decrementado en 1).