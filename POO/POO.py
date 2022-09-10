
class Persona():
    apellidos= ""
    nombres = ""
    edad = 0
    despierta = False

    def despertar(self):
        self.despierta= True
        print("Buen Día")

persona1 = Persona()
persona1.apellidos ="Panta Vilela"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2 = Persona()
persona2.apellidos ="Nathaly Solange"
print(persona2.apellidos)
#persona2.despertar()
print(persona2.despierta)