# Prueba final de conceptos básicos de Python

# El significado de un argumento de palabra clave está determinado por su:
# tanto el nombre como el valor que se le asigna

# ¿Cuál es el comportamiento esperado del siguiente fragmento?
# try:
#   raise Exception
# except:
#   print("c")
# except BaseException:
#   print("a")
# except Exception:
#   print("b")
# El código causará un error.

# Seleccione las afirmaciones verdaderas. (Seleccione dos respuestas)
# Si una clase contiene el __init__método, no puede devolver ningún valor
# El primer parámetro de un método de clase no tiene que llamarse self
# Sabiendo que la función named f()reside en el módulo named m, y el código contiene la siguiente importdeclaración:
# from f import m
# Elija la forma correcta de invocar la función:

# La función no se puede invocar porque la importdeclaración no es válida

# ¿Cuál es el resultado esperado del siguiente fragmento?
# class X:
#   pass
  
# class Y(X):
#   pass
  
# class Z(Y):
#   pass
  
# x = X()
# z = Z()
# print(isinstance(x, Z), isinstance(z, X))
# False True

# ¿Cuál es el comportamiento esperado de la siguiente pieza de código?
# x = 16
# while x > 0:
#   print('*', end='')
#   x //= 2
# El código saldrá*****

# ¿Cuál es el comportamiento esperado del siguiente fragmento de código?
# my_list = [1, 2, 3, 4]

# my_list = list(map(lambda x: 2*x, my_list))
# print(my_list)
# El código saldrá2 4 6 8

# ¿Cuál es el comportamiento esperado de la siguiente pieza de código?
# d = {1: 0, 2: 1, 3: 2, 0: 1}
# x = 0

# for y in range(len(d)):
#   x = d[x]
  
# print(x)
# El código saldrá0

# ¿Qué línea invoca correctamente la función definida a continuación?
# def fun(a, b, c=0):
#   # function body
# fun(a=1, b=0, c=0)

# ¿Qué es PEP 8?
# Un documento que proporciona convenciones de codificación y una guía de estilo para el código de Python

# ¿Cuál es el comportamiento esperado del siguiente fragmento?
# def fun(x):
#   return 1 if x % 2 != 0 else 2
  
# print(fun(fun(1)))
# El programa generará1

# Si desea escribir el contenido de una matriz de bytes en una secuencia, ¿qué método puede usar?
# write()

# ¿Cuál es el resultado esperado del siguiente código?
# from datetime import timedelta

# delta = timedelta(weeks = 1, days = 7, hours = 11)
# print(delta)
# 14 days, 11:00:00

# 14.Es sun flujo abierto en modo lectura, la siguiente línea:

# q = s.readlines()
# asignará qcomo:

# lista

# ¿Cuál es el resultado esperado del siguiente fragmento?
# a = True
# b = False
# a = a or b
# b = a and b
# a = a or b
# print(a, b)
# True False

# ¿Cuál es el resultado esperado del siguiente código?
# t = (1, )
# t = t[0] + t[0]
# print(t)
# 2

# ¿Cuántas líneas vacías enviará el siguiente fragmento a la consola?
# my_list = [[c for c in range(r)] for r in range(3)]

# for element in my_list:
#   if len(element) < 2:
#     print()
# two

# ¿Cuál de las siguientes oraciones es verdadera sobre el fragmento a continuación?
# str_1 = 'string'
# str_2 = str_1[:]
# str_1y str_2son cadenas diferentes (pero iguales)

# ¿Cuál es el resultado esperado del siguiente código?
# import calendar

# c = calendar.Calendar(calendar.SUNDAY)

# for weekday in c.iterweekdays():
#   print(weekday, end=" ")
# 6 0 1 2 3 4 5

# ¿Cuál es el comportamiento esperado del siguiente código?
# x = """
# """
# print(len(x))
# El código saldrá1

# Si hay una finally:rama dentro del try:bloque, podemos decir que:
# la finally:rama siempre será ejecutada

# ¿Cuál es el resultado esperado del siguiente código?
# my_string_1 = 'Bond'
# my_string_2 = 'James Bond'

# print(my_string_1.isalpha(), my_string_2.isalpha())
# True False

# ¿Cuál es el resultado esperado del siguiente código?
# class A:
#   def a(self):
#     print('a')
    
# class B:
#   def a(Self):
#     print('b')
    
# class C(A, B):
#   def c(self):
#     self.a()
    
# o = C()
# o.c()
# El código se imprimiráa

# ¿Cuál es el resultado esperado del siguiente fragmento?
# print(len([i for i in range(0, -2)]))
# 0

# ¿Qué es cierto acerca de la siguiente línea de código?
# print(len((1, )))
# El código saldrá1

# ¿Cuál es el resultado esperado de la siguiente pieza de código si el usuario ingresa dos líneas que contienen 1y 2respectivamente?
# y = input()
# x = input()
# print(x + y)
# 21

# ¿Cuál es el resultado esperado del siguiente código?
# def fun(n):
#   s = ''
#   for i in range(n):
#     s += '*'
#     yield s
    
# for x in fun(3):
#   print(x, end='')
# ******

# ¿Con qué se sys.stdoutasocia normalmente la corriente?
# La pantalla

# ¿Cuál es el resultado esperado de ejecutar el siguiente código?
# class A:
#   def __init__(self):
#     pass
    
#   def f(self):
#     return 1
    
#   def g():
#     return self.f()
    
# a = A()
# print(a.g())
# El código generará una excepción.

# ¿Cuál es el resultado esperado del siguiente fragmento?
# d = {}
# d['2'] = [1, 2]
# d['1'] = [3, 4]

