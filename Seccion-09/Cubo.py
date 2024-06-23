class Cubo:
    def __init__(self, ancho, alto,  profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def cal_volumen(self):
        return (self.ancho * self.alto * self.profundo)


ancho = int(input("Ingrese el ancho del cubo: "))
alto = int(input("Ingrese el alto del cubo: "))
profundo = int(input("Ingrese el profundo del cubo: "))

cubo = Cubo(ancho, alto, profundo)

print(f"El volumen: {cubo.cal_volumen()}")
