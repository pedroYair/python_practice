
"""
Un Diccionario es una estructura de datos y un tipo de dato en Python con características especiales que nos
 permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos
 diccionarios nos permiten además identificar cada elemento por una clave (Key).

 - las key no necesariamente deben ser del mismo tipo
 - un diccionario es un tipo de datos mutable por lo que pasa lo mismo que con las listas si sacamos
 una "copia"  mediante asignacion directa (dir2 = dir1)

"""

diccionario = {'nombre': 'Carlos', 'edad': 22, 'cursos': ['Python', 'Django', 'JavaScript']}

print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])
print(diccionario['cursos'][1])

# recorrer diccionario

for key in diccionario:
  print(key, ":", diccionario[key])

# imprimir solo los valores
for val in diccionario.values():
  print(val)

# imprimir solo las keys
for key in diccionario.keys():
  print(key)

print("-----------------")

# imprimir keys y valores
for clave,valor in diccionario.items():
    print(clave, valor)

print("-----------------")

# metodos

# dict permite crear diccionarios a partir de otros objetos

dic = dict(nombre='nestor', apellido='Plasencia', edad=22)
print(dic)

dic = dict(zip('abcd', [1, 2, 3, 4])) # los primeros elementos seràn tomados como keys
print(dic)

# Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el
# segundo, su valor.
print(dic.items())

# devuelve una lista compuesta por las keys del diccionario
print(dic.keys())

# vaciar diccionario
dic.clear()
print(dic)

# copiar diccionario
# OJO si el diccionario contiene elementos mutables lo mejor es hacer una copia profunda (VER LISTAS)
dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dic1 = dic.copy()
print(dic1)

# crear diccionario a apartir de una lista de keys
dic2 = dict.fromkeys(['a', 'b', 'c', 'd'], 1) # cada key tendrà como valor el 1, sino se ingresa valor
# coloca none
print(dic2)

# obtener el valor de una key
# Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.
print(dic2.get('c'))

# eliminar elemento segun la key (elimina y devuelve el valor eliminado)
valor = dic2.pop('b')
print(dic2, valor)

# agregar nuevo elemento al diccionario

dic2['e'] = 12
print(dic2)

dic2.setdefault('f', 5)
print(dic2)

# concatenar o actualizar diccionarios .Si se tienen claves iguales, actualiza el valor de la clave repetida

dic1 = {1: 2, 2: 1, 4: 0}
dic2 = {'a': 0, 2: 0, 3: 22, 'b': 10}
dic1.update(dic2)
print(dic1)

# verificar si existe una key

print('a' in dic1)