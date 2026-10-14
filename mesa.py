class Mesa:
    def __init__(self, numero, ubicacion, capacidad):
        if numero <= 0:
            raise ValueError('El numero debe ser mayor a cero')
        if capacidad <= 0:
            raise ValueError('La capacidad de la mesa debe ser mayor a cero')

        self.numero = numero
        self.ubicacion = ubicacion
        self.capacidad = capacidad

    def informacion_mesa(self):
        return f'La mesa numero {self.numero} tiene una capacidad de {self.capacidad} y esta ubicada en {self.ubicacion}'