#```py

#Diseñar un algoritmo que muestre los resultados de encuestas. 
# Se deben encuestar a 7 personas que opinen sobre la situación económica del país. 
# Las posibles respuestas son: mejorando, regular, muy mala. 
# Las respuestas almacenarla en una lista y mostrar los resultados obtenidos, por ejemplo:

# Mejorando: 3
# Regular: 1
# Mala: 3


mejorando = 0
regular = 0
mala = 0

encuesta = input ("""\nQué opinas sobre la situación económica?

a) Mejorando
b) Regular
c) Mala 

Ingrese la opción correspondiente: """)

while (int(mejorando + regular + mala)) < 7:
    encuesta = input ("""\nQué opinas sobre la situación económica?
    
a) Mejorando
b) Regular
c) Mala 

Ingrese la opción correspondiente: """)
    if (encuesta == "a"):
        mejorando +=1
    elif (encuesta == "b"):
        regular +=1
    else:
        mala +=1

print(f"""\nResultados de la encuesta:

a) Mejorando:  {mejorando}
b) Regular:  {regular}
c) Mala: {mala} """)
#```
    