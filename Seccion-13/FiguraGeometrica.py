class FiguraGeometrica():
    def __init__(self, alto, ancho):
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto
    @property
    def ancho(self):
        return self._ancho

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def __str__(self):
        return f"El alto de {self._alto} y el ancho es de: {self._ancho}"



