class Aritmetica:
    """
    Classe Aritmetica para operaciones
    """
    def __init__(self, OperandoA, OperandoB):
        self.OperandoA = OperandoA
        self.OperandoB = OperandoB

    def sumar(self):
        return self.OperandoA + self.OperandoB
    def restar(self):
        return self.OperandoA - self.OperandoB
    def multiplicar(self):
        return self.OperandoA * self.OperandoB
    def division(self):
        return self.OperandoA / self.OperandoB

a1 = Aritmetica(3, 3)
print(a1.sumar())
print(a1.restar())
print(a1.multiplicar())
print(a1.division())