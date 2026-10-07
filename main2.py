from mesa import Mesa
from plato import Plato
from bebida import Bebida
from pedido import Pedido

print('Bienvenido al Sistema de gestion')
def main2():
    mesa1 = Mesa(1, "Planta Baja", 4)
    mesa2 = Mesa(2, "Terraza", 2)
    
    plato1 = Plato("Milanesa Napolitana", 8500, False, "Papas Fritas", "Principal", False)
    plato2 = Plato("Ensalada Caesar", 6200, True, "crutones", "Entrada", False)

    bebida1 = Bebida("Coca Cola", 2500, 500)
    bebida2 = Bebida("Pepsi", 3800, 750)

    while True:
        print('Mesas:')
        print(f'Mesa 1: {mesa1.informacion_mesa()}')
        print(f'Mesa 2: {mesa2.informacion_mesa()}')
        mesa_seleccionada = int(input('Opcion: '))
        match mesa_seleccionada:
            case 1:
                print(f'Se ha seleccionado la mesa N 1: {mesa1.informacion_mesa()}')
                pedido_mesa = Pedido(mesa1)
            case 2:
                print(f'Se ha seleccionado la mesa N 2: {mesa2.informacion_mesa()}')
                pedido_mesa = Pedido(mesa2)
            case _:
                print('Opcion invalida.')
                continue
        print('Opciones:')
        print('1. Hacer un pedido')
        print('2. Salir')
        opcion = int(input('Selecciona la opcion: '))
        if opcion == 1:
            print('Platos:')
            print('1. Milanesa Napolitana de tipo Principal y va a ser acompañado con Papas Fritas, NO es celiaco y NO es vegano. Todo esto va a tener el precio de $8500')
            print('2. Ensalada Caesar de tipo Pricipal y va a ser acompañado con crutones, NO es celiaco y es vegano. Todo esto va a tener el precio de $6200 ')
            opcion_plato = int(input('Cual plato es: '))
            match opcion_plato:
                case 1:
                    print(f'Se ha seleccionado la comida {plato1.obtener_informacion()}')
                    
                    print('Quire agregarle o quitar ingredientes?')
                    print('1. Agregar')
                    print('2. Sacar')
                    print('3. igual')
                    opcion_agregar_sacar = int(input('Opcion: '))
                    while True:
                     match opcion_agregar_sacar:
                      case 1:
                        print('Que le queres agregar?')
                        agregado = input('Agregado: ')
                        plato1.añadir_ingredientes(agregado)
                        pedido_mesa.agregar(plato1)
                        break
                      case 2:
                        print('Que le queres sacar?')
                        agregado = input('Sacar: ')
                        plato1.quitar_ingredientes(agregado)
                        pedido_mesa.agregar(plato1)
                        break
                      case 3:
                            print(f'Ok, ha quedado igual: {plato1.obtener_informacion()}')
                            pedido_mesa.agregar(plato1)
                            break
                      case _:
                            print('Tiene que ser alguna de las opciones entre 1 y 3')
                            continue
                case 2:
                    print(f'Se ha seleccionado la comida {plato2.obtener_informacion()}')
                    
                    print('Quire agregarle o quitar ingredientes?')
                    print('1. Agregar')
                    print('2. Sacar')
                    print('3. igual')
                    opcion_agregar_sacar = int(input('Opcion: '))
                    while True:
                     match opcion_agregar_sacar:
                      case 1:
                        print('Que le queres agregar?')
                        agregado = input('Agregado: ')
                        plato2.añadir_ingredientes(agregado)
                        pedido_mesa.agregar(plato2)
                        break
                      case 2:
                        print('Que le queres sacar?')
                        agregado = input('Sacar: ')
                        plato2.quitar_ingredientes(agregado)
                        pedido_mesa.agregar(plato2)
                        break
                      case 3:
                            print(f'Ok, ha quedado igual: {plato1.obtener_informacion()}')
                            pedido_mesa.agregar(plato2)
                            break
                      case _:
                            print('Tiene que ser alguna de las opciones entre 1 y 3')
                            continue
            print(f'El pedido hasta ahora: {pedido_mesa.mostrar_pedido()}')
            print(f'El precio hasta ahora: ${pedido_mesa.calcular_total}')
            print(f'Anadir bebida? SI o NO')
            while True:
             bebida = input('Bebida: ')
             if bebida == 'SI':
               print('Opciones:')
               print(f'1. {bebida1.obtener_informacion()}')
               print(f'2. {bebida2.obtener_informacion()}')
               while True: 
                opcion_bebida = int(input('Opcion: '))
                match opcion_bebida:
                  case 1:
                     pedido_mesa.agregar(bebida1)
                     break
                  case 2:
                     pedido_mesa.agregar(bebida2)
                     break
                  case _:
                     print(f'Solo se puede: {bebida1.nombre} y {bebida2.nombre}')
                     continue
             elif bebida == 'NO':
               print(f'El pedido esta: {pedido_mesa.mostrar_pedido()}')
               print(f'Precio hasta ahora: ${pedido_mesa.calcular_total()}')
               break
             else:
               print('es SI o NO')
               continue
        print('Quiere sacar un producto')
        while True:
         sacar = input('Sacar: ')
         if not isinstance(sacar, str):
            print('Tiene que ser de tipo texto el producto que quiere eliminar')
            continue
         elif sacar == 'NO' or sacar == 'no':
            print('ok, no se ha sacado nada del pedido')
            break
         else:
            pedido_mesa.eliminar_producto(sacar)
            break
        
         
