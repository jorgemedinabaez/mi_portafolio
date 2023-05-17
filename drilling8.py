listado=[[1,2,3], [0,4,5], [4,0,1], [6,5,4]]
# diccionario={}

# for i, sublista in enumerate(lista):
#     if sublista[0] == 0:
#         continue
#     else:
#         clave=chr(i+65)
#         diccionario[clave]=[elem for elem in sublista if elem != 0]
#         for j in diccionario[clave]:
#             print(clave+':'+ str(j))
# print(diccionario)

for sublista in listado:
    if sublista[0] == 0:
        listado.remove(sublista)
        sublistaC = listado[1]
        for num in sublistaC:
            if num == 0:
                sublistaC.remove(num)
        lista2 = listado

diccionario = {
    "A": lista2[0],
    "B": lista2[1],
    "C": lista2[2]
}

print(diccionario)
# print(listas)