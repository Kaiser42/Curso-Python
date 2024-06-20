precio = int(input("Ingresa el valor sin los impuestos: "))
impuestos = int(input("Ingresa el valor del impuesto: "))

def calcularImpuestos(impuestos, precio):
    precio_total = precio+precio * (impuestos/100)
    return precio_total

precio_total = calcularImpuestos(impuestos, precio)

print(f"El precio total es: {precio_total:.2f}")
