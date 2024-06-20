def sumaValores(*args):
    total = 0
    for numero in args:
        total += numero
    return total

total = sumaValores(1,2,3,4,5,6,1,6,7,8,9)
print(f"La suma de todos los numeros es {total}")

