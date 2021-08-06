import re

"""
    Con la función match podemos comprobar si una expresión regular coincide con el inicio de una cadena
    
    match(expresiónregular, cadena, [flag])

    Valores en Flag:

    re.IGNORECASE: no distingue entre mayúsculas y minúsculas.
    Re.VERBOSE: ignora comentaros y espacios en la expresión.
"""

palabra1 = 'taza'
palabra2 = 'tazas'
palabra3 = 'casa'

# verificar si la primera cadena coincide con el inicio de la segunda
if re.match(palabra1, palabra2):
    print('palabra1 y palabra2 coinciden')
else:
    print('palabra1 y palabra2 no coinciden')

if re.match(palabra1, palabra3):
    print('palabra1 y palabra3 coinciden')
else:
    print('palabra1 y palabra3 no coinciden')

# el punto indica que antes de 'aza' puede venir cualquier caracter (pero solo uno) a expecion de \n
if re.match('.aza', palabra1):
   print('palabra1 termina en aza')
else:
   print('palabra1 no termina en aza')


# CARACTERES ESPECIALES

# Los caracteres especiales que queremos validar debemos escribirla luego de una barra invertida “\”.
# en este caso el punto hace referencia a la extension pdf

ext = '\.pdf'
if re.match(ext, '.pdf'):
   print('El archivo es de formato pdf')

# agrupaciones y variaciones

extensiones = ['pdf', 'jpg', 'doc', 'txt', 'flv']
for tipoarchivo in extensiones:
    if re.match('pdf|doc|txt', tipoarchivo):
       print('La extensión ', tipoarchivo, ' es un formato de texto')
    else:
       print('La extensión ', tipoarchivo, 'no es un formato de texto')


palabras = ['computadora', 'compañera', 'compota', 'compara', 'camisa', 'compromiso']
for termino in palabras:
    if re.match('com(...|.)a', termino):
       print(termino)

codigo = 'cod1'
if re.match('...\d', codigo):
   print("Es una cadena válida porque termina con un digito")
else:
   print("No es una cadena válida porque termina con un digito")

codigo = "@cod"
if re.match('\W', codigo):
   print ('Es una cadena valida porque comienza con carácter no alfanumérico')
else:
   print ('no es una cadena valida porque no comienza con carácter no alfanumérico')