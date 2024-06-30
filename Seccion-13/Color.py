class Color:
    def __init__(self, color):
        self._color = color

    @property #getter
    def color(self):
        return self.color
    @color.setter
    def color(self, color):
        self.color = color
