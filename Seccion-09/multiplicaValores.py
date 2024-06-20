def multiplicaValores(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

total = multiplicaValores(1, 2, 3, 4, 5, 6, 1, 6, 7, 8, 9)
print(f"La suma de todos los numeros es {total}")

