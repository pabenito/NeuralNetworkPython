class Capa:
    def __init__(self, neuronas, funcion_activacion):
        self.neuronas = neuronas
        self.funcion_activacion = funcion_activacion

    def activar(self, entradas):
        return [self.funcion_activacion(neurona.activar(entradas)) for neurona in self.neuronas]