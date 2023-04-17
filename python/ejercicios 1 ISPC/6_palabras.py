#Diseñe un algoritmo que permita ingresar una N cantidad de palabras. El programa se debe finalizar
#al ingresar “a” y mostrar en pantalla la cantidad de palabras ingresadas que comienzan con la letra “m”.

word = input("ingrese una palabra :")
words = []
mWords = 0

while word != "a":

    if word[0] == "m":
        mWords += 1
        
    words.append(word)
    word = input("ingrese una palabra :")


print(words)
print(f"la cantidad de palabras que inician con m es : {mWords}")