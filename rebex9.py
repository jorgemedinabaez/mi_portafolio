def operaciones (a,b,c):
    suma = a+b+c
    resta = a-b-c
    resultados= (suma, resta)

    print("Los resultados son:",(suma,resta))
 
    return resultados

a,b,c = [15,11,4]
resultados = operaciones(a,b,c)

# def sumar_y_restar_numeros(a,b,c):
#     suma_total = sum(parametros)
#     resta = parametros[0] - parametros[1] - parametros[2]
#     resultados = (suma_total, resta)
#     print("La suma total es:", resultados[0])
#     print("El resultado de la resta es:", resultados[1])
#     return resultados

# parametros = [5, 3, 2]
# resultados = sumar_y_restar_numeros(parametros)
