from bebida import Bebida
from mesa import Mesa
from plato import Plato
from producto import Producto


class Pedido:

    def __init__(self, mesa):
        if not isinstance(mesa, Mesa):
            raise TypeError(
                "El parametro mesa debe ser una instancia de la clase Mesa"
            )
        self.mesa = mesa
        self.productos = []

    def agregar(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError(
                "Solo se pueden agregar objetos que vengan de la clase Producto"
            )
        self.productos.append(producto)
        print(
            f"Se agrego {producto.nombre} al pedido de la mesa {self.mesa.numero}"
        )

    def eliminar_producto(self, producto):
        for elemento in self.productos:
            if elemento.nombre == producto or elemento == producto:
                self.productos.remove(elemento)
                print(f"Se ha eliminado {elemento.nombre} del pedido.")
                return
        raise ValueError(
            f"El producto {producto} no se encuentra en el pedido."
        )

    def calcular_total(self):
        total = 0
        for prod in self.productos:
            total += prod.precio
        return total

    def mostrar_pedido(self):
        if len(self.productos) == 0:
            resumen_productos = "No hay productos agregados todavia"
        else:
            resumen_productos = ""
            for producto in self.productos:
                resumen_productos += (
                    f"\n - {producto.obtener_informacion()}"
                )

        print("PEDIDO")
        print(f"Mesa {self.mesa.informacion_mesa()}")
        print(f"Productos registrados: {resumen_productos}")
        print(f"Total a pagar: ${self.calcular_total()}")