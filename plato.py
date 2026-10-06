from producto import Producto

class Plato(Producto):
    def __init__(self, nombre, precio, es_vegano, añadido, tipo, es_celiaco):
        super().__init__(nombre, precio)
        self.es_vegano = es_vegano
        self.añadido = añadido
        self.tipo = tipo
        self.es_celiaco = es_celiaco
        self.ingredientes_extra = []
        self.sin_ingredientes = []

    def añadir_ingredientes(self, extra):
        if extra in self.ingredientes_extra:
            raise ValueError(f'{extra} ya se encuentra en la lista de extras')
        else:
            self.ingredientes_extra.append(extra)
            print(f'Se le agrego {extra} a {self.nombre}')

    def quitar_ingredientes(self, ingrediente):
        if ingrediente in self.sin_ingredientes:
            raise ValueError(f'{ingrediente} ya se encuentra en la lista de Sin ingredientes')
        else:
            self.sin_ingredientes.append(ingrediente)
            print(f'Quedo {self.nombre} SIN {ingrediente}')

    def obtener_informacion(self):
        if self.es_celiaco:
            resultado_celiaco = 'SI'
        else:
            resultado_celiaco = 'NO'

        if self.es_vegano:
            resultado_vegano = 'SI'
        else:
            resultado_vegano = 'NO'

        if len(self.ingredientes_extra) == 0:
            extras = ''
        else:
            extras = 'Con extras de: '
            for ingrediente in self.ingredientes_extra:
                extras += ingrediente + ' '

        if len(self.sin_ingredientes) == 0:
            sin_extras = ''
        else:
            sin_extras = 'Sin: '
            for ingrediente in self.sin_ingredientes:
                sin_extras += ingrediente + ' '
                
        return f'El producto es {self.nombre}{extras}{sin_extras} de tipo {self.tipo} y va a ser acompañado con {self.añadido}, {resultado_celiaco} es celiaco y {resultado_vegano} es vegano. Todo esto va a tener el precio de ${self.precio}.'



