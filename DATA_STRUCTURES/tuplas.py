"""
Una tupla es una secuencias ordenadas de objetos de distintos tipos.

Se construyen poniendo los elementos entre corchetes ( ) separados por comas.

Se caracterizan por:

Tienen orden.
Pueden contener elementos de distintos tipos.
Son inmutables, es decir, no pueden alterarse durante la ejecución de un programa.

"""

# creacion

a = [1, 2, 3]
tupla1 = tuple(a) # conversion lista a tupla
print(tupla1)

tupla2 = (0, 2, 3)
print(tupla2)

tupla3 = tuple("Python") # cada caracter serà un elemento de la tupla
print(tupla3)

# slicing

print(tupla3[2])
print(tupla3[0:3])
print(tupla3[::2])
print(tupla1[-1])

b = ((1, 2, 3), (4, 5, 6))
print(b[0])
print(b[0][2])

# busqueda

print(0 in tupla2)
print(tupla3.index("P"))

# tamaño
print(len((1, "a", 3.14)))

# contar apariciones de un valor
valores = ("Python", True, "Zope", 5)
print(valores.count(True))

# concatenacion

tupla4 = tupla1 + tupla2
print(tupla4)
