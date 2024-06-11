numero = int(input('Introzuca un valor numerico: '))

rango = numero >= 0 and numero <=5

if rango:
    print(f'El numero {numero} SI forma parte del rango de 0 a 5')
else:
    print(f'El numero {numero} NO forma parte del rango de 0 a 5')