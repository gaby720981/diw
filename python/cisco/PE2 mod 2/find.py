# El método find(), busca una subcadena y devuelve el índice de la primera aparición de esta subcadena, pero:

# Es más seguro que index(), no genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
# Funciona solo con cadenas - no intentes aplicarlo a ninguna otra secuencia.

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

