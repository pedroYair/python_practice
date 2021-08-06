""" MAP: aplica a una lista la funcion pasada como parametro, retornando una nueva lista con
 los resultados. Util cuando de requiere trabajar con un gran numero de datos.
"""


def multiplicar(numero):
  return numero * 5


lista = [1, 2, 3, 4, 5]
lista2 = list(map(multiplicar, lista))
print(lista2)

""" puede tener multiples listas de acuerdo al numero de parametros que requiere la funcion a aplicar
"""

# los elementos de la primera lista seràn usandos como base
# los elementos de la segunda lista seràn usados como exponentes
lista3 = list(map(pow, lista, lista2))
print(lista3)