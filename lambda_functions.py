"""FUNCIONES LAMBDA: tambien llamadas funciones anonimas permiten simplificar las funciones en
 unas pocas lineas de codigo. Usualmente se crean para ser pasadas como argumentos en funciones de orden
  superior como filter y map
"""

doblar = lambda numero: numero * 2
print(doblar(10))

lista = [1, 2, 3, 4, 5]
lista4 = [1, 2, 3, 4, 5]

# con la funcion map
# mediante map aplicamos a cada elemento de la lista la funcion anonima doblar
lista2 = map(doblar, lista)
print(list(lista2))

# se multiplican los elementos de cada lista segun su posicion
print(list(map(lambda x, y: x*y, lista, lista4)))

# con la funcion filter

par = lambda numero: numero % 2 == 0
# aplicamos la funcion como filtro a la lista
lista3 = filter(par, lista)
print(list(lista3))