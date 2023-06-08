class A: 
    def __init__(self): 
        print("Pertenezco a la clase A") 
    def metodo_a(self): 
        print("Método heredado de A") 

class B: 
    def __init__(self): 
        print("Clase B") 
    def metodo_b(self): 
        print("Método heredado de B")

class C(B,A):
    def __init__(self):
        pass 
    def metodo_c(self):
        print("Metodo de clase C")
    def metodos_varios(self):
        B.__init__(self)
        A.metodo_a(self)
        B.metodo_b(self)

objetoC = C()
objetoC.metodos_varios()
objetoC.metodo_c()