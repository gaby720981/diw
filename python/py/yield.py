def generator():

   yield "Welcome"

   yield "to"

   yield "Simplilearn"

gen_object = generator()

print(type(gen_object))

for i in gen_object:

   print(i)


def filter_odd(numbers):

   for number in range(numbers):

       if(number%2!=0):

           yield number 

odd_numbers = filter_odd(20)

print(list(odd_numbers))

def fun (n):
    s= ''
    for i in range (n):
        s += '*'
        yield s

for x in fun (3):
    print (x, end ='')

    