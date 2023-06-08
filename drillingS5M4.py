class Persona:
    def __init__(self,nombre,apellido,anno):
        self.nombre = nombre
        self.apellido = apellido
        self.anno = anno
    def imprimir_persona(self):
        print(f'Es trabajador instancia de Persona: {True}')
              
class Departamento:
    def __init__(self,nombre_depto,nombre_corto_depto):
        self.nombre_depto = nombre_depto
        self.nombre_corto_depto = nombre_corto_depto
    def imprimir_depto(self):
        print(f'Es trabajador instancia de Departamento: {True}')

class Trabajador(Persona,Departamento):
    def __init__(self, nombre, apellido, anno, nombre_depto, nombre_corto_depto,salario):
        Persona.__init__(self,nombre, apellido, anno)
        Departamento.__init__(self,nombre_depto,nombre_corto_depto)
        self.salario = salario
    def imprimir_trabajador(self):
        Persona.imprimir_persona(self)
        Departamento.imprimir_depto(self)
        print(f'Es trabajador instancia de Trabajador: {True}')    

trabajador = Trabajador('Juan','Perez',2005,'Ingenieria de software','IS',20000)
print(trabajador.__dict__)
trabajador.imprimir_trabajador()