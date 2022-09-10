# FUNCIONES  -- EJERCICIO 11
def ejercicio11():
    print("Garcia")
    print("Oscar")
    print("LLLLLLLL")
    return "Hola"


# print(saludar())

def evaluarSueldoMinimo(sueldo):
    if sueldo >= 850:
        print("Cumple con el sueldo")
    else:
        print("Ganas menos que el sueldo")


# evaluarSueldoMinimo(1200)


# OPERADORES LÓGICOS  (AND - OR - NOT)
def ejercicio12():
    distancia = 400
    numeroHermanos = 3
    salarioPadres = 3000

    tieneBeneficio = False

    if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
        tieneBeneficio = True

    print(not tieneBeneficio)

    if (5 > 3) and (4 < 6):
        print("Es verdad")
    else:
        print("Es mentira...")


# OPERADORES TERNARIOS
def ejercicio13():
    sexos = ("Hombres", "Mujer")
    posicion = True
    sexo = sexos[posicion]
    print(sexo)
    sexo = sexos[not posicion]
    print(sexo)


# RANGE
def ejercicio14():
    numeros = range(5)
    print(numeros[1])
    numeros1 = range(4, 10)
    print(numeros1[3])


# FOR
def ejercicio15():
    for num in range(0, 20, 2):
        print("Valor actual: {0}".format(num))
    for i in range(1, 13):
        print("{} x {} es: {}".format(i, i, (i * i)))
    for nom in ["Karen", "Oscar", "Hector", "Leonardo"]:
        print("Cantidad de letras de {} es: {}".format(nom, len(nom)))


# IF con TUPLSA y LISTAS
def ejercicio16():
    print("....CURSOS....")
    print("Matemáticas - Biología - Lenguaje - Ciencias")

    curso = input("Ingrese el curso deseado: ")

    if curso in ("Matematica", "Biologia", "Lenguaje", "Ciencia"):
        print("Curso {0} seleccionado".format(curso))
    else:
        print("No existe ese curso...")


# Factorial de un numero
def ejercicio17():
    numero = int(input("Ingrese numero: "))
    factorial = 1
    for n in range(1, (numero + 1)):
        factorial = factorial * n
    print("El factorial de {} es: {}".format(numero, factorial))


# WHILE
def ejercicio18():
    indice = 1
    while indice < 10:
        print("Valor actual {}".format(indice))
        indice = indice + 1
    print("Hemos terminado el bucle while.")

    inicio = 2
    while inicio <= 50:
        print("Numero par: {}".format(inicio))
        inicio += 2
    print("Hemos terminado el bucle while.")


# SENTENCIAS BREAK - CONTINUE - PASS
def ejercicio19():
    for numero in range(1, 6):
        if numero == 3:
            break
        print("El numero es: {}".format(numero))
    print("Bucle terminado")

    for num in range(1, 6):
        if num == 3:
            continue
        print("El numero es: {}".format(num))
    print("Bucle terminado")

    for num2 in range(1, 6):
        if num2 <= 3:
            # no pasa nada y el bucle sigue trabajando
            pass
        else:
            print("El siguiente valor es mayor a 3:")
        print("El numero es {}".format(num2))
    print("Bucle terminado")


# Generadores
def ejercicio20(limite):
    numero = 1
    listaNumeros = []

    while numero <= limite:
        listaNumeros.append(numero * 7)
        numero = numero + 1
    return listaNumeros


def generadorMultiplo7(limite):
    numero = 1

    while numero <= limite:
        yield numero * 7
        numero = numero + 1


# obtieneMultiplos7 = generadorMultiplo7(10)
#
# print(obtieneMultiplos7)
# for n in obtieneMultiplos7:
#      print(n)
#
# print(next(obtieneMultiplos7))
# print("Acá hay 300 líneas de código...")
# print(next(obtieneMultiplos7))
# print("Acá hay 100 lÍneas de código...")
# print(next(obtieneMultiplos7))