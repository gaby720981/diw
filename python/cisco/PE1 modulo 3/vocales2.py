

from ast import Continue

user_word = (input ("Ingrese una palabra: ")).upper()

word_without_vowels = " " 

for letter in user_word:
    if letter == "A":
        Continue
    elif letter == "E":
        Continue
    elif letter == "I":
        Continue
    elif letter == "O":
        Continue
    elif letter == "U":
        Continue
    else:
        word_without_vowels += letter
print (word_without_vowels)