class Persona:
    def __init__(self,nombre,apellido,sexo,edad,estatura,peso):
        self.nombre=nombre
        self.apellido=apellido
        self.sexo=sexo
        self.edad=edad
        self.estatura=estatura
        self.peso=peso

    def get_nombre(self):
        return self.nombre
    def set_nombre(self,nombre):
        self.nombre=nombre
    
    def get_apellido(self):
        return self.apellido
    def set_apellido(self,apellido):
        self.apellido=apellido

    def get_sexo(self):
        return self.sexo
    def set_sexo(self,sexo):
        self.sexo=sexo

    def get_edad(self):
        return self.edad
    def set_edad(self,edad):
        self.edad=edad

    def get_estatura(self):
        return self.estatura
    def set_estatura(self,estatura):
        self.estatura=estatura

    def get_peso(self):
        return self.peso
    def set_peso(self,peso):
        self.peso=peso

persona_1 = Persona('Pedro','Vivas','masculino','20 años','1.78 mts','68 kg')
persona_2 = Persona('Juan','Camargo','masculino',18,'1.8 mts','75 kg')

print(persona_1.__dict__)
print(persona_2.__dict__)

persona_1.set_edad('21 años')
persona_2.set_apellido('Santiago')

print(persona_1.__dict__)
print(persona_2.__dict__)