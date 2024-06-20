numero = int(input("Ingrese un numero: "))

def cuentaAtras(numero):
    if numero <= 0:
        return None
    else:
        print(numero)
        cuentaAtras(numero-1)

cuentaAtras(numero)



