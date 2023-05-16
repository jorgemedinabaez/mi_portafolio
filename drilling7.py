listado=[[1,2,3], [0,4,5], [4,0,1], [6,5,4]]

for sublista in listado:
    if sublista[0] == 0:
        continue
    for num in sublista:
        if num == 0:
            continue
        print("El número es: ",num)
