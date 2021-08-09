
"""
https://docs.python.org/es/3/tutorial/introduction.html#lists
https://aprendeconalf.es/docencia/python/manual/listas/

    - las listas pueden contener elementos de cualquier tipo incluso otras listas

    - si asignamos una lista a una nueva variable las modificaciones que hagamos en esta nueva se veràn
    reflejados en la lista original.

    - El signo de igualdad = se puede utilizar para construir un duplicado de una lista. Sin embargo, la
     nueva lista estará vinculada a la existente. Esto significa que la nueva lista también se verá alterada
      si se actualiza la lista original. La nueva lista se refiere a un elemento similar a la lista antigua.

"""

# creacion

squares = [1, 4, 9, 16, 25]
a = list("Python")
print(a)

# slicing: retorna una nueva lista cuando se devuelve mas de un elemento
print(squares[2])
print(squares[-1]) # obtener el valor de la ultima posicion
print(squares[2:4]) # obtener en una nueva lista los elementos de la posicion 2 a la 3
print(squares[1:]) # obtener los elementos de la posicion 1 en adelante
print(squares[-3:]) # obtener los elementos de la posicion -3 en adelante
print(a[0:4:2]) # obtener elementos de la posicion 0 a la 3 saltando de dos en dos

# concatenacion

squares = squares + [30, 31, 32, 33]
print(squares)

# asignando y reemplazando valores

squares[1] = 0
squares[2:5] = [1, 1, 1]
print(squares)

squares[2:5] = [] # remover elementos
print(squares)

# operaciones
print(min(squares))
print(max(squares))
print(sum(squares))
print(1 in squares) # verificar si un elemento pertenece a la lista
print(a.index("P")) # obtener el indice de un elemento
squares.append(0)
print(squares.count(0)) # contar cuantas veces aparece un elemento
print(all(squares)) # devuelve true si todos los elementos son valores equivalentes a true, false en caso contrario
print(any(squares)) # devuelve true si alguno de los elementos es equivalente a true, false en caso contrario

# copiando listas

# usando copy

fruits_spring = ['carrots', 'kiwi', 'grapes', 'cherry']
fruits_summer = fruits_spring.copy()
print(fruits_summer)

# usando slicing
fruits_summer2 = fruits_spring[:]
print(fruits_summer2)

# usando el metodo list
fruits_summer3 = list(fruits_spring)
print(fruits_summer3)

# usando comprension de listas
fruits_summer4 = [i for i in fruits_spring]
print(fruits_summer4)

# prueba
fruits_spring.append("pear")
print(fruits_spring)
print(fruits_summer)

# usando el modulo copy
import copy

nueva_lista = copy.copy(fruits_spring)
print(nueva_lista)

# cuando la lista contiene elementos mutables (ej: otra lista) si accedemos a ese elemento y lo cambiamos en la
# lista original ese cambio se reflejarà en las copias, en este caso podemos usar una copia profunda:

original_list = [['carrots', "apple"], 'kiwi', 'grapes', 'cherry']
copia = original_list.copy()
print(copia)

original_list[0][0] = "nothing"
print(copia)

# haciendo copia profunda
copia = copy.deepcopy(original_list)
original_list[0][0] = "---"
print(copia)