# for x in d.keys():
#   print(d[x][1]. end="")
# 24

# ¿Qué es cierto acerca de la siguiente pieza de código?
# print("a", "b", "c", sep="'")
# El código saldráa'b'c

# La Exceptionclase contiene una propiedad llamada args-qué es?
# una tupla

# ¿Qué hay de cierto en el siguiente fragmento?
# def fun(d, k, v):
#   d[k] = v
  
# my_dictonary = {}
# print(fun(my_dictionary, '1', 'v'))
# El código saldráNone

# ¿Cuál es el comportamiento esperado del siguiente fragmento?
# my_string = 'abcdef'

# def fun(s):
#   del s[2]
#   return s
  
# print(fun(my_string))
# El programa dará un error.

# ¿Cuál es el comportamiento esperado del siguiente código?
# x = "\"
# print(len(x))
# El código generará un error.

# ¿Cuál es el efecto esperado de ejecutar el siguiente código?
# class A:
#   def __init__(self, v):
#     self._a = v + 1
    
# a = A(0)
# print(a._a)
# El código saldrá1

# ¿Qué puede hacer si quiere decirles a los usuarios de su módulo que no se debe acceder directamente a una variable en particular ?
# Comienza su nombre con _o__

# ¿Cuáles de las siguientes funciones proporcionadas por el osmódulo están disponibles tanto en Windows como en Unix? (Seleccione dos respuestas)
# mkdir()
# chdir()
# Si el constructor de la clase se declara de la siguiente manera:
# class Class:
#   def __init__(self):
#     pass
# ¿Cuál de las asignaciones es válida?

# object = Class()

# ¿Cuál es el nombre del directorio/carpeta creado por Python utilizado para almacenar pycarchivos?
# __pycache__

# Un directorio/carpeta de paquete puede contener un archivo destinado a inicializar el paquete. ¿Cual es su nombre?
# __init__.py

# ¿Cuántas estrellas ( *) enviará el siguiente fragmento a la consola?
# i = 4

# while i > 0:
#   i -= 2
#   print("*")
#   if i == 2:
#     break
    
# else:
#   print("*")
# una

# ¿Cuál es el resultado esperado del siguiente código?
# class A:
#   A = 1
#   def __init__(self):
#     self.a = 0
    
# print(hasattr(A, 'A'))
# True

# ¿Cuál es el resultado esperado del siguiente código, ubicado en el archivo module.py?
# print(__name__)
# __main__

# ¿Qué operación de pip usaría para verificar que los paquetes de Python se hayan instalado hasta ahora?
# list

# ¿Cuál es el resultado esperado del siguiente código?
# def a(x):
#   def b():
#     return x + x
#   return b
  
# x = a('x')
# y = a('')
# print(x() + y())
# xx

# ¿Cuál es el resultado esperado de la siguiente pieza de código?
# x, y, z = 3, 2, 1
# z, y, x = x, y, z
# print(x, y, z)
# 1 2 3

# ¿Qué valor se le asignará a la xvariable?
# z = 2
# y = 1
# x = y < z or z > y and y > z or z < y
# True

# ¿Cuál es el resultado esperado del siguiente fragmento?
# d = {'one': 1, 'three': 3, 'two': 2}

# for k in sorted(d.values()):
#   print(k, end=' ')
# 1 2 3

# ¿Cuál es el resultado esperado del siguiente código?
# d = {}
# class A:
#   A = 1
#   def __init__(self, v=2):
#     self.v = v + A.A
#     A.A += 1
    
#   def set(self, v):
#     self.v += v
#     A.A += 1
#     return
    
# a = A()
# a.set(2)
# print(a.v)
# 5

# ¿Cuál es el resultado esperado del siguiente código?
# from datetime import datetime

# datetime = datetime(2019, 11, 27, 11, 27, 22)
# print(datetime.strftime('%Y/%m/%d %H:%M:%S'))
# 2019/11/27 11:27:22

# ¿Cuál es el comportamiento esperado del siguiente código?
# import os

# os.makedirs('pictures/thumnails')
# os.rmdir('pictures')
# El código generará un error.

# ¿Cuál es el resultado esperado del siguiente fragmento?
# class A:
#   def __init__(self,name):
#     self.name = name
    
# a = A("class")
# print(a)
# Una cadena que termina con un número hexadecimal largo

# ¿Cuál es el resultado esperado del siguiente fragmento?
# try:
#   raise Exception
# except BaseException:
#   print("a", end='')
# else:
#   print("b", end='')
# finally:
#   print("c")
# ac

# ¿Cuál es el resultado esperado del siguiente fragmento?
# t = (1, 2, 3, 4)
# t = t[-2:-1]
# t = t[-1]
# print(t)
# 3

# ¿Qué operador usarías para verificar si dos valores son iguales ?
# ==

# ¿Cuál es el resultado esperado del siguiente código?
# class A:
#   pass
  
# class B:
#   pass
  
# class C(A, B):
#   pass
  
# print(issubclass(C, A) and issubclass(C, B))
# El código se imprimiráTrue

# ¿Cuál es el resultado esperado del siguiente código?
# v = 1 + 1 // 2 + 1 / 2 + 2
# print(v)
# 3.5

# ¿Qué es cierto sobre el siguiente fragmento de código?
# def fun(par2, par1):
#   return par2 + par1
  
# print(fun(par2=1, 2))
# el codigo es erroneo

# Seleccione las afirmaciones verdaderas. (Seleccione dos respuestas)
# PyPI es la abreviatura de Python Package Index
# # PyPI es uno de los muchos repositorios existentes de Python