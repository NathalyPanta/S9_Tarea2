class Pais():

    def __init__(self,nom,pre):
        self.nombre = nom
        self.presidente = pre

    def __str__(self):
        txt ="Pais: {} - Presidente: {}"
        return txt.format(self.nombre, self.presidente)

class Ciudad():
    def __init__(self,nom,hab,pai):
        self.nombre=nom
        self.habitantes=hab
        self.pais=pai

    def __str__(self):
        txt ="Ciudad: {} - N° Habitantes: {} ({})"
        return txt.format(self.nombre, self.habitantes, self.pais)

class Urbanizacion():
    def __init__(self,nom,ciu):
        self.nombre= nom
        self.ciudad= ciu

    def __str__(self):
        txt ="Urbanizacion: {} ({})"
        return txt.format(self.nombre, self.ciudad)


pais1 = Pais ("Ecuador","Nathaly Panta")
print(pais1)

ciudad1 = Ciudad("Guayaquil", 1500, pais1)
print(ciudad1)

urba1 = Urbanizacion ("Micasa",ciudad1)
print(urba1)