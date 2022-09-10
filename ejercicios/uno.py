# ejercicio 1
def ejercicio1():
    print("Hola Mundo")

# ejercicio 2 CONVERSIONES
def ejercicio2 ():
    numero1 = "35"
    numero2 = "18"
    print(numero1+numero2)

    num1 = int(numero1)
    num2 = int(numero2)
    print(num1+num2)

    #2.1
def con_2 ():
    sueldo= 1200.43
    sueldoEntero = int(sueldo)
    print(sueldoEntero)

    #2.2
def con_3():
    valor = "4500.89"
    valorDecimal = float(valor)
    print(valorDecimal * 3)

    #2.3
def con_4():
    edad = 100
    print(len(str(edad)))

#3 OPERACIONES MATEMÁTICAS
def ejercicio3():
    # entero = 23
    # decimal = 31.70
    # complejo = 12 + 5j
    # booleano = True
    # print(entero)
    # print(decimal)
    # print(complejo)
    # print(booleano)
#
#     #3.1
# def op_mat_2():
    num1 = 20
    num2 = 4
    print("SUMA: ", (num1+num2))
    print("RESTA: ", (num1-num2))
    print("MULTPLICACIÓN: ", (num1*num2))
    print("DIVISIÓN: ", (num1/num2))
    print("DIVISIÓN EXACTA: ", (num1//num2))
    print("POTENCIA: ", (num1**num2))



# 4 CONCATENAR
def ejercicio4 ():
    texto1= "Hola"
    texto2= "Mundo"
    textoFinal = texto1 + " "+ texto2
    print(textoFinal)

    print("El saludo es: %s %s" % (texto1, texto2))

    saludoFinal = "Saludo: {0} {1}".format(texto1, texto2)
    print(saludoFinal)

#5 CADENAS
def ejercicio5 ():
    texto ="Bienvenidos al canal"

    print(texto)
    print(texto.lower())
    print(texto.upper())
    print(texto.title())
    print(texto.find("ca"))
    print(texto.count("e"))

    textoFinal = texto.replace("e", "3")
    print(textoFinal)

    valor = texto.isnumeric()
    print(valor)

    cadenaSeparada = texto.split(" ")
    print(cadenaSeparada)

# 6 TUPLAS
def ejercicio6 ():
    tupla= (1,2,3)
    print(tupla)
    tupla2=(7,"Oscar",True,450.1,16+7j,15,"felicidad",False)
    print(tupla2)
    tupla3=(9,3,(4,5,6))
    print(tupla3)
    print(tupla2[1])
    print(tupla2[-1]) #Accede al ultimo elemento.
    print(tupla2[0:4])
    print(tupla2[-2])

    a,b,c= tupla
    print(a)
    print(b)
    print(c)

    tuplaFinal = tupla + tupla3
    print(tuplaFinal)

    print(tuplaFinal.count(3))
    print(tuplaFinal.index(3))

# 7 Listas
def ejercicio7 ():
    lista1 = ["Oscar", 25, 98.3, True,"Flavio",56.3]
    print(lista1)
    print(lista1[:])
    print(lista1[2])
    print(lista1[-1])

    print(lista1[0:3])
    print(lista1[:2])
    print(lista1[3:])

    lista1.append("Nathaly")
    print(lista1)

    lista1.insert(4,"Perú")
    print(lista1)

    lista1.extend(["Alejandro",110,False])
    print(lista1)

    print(lista1.index("Flavio"))

    lista1.remove(56.3)
    print(lista1)

    lista1.pop()
    print(lista1)

    lista2 = ["Chiclayo", "Irma"]
    lista3 = lista1+lista2
    print(lista3)

    print(lista2 *4)

    print("NathalyPPPP" in lista1)

# 8 DICCIONARIOS
def ejercicio8 ():
    miDiccionario = {"España":"Madrid", "Perú":"Lima", "Alemania":"Berlin"}
    print(miDiccionario["Perú"])
    print(miDiccionario)

    miDiccionario["Venezuela"] = "Caracas"
    print(miDiccionario)

    miDiccionario["Ecuador"] = "Quito"
    print(miDiccionario)

    miDiccionario["Ecuador"] = "Guayaquil"
    print(miDiccionario)

    del miDiccionario["España"]
    print(miDiccionario)

    dic2={"García":"Oscar",25:True,"Sueldo":150.80}
    print(dic2[25])

    llaves=("España", "Francia", "Inglaterra")
    dicPaises = {llaves[0]: "Madrid", llaves[1]:"Paris", llaves[2]: "Londres"}
    print(dicPaises)

    datosPersonales={"Ape":"Garcia","Anios":{1:2010,2:2011,3:2012,4:2013,5:2014}}
    print(datosPersonales)
    print(datosPersonales["Anios"])

    print(datosPersonales.get('Ape', "Oscar"))

    print(datosPersonales.keys())
    print(datosPersonales.values())

#INGRESO DE DATOS
def ejercicio9 ():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    sueldo = float(input("Ingrese su sueldo: "))

    print(" \n Hola, "+nombre)
    edadFu= edad +20
    print("Tu edad es: ", edad)
    print("Tu sueldo es: ", sueldo)
    print("tu edad dentro de 20 años será: ", edadFu)

#IF ELSE -- ESTRUCTURAS CONDICIONALES
def ejercicio10():
    edad = int(input("Ingrese edad: "))
    if edad >18:
        print("\n Eres mayor de edad.")
    elif edad == 18:
        print("\n Tienes 18 años!")
    else:
        print("\n Eres menor de edad.")

