listado = [1, 2, 3, 4, 5]

factorial = 1
for valor in listado:
    factorial = factorial * valor
    # factorial *= valor
    print(f"El factorial correspondiente a {valor} es: {factorial}")