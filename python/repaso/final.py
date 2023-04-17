# CUAL ES EL RESULTADO DEL STE CODIGO?
def fun (n):
    s = ''
    for i in range (n):
        s += '*'
        yield s

for x in fun (3):
    print (x, end = '')

# ******



#QUE ES VERDADERO SOBRE EL STE FRAGMENTO DE CODIGO?

print("a", "b", "c", sep = " ' ")

# a ' b ' c

z = 2
y = 1

x = y<z or z>y and y>z or z<y #(primero resuelve el and)

print (x)

print(sorted([4, 1, 3, 2])) #ordena

print("******************************")

class A:
    def __init__(self,name):
        self.name = name

a = A ("class")
print(a)

#<__main__.A object at 0x0000025EF945BD90>


