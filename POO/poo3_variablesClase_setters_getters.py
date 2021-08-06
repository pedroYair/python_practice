# variables de clase: disponibles para todos los objetos de la clase, se accede a ella con la
# sintaxis NombreClase.nombreVariable

class Estudiante:

    # esta es una variable de clase
    colegio = "Institucion educativa"

    def __init__(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def __str__(self):
        return "{} - {} - {} años".format(Estudiante.colegio, self.nombre, self.edad)


# e1 = Estudiante()
# print(e1)

""" en python los atributos y metodos son accedidos publicamente, para dar una especie de solucion al problema
 de encapsulamiento se pueden agregar los siguientes decoradores:

@property para leer el valor de un atributo.
@name.setter para escribir el valor de un atributo.

de esta forma el acceso no es directo con los atributos
"""


class Droid:
    def __init__(self, nombre, peso):
        self.hidden_nombre = nombre
        self.peso = peso

    # getter
    @property
    def nombre(self):
        print('inside the getter')
        return self.hidden_nombre

    # setter
    @nombre.setter
    def nombre(self, nombre):
        print('inside the setter')
        self.hidden_nombre = nombre

    # getter valor calculado (se accede como una propiedad de la clase)
    @property
    def peso_triple(self):
        return 3 * self.peso


d1 = Droid("pedro", 30)
# print(d1.nombre)

d1.nombre = "samir"
# print(d1.nombre)
# print(d1.peso_triple)

"""OCULTANDO ATRIBUTOS: es otra forma de privatizar atributos, consiste en colocar doble gion antes del nombre del atributo, pero lo que en realidad cambia es la forma en que se debe acceder al mismo, ya que anteponiendo el nombre de la clase el valor del atributo puede ser accedido"""


class Usuario:

    def __init__(self, nombre):
        self.__nombre = nombre


u1 = Usuario("abc")
# print(u1.__nombre) mostrará error diciendo que el atributo no existe
# print(u1._Usuario__nombre) # se antepone el nombre de la clase

"""METODOS DE CLASE: modifican el comportamiento de la clase a la que hace referencia
  METODOS ESTATICOS: no modifican ni objetos ni clases, no reciben argumentos, pueden ser llamados sin 
  necesidad de crear una instancia de la clase"""


class Animal:
    count = 0

    def __init__(self, nombre):
        Animal.count += 1
        self.nombre = nombre

    @classmethod
    def total_instancias(cls):
        print(f'{cls.count} droids built so far!')

    @staticmethod
    def metodoEstatico():
        print("metodo estatico")


a1 = Animal("kinito")
a2 = Animal("toby")
a1.metodoEstatico()
Animal.metodoEstatico()
Animal.total_instancias()