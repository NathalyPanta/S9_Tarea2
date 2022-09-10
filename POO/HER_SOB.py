class Persona():
    def __init__(self,apePat,apeMat,nom):
        self.apellidoPaterno = apePat
        self.apellidoMaterno = apeMat
        self.nombres = nom

    def mostrarNombreCompleto(self):
        txt = "{} {} {}"
        return txt.format(self.apellidoPaterno,self.apellidoMaterno,self.nombres)

    def datos(self):
        print(self.mostrarNombreCompleto())


class Estudiante(Persona):

    def __init__(self,apePat,apeMat,nom,pro):
        super().__init__(apePat,apeMat,nom)
        self.profesion = pro

    def datos(self):
        super().datos()
        print("Profesion: {}".format(self.profesion))


estu1 = Estudiante("Panta","Vilela","Nathaly","ING")
#print(estu1.mostrarNombreCompleto())
#print(estu1.profesion)
#estu1.datos()

