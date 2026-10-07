from mesa import Mesa
from plato import Plato
from bebida import Bebida
from pedido import Pedido


def main():
    print("---INICIO DEL SISTEMA DE GESTIÓN DE RESTAURANTE---")

    mesa1 = Mesa(1, "Planta Baja", 4)
    mesa2 = Mesa(2, "Terraza", 2)

    plato1 = Plato(
        "Milanesa Napolitana",
        8500,
        False,
        "Papas Fritas",
        "Principal",
        False
    )

    plato2 = Plato(
        "Ensalada Caesar",
        6200,
        False,
        "crutones",
        "Entrada",
        False
    )

    plato1.añadir_ingredientes("Huevo frito")
    plato1.quitar_ingredientes("Cebolla")

    bebida1 = Bebida("Coca Cola", 2500, 500)
    bebida2 = Bebida("Pepsi", 3800, 750)

    print("---CREANDO Y PROCESANDO PEDIDO MESA 1---")

    pedido_mesa1 = Pedido(mesa1)

    pedido_mesa1.agregar(plato1)
    pedido_mesa1.agregar(bebida1)
    pedido_mesa1.agregar(bebida2)

    print("Estado inicial del pedido:")
    pedido_mesa1.mostrar_pedido()

    print("---MODIFICANDO PEDIDO---")

    pedido_mesa1.eliminar_producto(bebida1)

    print("Estado actualizado del pedido:")
    pedido_mesa1.mostrar_pedido()


main()