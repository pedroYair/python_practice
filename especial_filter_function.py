""" FILTER: aplica a una lista la funcion pasada como parametro, retornando una nueva lista
con los valores que satisfacen la condicion establecida en la funcion
https://entrenamiento-python-basico.readthedocs.io/es/latest/leccion5/funciones_orden_superior.html
"""


def par(numero):

    if numero % 2 == 0:
        return True
    else:
        return False


lista = list(filter(par, [1, 2, 3, 4, 5, 6, 7, 8]))
print(lista)

# filtrar valores nulos o equivalentes a false

objects = [0, 1, [], 4, 5, "", None, 8]
lista2 = list(filter(lambda x: x, objects))
print(lista2)

# otra forma de hacer lo anterior
lista2 = list(filter(None, objects))
print(lista2)

