class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'{self.color} {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
       return super().__str__() + f' {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f' {self.tipo}'

vehiculo1 = Vehiculo('ROJO', 5)
print(vehiculo1)

vehiculo2 = Coche('AZUL', 5, 300)
print(vehiculo2)

vehiculo3 = Bicicleta('NEGRA', 3, "Electica")
print(vehiculo3)