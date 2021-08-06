
class Persona:

    def __init__(self):

        nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

        if nombre != "":
            self.nombre = nombre
        else:
            raise Exception('El nobre no puede ser una cadena vacia')

    def __str__(self):
        return 'Soy {} y tengo {} años'.format(self.nombre, self.edad)

    def mensaje(self):
        print("mensaje desde la clase Persona")


# p1 = Persona("pedro", 27)
# print(p1)

# p2 = Persona("samr", 'sd')

# creando la clase derivada o concreta

class Docente(Persona):

    def __init__(self):
        Persona.__init__(self)
        self.materia = str(input("\nIngrese la materia: "))

    def __str__(self):
        return '\nSoy el docente {}, tengo {} años y doy clases de {}'.format(self.nombre, self.edad, self.materia)

    # aplicando polimorfismo al sobreescribir la el metodo heredado
    def mensaje(self):
        print("mensaje desde la clase Docente")


# p3 = Persona()
# print(p3)

# d1 = Docente()
# print(d1)

# Herencia multiple

class Telefono:

    def __init__(self):
        self.marca = input("Ingrese la marca del telefono: ")


class Camara:

    def __init__(self):
        self.mpx = input("Ingrese los mpx: ")


class Memoria:

    def __init__(self):
        self.memoria = input("Ingrese la capacidad: ")


class Movil(Telefono, Camara, Memoria):

    def __init__(self):
        Telefono.__init__(self)
        Camara.__init__(self)
        Memoria.__init__(self)
        self.precio = input("Ingrese el precio: ")

    def __str__(self):
        return "{} - {} - {} - {}".format(self.marca, self.precio, self.mpx, self.memoria)


m1 = Movil()
print(m1)