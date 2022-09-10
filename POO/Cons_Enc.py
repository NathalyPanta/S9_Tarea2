class Curso():
    # nombre = "Matemáticas"
    # creditos = 5
    # profesion = "Ingenieria de Software"

#Estado inicial del objeto
    def __init__(self,nom,cre,pro):
        self.nombre=nom
        self.creditos = cre
        self.profesion = pro
        self.__imparticion = "Presencial"     #Propiedad encapsulada

    def mostrarDatos(self):
        dat= "Nombre: {} / Créditos: {} / Modo de impartición {}"
        print(dat.format(self.nombre,self.creditos,self.__imparticion))
        docenteAsignado= self.__verificarDocente()
        if docenteAsignado:
            print("Existe Docente Asignado")
        else:
            print("No es necesario asignar un docente...")


    def __verificarDocente(self):
        print("Verificando si existe docente asignado...")
        if self.__imparticion == "Presencial":
            return True
        else:
            return False

# Retorna en formato de texto los datos de una instancia de una clase
    def __str__(self):
        texto ="Nombre: {} - creditos: {}"
        return texto.format(self.nombre,self.creditos)

curso1 = Curso("matematica",5,"Ing de Soft")
print(curso1.nombre)
curso1.mostrarDatos()

curso2 = Curso("lenguaje",80,"Ing de Soft")
print(curso2.nombre)
print((curso2))