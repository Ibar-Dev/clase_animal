# Crea una clase base llamada Animal con atributos nombre y tipo. 
# La clase debe tener un método llamado hacer_sonido que no hace nada en la clase base.

# Deriva dos clases, Perro y Gato, de la clase Animal. Implementa el método hacer_sonido en
#  ambas clases para que devuelva sonidos característicos de perros y gatos, respectivamente.
# Crea instancias de ambas clases y muestra sus nombres junto con los sonidos que hacen.


class Animal():
    def __init__(self, nombre, tipo) -> None:
        self.nombre = nombre
        self.tipo = tipo
    
    def hacer_sonido(self):
        pass


class Perro(Animal):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)

    
    def mostrar_nombre(self):
        return self.nombre
    
    def mostrar_tipoRaza(self):
        return self.tipo
    

    def hacer_sonido(self):
        return 'guau'



perro  = Perro('Sam', 'Labrador')

print(perro.mostrar_nombre())

print(perro.mostrar_tipoRaza())

print(perro.hacer_sonido())

print('\n')


class Gato(Animal):
    def __init__(self, nombre, tipo) -> None:
        super().__init__(nombre, tipo)

    
    def mostrar_nombre(self):
        return self.nombre
    
    def mostrar_tipoRaza(self):
        return self.tipo
    

    def hacer_sonido(self):
        return 'Miauh'
    
gato = Gato('Michi', 'Persa')


print(gato.mostrar_nombre())

print(gato.mostrar_tipoRaza())

print(gato.hacer_sonido())
