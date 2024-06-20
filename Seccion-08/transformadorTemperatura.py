def grados2Fahrenheit(numero):
    return (numero * (9/5)) + 32

def grados2Celsius(numero):
    return (numero - 32) * (5/9)

numero = int(input("Ingrese un numero: "))

print("""
1 - Convertir de grados Fahrenheit a grados Celsius:
2 - Convertir de grados Celsius a grados Fahrenheit:
""")
opcion = int(input("Ingrese un numero: "))
if opcion == 1:
    print(grados2Fahrenheit(numero))
else:
    print(grados2Celsius(numero))