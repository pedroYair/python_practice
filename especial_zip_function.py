"""
Funcion zip: crea grupos de tuplas a partir de los iterables que se le pasan como parametro
la primera tupla esta compuesta por el primer elemento de cada iterable y asi sucesivamente
https://realpython.com/python-zip-function/

    - si se pasa un solo iterador se generaran tuplas de un solo elemento (1, )

    - si los iterables no tienen la misma longitud la cantidad de tuplas generadas serà el tamaño del
    iterable mas corto. este problema se puede solucionar usando zip_longest

    - En Python 2, zip() devuelve una listde tuplas en python3 un iterable
"""
from itertools import zip_longest

numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
zipped = zip(numbers, letters)
zipped = list(zipped)
print(zipped)

# en este caso los iterables no tienen sus elementos en un orden en particular por lo que
# las tuplas generadas se crean aleatoriamente
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}
print(list(zip(s1, s2)))

# crear tuplas con iterables de tamaño desigual, rellenando los espacios vacios
letters = ['a', 'b', 'c']
numbers = range(5)
nombres = ["pedro", "yair"]
zipped2 = list(zip_longest(letters, numbers, nombres, fillvalue="*"))
print(zipped2)
