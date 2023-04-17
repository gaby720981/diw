class Pato:
    def hablar(self):
        print("¡Cua!, Cua!")

p = Pato()

p.hablar()

class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")

def llama_hablar(x):
    x.hablar()

llama_hablar(Perro())
llama_hablar(Gato())
llama_hablar(Vaca())

lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()



class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# Sample class with init method
class Person:

	# init method or constructor
	def __init__(self, name):
		self.name = name

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)


p = Person('Nikhil')
p.say_hi()

