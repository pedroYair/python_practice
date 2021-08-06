"""
Algunas particularidades de POO en Python son las siguientes:

Todo es un objeto, incluyendo los tipos y clases.

Permite herencia múltiple.

No existen métodos ni atributos privados.

Los atributos pueden ser modificados directamente.

Permite «monkey patching: consiste en modificar el código en tiempo de ejecución. Esto quiere decir que en lugar
de modificar el código fuente de una clase, por ejemplo, en tiempo de ejecución asignamos otra función a ese
 método y todas las llamadas posteriores en lugar de ejecutar el código definido en la clase ejecutarán el
código "parcheado".

Permite «duck typing»: consiste en que si un determinado objeto tiene los métodos que nos interesan, nos basta,
 siendo su tipo irrelevante.

Permite la sobrecarga de operadores.

Permite la creación de nuevos tipos de datos.

https://fide.dev/2019/09/07/metodos-especiales-en-python/

"""


class Persona:

    def __init__(self, nombre, edad, sexo='M'):
        """constructor de la clase"""
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.colores = []

    def __str__(self):
        """Devuelve una representación orientada al usuario final, es la manera “informal” de representar la clase"""
        return "{} - {} de {}. Colores: {}".format(self.sexo, self.nombre, self.edad, self.colores)

    def __repr__(self):
        """Es una representación “formal” de cómo se genera el objeto"""
        return 'Persona({}, {}, {}, {})'.format(self.nombre, self.edad, self.sexo, self.colores)

    def __len__(self):
        """Permite obtener el tamaño de la lista colores"""
        return len(self.colores)

    def __getitem__(self, ix):
        """Permite iterar sobre la lista colores"""
        return self.colores[ix]

    def __add__(self, otro):
        """Permite definir el resultado de concatenar dos objetos de la clase Persona"""
        nombre = "{} & {}".format(self.nombre, otro.nombre)
        edad = self.edad + otro.edad
        sexo = self.sexo + " " + otro.sexo
        nuevo = Persona(nombre, edad, sexo)
        nuevo.colores = self.colores + otro.colores
        """ la concatenacion de objetos iterables debe venir despues de que se creo el objeto contenedor 
        (en este caso nuevo)"""

        return nuevo

    # __del__: se usa para gestionar las instrucciones a ejecutar cuando se vaya a destruir el objeto

    # __cmp__: se usa para comparar objetos, una vez definido si se crea una lista de objetos de esta clase, al
    # aplicar el metodo sort a la lista, el criterio de ordenamiento será el definido en el metodo __cmp__

    def agregar_color(self, color):
        self.colores.append(color)


p1 = Persona("pedro", 23)
print(p1)
print("{} de {}".format(p1.nombre, p1.edad))
print(repr(p1))

print("--------------------")

p1.agregar_color("azul")
print(p1)

print("--------------------")

p1.agregar_color("rojo")
print(p1)
print(len(p1.colores))  # tambien puede ser len(p1) dará el mismo resultado
print(p1.colores[0])  # tambien puede ser p1[0], dará el mismo resultado

print("-------------")

for color in p1.colores:
    print(color)

print("-------------")

p2 = Persona("samir", 24)
p2.agregar_color("negro, gris")
print(p2)

p3 = p1 + p2
print(p3)
