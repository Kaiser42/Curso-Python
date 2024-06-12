nota = int(input("Introzuca su nota: "))

if nota >= 0 and nota <= 10:
    if nota >= 0 and nota < 6:
        print("\nF")
    if nota >= 6 and nota < 7:
        print("\nD")
    if nota >= 7 and nota < 8:
        print("\nC")
    if nota >= 8 and nota < 9:
        print("\nB")
    if nota >= 9 and nota <= 10:
        print("\nA")
else:
    print("\nValor incorrecto")