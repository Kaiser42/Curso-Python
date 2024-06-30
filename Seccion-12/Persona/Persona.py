class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
class Empleado(Persona):
    def __init__(self, nombre, apellido, salario):
        super().__init__(nombre, apellido)
        self.salario = salario

