nombre = input('Introzuca el nombre del libro: ')
id = int(input('Introzuca el id del libro: '))
precio = float(input('Introzuca el precio del libro: '))
envioGratis =bool(input('El envio es gratuito?: '))

print(f"""Nombre: {nombre}
ID: {id}
Precio: {precio}
Envio Gratis: {envioGratis}""")