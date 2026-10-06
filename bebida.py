from producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, capacidad):
        super().__init__(nombre, precio)
        if capacidad <= 0:
            raise ValueError('La capacidad no puede ser menor o igual a cero')
        
        self.capacidad = capacidad

    def obtener_informacion(self):
        return f'La bebida {self.nombre} de {self.capacidad} ml posee un precio final de {self.precio}'