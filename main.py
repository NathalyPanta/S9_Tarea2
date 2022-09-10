import os
import ejercicios.uno
import ejercicios.dos
import ejercicios.tres
from helper import Helper



helper = Helper()
lista = ["\n1. ejercicios del 1 al 10","2. ejercicios del 11 al 20","3. ejercicios 21 al 30","4. Ejercicios de POO","5. Salir"]
opcion =""
while opcion != "5":
    os.system("cls")
    opcion = helper.menu(lista,"\033[1;36m"+"    >> EJERCICIOS <<"+"\033[0m")
    os.system("cls")

    if opcion == '1':
        opc1 =""
        while opc1 != 0:
            os.system("cls")
            opc1 = helper.menu([" 1. Ejercicio - Primer Proyecto"," 2. Ejercicio 2 - Conversiones",
            " 3. Ejercicio 3 - Operaciones Matemáticas"," 4. Ejercicio 4 - Concatenar"," 5. Ejercicio 5 - Cadenas",
            " 6. Ejercicio 6 - Tuplas"," 7. Ejercicio 7 - Listas"," 8. Ejercicio 8 - Diccionarios",
            " 9. Ejercicio 9 - Ingreso de Datos","10. Ejercicio 10 - Estructuras Condicionales","\n11. REGRESAR A MENU PRINCIPAL "], ("\033[1;33m"+"       >> EJERCICIOS DEL 1 AL 10 <<"+'\033[0;m'))
            os.system("cls")
            if opc1 == "1":
                print("\033[1;33m"+"     PRIMER PROYECTO EN PYTHON" +'\033[0;m')
                ejercicios.uno.ejercicio1()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "2":
                print("\033[1;33m"+"     EJERCICIO 2 > CONVERSIONES" +'\033[0;m')
                ejercicios.uno.ejercicio2()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "3":
                print("\033[1;33m"+"     EJERCICIO 3 > OPERACIONES MATEMÁTICAS" +'\033[0;m')
                ejercicios.uno.ejercicio3()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "4":
                print("\033[1;33m"+"     EJERCICIO 4 > CONCATENAR" +'\033[0;m')
                ejercicios.uno.ejercicio4()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "5":
                print("\033[1;33m"+" EJERCICIO 5 --> CADENAS" +'\033[0;m')
                ejercicios.uno.ejercicio5()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "6":
                print("\033[1;33m"+" EJERCICIO 6 --> TUPLAS" +'\033[0;m')
                ejercicios.uno.ejercicio6()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "7":
                print("\033[1;33m"+" EJERCICIO 7 --> LISTAS" +'\033[0;m')
                ejercicios.uno.ejercicio7()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "8":
                print("\033[1;33m"+" EJERCICIO 8 --> DICCIONARIO" +'\033[0;m')
                ejercicios.uno.ejercicio8()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "9":
                print("\033[1;33m"+" EJERCICIO 9 --> INGRESO DE DATOS" +'\033[0;m')
                ejercicios.uno.ejercicio9()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "10":
                print("\033[1;33m"+" EJERCICIO 10 --> ESTRUCTURAS CONDICIONALES - IF...ELSE" +'\033[0;m')
                ejercicios.uno.ejercicio10()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "11":
                input("\033[1;32m" + "Saliendo del menú..."
                                     "\n" "Presione una tecla para continuar..." + "\033[0m")
                break

    elif opcion == "2":
        opc1 =""
        while opc1 != '0':
            os.system("cls")
            opc1 = helper.menu(["1. Ejercicio 11 - Funciones","2. Ejercicio 12 - Operadores Lógicos", "3. Ejercicio 13 - Operadores Ternarios",
                                "4. Ejercicio 14 - Range", "5. Ejercicio 15 - For","6. Ejercicio 16 - IF con TUPLAS y LISTAS",
                                "7. Ejercicio 17 - Factorial de un Número","8. Ejercicio 18 - While","9. Ejercicio 19 - Break, Continue, Pass",
                                "10. Ejercicio 20 - Generadores","\n11. REGRESAR AL MENÚ PRINCIPAL"],"\033[1;33m"+"  EJERCICIO 11 AL 20:" +'\033[0;m')
            os.system("cls")
            if opc1 == "1":
                print("\033[1;33m"+"     Ejercicio 11 - FUNCIONES" +'\033[0;m')
                ejercicios.dos.ejercicio11()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "2":
                print("\033[1;33m"+"     Ejercicio 12 - OPERADORES LÓGICOS" +'\033[0;m')
                ejercicios.dos.ejercicio12()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "3":
                print("\033[1;33m"+"     Ejercicio 13 - OPERADORES TERNARIOS" +'\033[0;m')
                ejercicios.dos.ejercicio13()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "4":
                print("\033[1;33m"+"     Ejercicio 14 - RANGE" +'\033[0;m')
                ejercicios.dos.ejercicio14()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "5":
                print("\033[1;33m"+"     Ejercicio 15 - FOR" +'\033[0;m')
                ejercicios.dos.ejercicio15()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "6":
                print("\033[1;33m"+"     Ejercicio 16 - IF con TUPLAS y LISTAS" +'\033[0;m')
                ejercicios.dos.ejercicio16()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "7":
                print("\033[1;33m"+"     Ejercicio 17 - Factorial de un Número" +'\033[0;m')
                ejercicios.dos.ejercicio17()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "8":
                print("\033[1;33m"+"     Ejercicio 18 - WHILE" +'\033[0;m')
                ejercicios.dos.ejercicio18()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "9":
                print("\033[1;33m"+"     Ejercicio 19 - BREAK, CONTINUE, PASS" +'\033[0;m')
                ejercicios.dos.ejercicio19()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "10":
                print("\033[1;33m"+"     Ejercicio 20 - Generadores (Cláusula Yield" +'\033[0;m')
                lim=int(input("\n Ingrese Límite: "))
                ejercicios.dos.generadorMultiplo7(lim)
                obtieneMultiplos7 = ejercicios.dos.generadorMultiplo7(lim)
                print(obtieneMultiplos7)
                for n in obtieneMultiplos7:
                    print(n)
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "11":
                input("\033[1;32m" + "Saliendo del menú.."
                                     "\n" "Presione una tecla para continuar..." + "\033[0m")
                break

    elif opcion == "3":
        opc1 = ""
        while opc1 != '0':
            os.system("cls")
            opc1 = helper.menu(["1. Ejercicio 21 - Generadores","2. Ejercicio 22 - Excepciones",
                                "3. Ejercicio 23 - Raise", "4. REGRESAR AL MENÚ PRINCIPAL"], "\033[1;33m"+"      >> EJERCICIOS 21 AL 23 <<" +'\033[0;m')
            os.system("cls")
            if opc1 == "1":
                print("\033[1;33m"+"     Ejercicio 21 - GENERADORES (Cláusula yield from)" +'\033[0;m')
                leng1 = input("INGRESA LENGUAJE DE PROGRAMACACIÓN 1: ")
                leng2 = input("INGRESA LENGUAJE DE PROGRAMACACIÓN 2: ")
                ejercicios.tres.ejercicio21()
                lengObtenidos = ejercicios.tres.ejercicio21(leng1)
                lengObtenidos2 = ejercicios.tres.ejercicio21(leng2)
                print(next(lengObtenidos))
                print(next(lengObtenidos2))
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "2":
                print("\033[1;33m"+"     Ejercicio 22 - EXCEPCIONES" +'\033[0;m')
                ejercicios.tres.ejercicio22()
                input("\n Presiona una tecla para continuar...")
            elif opc1 == "3":
                print("\033[1;33m"+"     Ejercicio 23 - RAISE" +'\033[0;m')
                nota = int(input("Ingrese su nota: "))
                ejercicios.tres.ejercicio23(nota)
                input("\n Presiona una tecla para continuar...")
            elif opc1 =="4":
                input("\033[1;32m" + "Saliendo del menú.."
                                     "\n" "Presione una tecla para continuar..." + "\033[0m")
                break

    elif opcion == "4":
        opc1 =""
        while opc1 != '0':
            os.system("cls")
            opc1 = helper.menu(["1. Clases y objetos", "2. Constructores","3. Encasulamiento","4. Encasulamiento de Funciones",
                                "5. Métodos GET - SET","6. Herencia y Sobreescritura de datos","7. Herencia Múltiple",
                                "8. Polimorfismo", "9. Relaciones Entre Clases","\n10. REGRESAR AL MENÚ PRINCIPAL"],"\033[1;33m"+"PROGRAMACIÓN ORIENTADA A OBJETOS" +'\033[0;m')
            os.system("cls")
            if opc1 =="1":
                print("\033[1;33m"+"     CLASES Y OBJETOS" +'\033[0;m')
                class Persona():
                    apellidos = ""
                    nombres = ""
                    edad = 0
                    despierta = False

                    def despertar(self):
                        self.despierta = True
                        print("Buen Día")

                persona1 = Persona()
                persona1.apellidos = "Panta Vilela"
                print(persona1.apellidos)
                persona1.despertar()
                print(persona1.despierta)
                input("\n Presiona una tecla para continuar...")
            elif opc1 =="2":
                print("     CONSTRUCTORES")
                class Curso():
                    # nombre = "Matemáticas"
                    # creditos = 5
                    # profesion = "Ingenieria de Software"

                    # Estado inicial del objeto
                    def __init__(self, nom, cre, pro):
                        self.nombre = nom
                        self.creditos = cre
                        self.profesion = pro
                n=input("Ingresa tu nombre: ")
                c=input("Ingresa tus créditos: ")
                p=input("Ingresa tu profesion: ")
                curso1 = Curso(n,c,p)
                print(curso1.nombre)
                input("\n Presiona una tecla para continuar...")

            elif opc1 == "3":
                print("\033[1;33m"+"  ENCAPSULAMIENTO" +'\033[0;m')
                class Curso():
                    def __init__(self, nom, cre, pro):
                        self.nombre = nom
                        self.creditos = cre
                        self.profesion = pro
                        self.__imparticion = "Presencial"  # Propiedad encapsulada

                    def mostrarDatos(self):
                        dat = "Nombre: {} / Créditos: {} / Modo de impartición {}"
                        print(dat.format(self.nombre, self.creditos, self.__imparticion))

                curso1 = Curso("Matemáticas", 5, "PROFESION")
                print(curso1.nombre)
                curso1.mostrarDatos()
                input("\nPresiona una tecla para continuar...")

            elif opc1=="4":
                print("\033[1;33m"+"  ENCAPSULAMIENTO DE FUNCIONES " +'\033[0;m')
                class Curso():
                    # nombre = "Matemáticas"
                    # creditos = 5
                    # profesion = "Ingenieria de Software"

                    # Estado inicial del objeto
                    def __init__(self, nom, cre, pro):
                        self.nombre = nom
                        self.creditos = cre
                        self.profesion = pro
                        self.__imparticion = "Presencial"  # Propiedad encapsulada

                    def mostrarDatos(self):
                        dat = "Nombre: {} / Créditos: {} / Modo de impartición {}"
                        print(dat.format(self.nombre, self.creditos, self.__imparticion))
                        docenteAsignado = self.__verificarDocente()
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
                        texto = "Nombre: {} - creditos: {}"
                        return texto.format(self.nombre, self.creditos)

                curso1 = Curso("matematica", 5, "Ing de Soft")
                print(curso1.nombre)
                curso1.mostrarDatos()
                input("\nPresiona una tecla para continuar...")

            elif opc1 == "5":
                print("\033[1;33m"+"   Métodos GET - SET" +'\033[0;m')
                class Cuenta():
                    def __init__(self, pro, sal, mon):
                        self.__propietario = pro
                        self.__saldo = sal
                        self.__moneda = mon

                    # Métodos GET - SET
                    # Getters
                    def get_Saldo(self):
                        return self.__saldo

                    def get_Propietario(self):
                        return self.__propietario

                    def get_Moneda(self):
                        return self.__moneda

                    # Setters
                    def set_Moneda(self, moneda):
                        self.__moneda = moneda


                cuenta1 = Cuenta("Nathaly Panta", 1500, "Soles")
                print(cuenta1.get_Saldo())
                print(cuenta1.get_Moneda())
                cuenta1.set_Moneda("Dolares")
                print(cuenta1.get_Moneda())
                input("\nPresiona una tecla para continuar...")
            elif opc1  == "6":
                print("\033[1;33m"+"  HERENCIA Y SOBREESCRITURA DE MÉTODOS" +'\033[0;m')
                class Persona():
                    def __init__(self, apePat, apeMat, nom):
                        self.apellidoPaterno = apePat
                        self.apellidoMaterno = apeMat
                        self.nombres = nom

                    def mostrarNombreCompleto(self):
                        txt = "{} {} {}"
                        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

                    def datos(self):
                        print(self.mostrarNombreCompleto())

                class Estudiante(Persona):
                    def __init__(self, apePat, apeMat, nom, pro):
                        super().__init__(apePat, apeMat, nom)
                        self.profesion = pro

                    def datos(self):
                        super().datos()
                        print("Profesion: {}".format(self.profesion))

                paterno= input("Ingrese Apellido Paterno: ")
                materno= input("Ingrese Apellido Materno: ")
                nom= input("Ingrese Nombre: ")
                prof= input("Ingrese Profesion: ")
                estu1 = Estudiante(paterno,materno,nom,prof)
                print(estu1.mostrarNombreCompleto())
                print(estu1.profesion)
                print("\nSOBREESCRITURA DE DATOS")
                estu1.datos()

                input("\nPresiona una tecla para continuar...")

            elif opc1 == "7":
                print("\033[1;33m"+"  HERENCIA MÚLTIPLE" +'\033[0;m')
                class ClaseA():
                    def __init__(self, par1, par2):
                        self.parametro1 = par1
                        self.parametro2 = par2
                class ClaseB():
                    def __init__(self, par3, par4, par5):
                        self.parametro3 = par3
                        self.parametro4 = par4
                        self.parametro5 = par5
                class ClaseX(ClaseA, ClaseB):
                    pass
                cx1 = ClaseX(15, 21)
                input("\nPresiona una tecla para continuar...")

            elif opc1 == "8":
                print("\033[1;33m"+"     POLIMORFISMO" +'\033[0;m')
                class Estudiante():
                    def describir(self):
                        print("Soy un buen estudiante")
                class Docente():
                    def describir(self):
                        print("Me dedico a enseñar cursos")
                class Trabajador():

                    def describir(self):
                        print("Trabajo dentro de una gran empresa")
                def describirPersona(persona):
                    persona.describir()

                doc1 = Trabajador()
                describirPersona(doc1)
                input("\nPresiona una tecla para continuar...")

            elif opc1 == "9":
                print("\033[1;33m"+"   RELACIONES ENTRE CLASES" +'\033[0;m')
                class Pais():
                    def __init__(self, nom, pre):
                        self.nombre = nom
                        self.presidente = pre
                    def __str__(self):
                        txt = "Pais: {} - Presidente: {}"
                        return txt.format(self.nombre, self.presidente)
                class Ciudad():
                    def __init__(self, nom, hab, pai):
                        self.nombre = nom
                        self.habitantes = hab
                        self.pais = pai
                    def __str__(self):
                        txt = "Ciudad: {} - N° Habitantes: {} ({})"
                        return txt.format(self.nombre, self.habitantes, self.pais)
                class Urbanizacion():
                    def __init__(self, nom, ciu):
                        self.nombre = nom
                        self.ciudad = ciu
                    def __str__(self):
                        txt = "Urbanizacion: {} ({})"
                        return txt.format(self.nombre, self.ciudad)
                pais1 = Pais("Ecuador", "Nathaly Panta")
                print(pais1)
                ciudad1 = Ciudad("Guayaquil", 1500, pais1)
                print(ciudad1)
                urba1 = Urbanizacion("Micasa", ciudad1)
                print(urba1)
                input("\nPresiona una tecla para continuar...")

            elif opc1 == "10":
                input("\033[1;32m" + "Saliendo del menú.."
                                     "\n" "Presione una tecla para continuar..." + "\033[0m")
                break

    elif opcion == "5":
        print("\033[1;33m"+"Saliendo del menú..." +"\033[0m")
        print()
