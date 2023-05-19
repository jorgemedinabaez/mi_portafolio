def operacion1(a,b):
    suma = a+b
    resultado1 = (suma)

    print("El resultado es:",suma)
    return resultado1

a=50
b=75
resultado=operacion1(a,b)

print("-"*30)

def operacion2(c,d):
    resta = c-d
    resultado2 = (resta)

    print("El resultado es:",resta)
    return resultado2

c=50
d=75
resultado2 = operacion2(c,d)

print("-"*30)

def operacion3(e,f):
    multiplicacion = a*b
    resultado3 = (multiplicacion)

    print("El resultado es:",multiplicacion)
    return resultado

e=50
f=2
resultado3 = operacion3(e,f)

print("-"*30)

def operacion4(g,h):
    division = g/h
    resultado4 = (division)

    print("El resultado es:",int(division))
    return resultado4

g=50
h=2
resultado4=operacion4(g,h)

print("-"*30)

def operacion5(i,j):
    suma = i+j
    resta = i-j
    division = int(i/j)
    multiplicacion = i*j
    resultado5_tupla = (suma,resta,division,multiplicacion)
    resultado5_diccionario = {
        "Suma": suma,
        "Resta": resta,
        "División": division,
        "Multiplicación": multiplicacion
    }
    print("Los resultados en formato tupla son:",resultado5_tupla)
        #   (suma,resta,int(division),multiplicacion))
    print("Los resultados en formato diccionario son:",resultado5_diccionario)

    return resultado5_tupla, resultado5_diccionario

i = 60
j = 10
resultado5_tupla, resultado5_diccionario = operacion5(i,j)

print("-"*30)
