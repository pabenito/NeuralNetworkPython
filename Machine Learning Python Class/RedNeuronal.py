class RedNeuronal:
    def __init__(self, capas):
        self.capas = capas

    def activar(self, entradas):
        for capa in self.capas:
            entradas = capa.activar(entradas)
        return entradas