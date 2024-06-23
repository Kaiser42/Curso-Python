class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

base = int(input("Ingrese el base del rectangulo: "))
alto = int(input("Ingrese el alto del rectangulo: "))

rect = Rectangulo(base, alto)

print(f"Area: {rect.area()}")