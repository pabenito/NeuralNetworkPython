class Neurona:
    def __init__(self, pesos, bias):
        self.pesos = pesos
        self.bias = bias
    def activar(self, entradas):
        return sum([self.pesos[i]*entradas[i] for i in range(len(entradas))]) + self.bias