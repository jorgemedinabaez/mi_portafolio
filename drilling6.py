x=12
y=8
z=14
if (x>y>z):
    print(f"El orden de los números es: {x},{y},{z}")
elif (x<y>z and x>z):
    print(f"El orden de los números es: {y},{x},{z}")
elif (x<y<z):
    print(f"El orden de los números es: {z},{y},{x}")
elif (x>y<z and x>z):
    print(f"El orden de los números es: {x},{z},{y}")
elif(x<y>z and x<z):
    print(f"El orden de los números es: {y},{z},{x}")
else:
    print(f"El orden de los números es: {z},{x},{y}")



