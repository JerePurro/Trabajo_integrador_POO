
class Producto:
    def __init__(self, nombre, precio):
        if not isinstance(nombre, str):
            raise TypeError("El nombre del producto debe ser un texto válido.")
        self.nombre = nombre
        if not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser un número.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = precio

    def obtener_informacion(self):
        return f'El producto {self.nombre} posee un precio de ${self.precio}'