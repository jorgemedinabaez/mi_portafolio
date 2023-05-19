lista = ["Harry Houdini","Newton","David Blaine","Hawking","Messi","Teller","Einstein","Pele","Juanes"]

magos = ["Harry Houdini","David Blaine", "Teller"]
magos_grandiosos =[]

cientificos = ["Newton","Hawking","Einstein"]
otros = ["Messi","Pele","Juanes"] 

def hacer_grandioso():
    for nombre in lista:
        if nombre in magos:
            magos_grandiosos.append(f"El gran {nombre}")

def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


imprimir_nombres(lista)

print("-"*30)

hacer_grandioso()
imprimir_nombres(magos_grandiosos)

print("-"*30)

imprimir_nombres(cientificos)

print("-"*30)

imprimir_nombres(otros)
