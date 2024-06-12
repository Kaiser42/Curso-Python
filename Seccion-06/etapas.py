edad = int(input("Introzuca su edad: "))

if edad >= 0 and edad <= 30:
    if edad >= 0 and edad <= 10:
        print("\nLa infancia es increible")
    if edad > 10 and edad <= 20:
        print("\nMuchos cambios y mucho trabajo")
    if edad > 20 and edad <= 30:
        print("\nAmor y comieza el trabajo")
else:
    print("\nEtapa no reconocida")