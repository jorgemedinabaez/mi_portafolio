lista=[0,1,2,3,4,5,6,7,8,9]

for x in lista:
    if (x == 0):
        print(f"El número es {x}")
    elif (x % 2 == 0 and x != 0):
        print(f"Este es un número par {x}")
    else:
        print(f"Este es un número impar {x}")