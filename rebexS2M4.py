class Animal():
    def __init__(self,Nombre,Edad,Raza,Peso):
        self.Nombre=Nombre
        self.Edad=Edad
        self.Raza=Raza
        self.Peso=Peso

Caballo = Animal('Zeus','5 años','Pura sangre','450 kg')

León = Animal('Boulder','10 años','Atlas','130 kg')

print(León.__dict__)
print(Caballo.__dict__)