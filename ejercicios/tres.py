# GENERADORES
#devuelve lenguajes
""" def ejercicio21(*lenguajes):
    for leng in lenguajes:
        yield leng """

def ejercicio21(*lenguajes):
    for leng in lenguajes:
        yield from leng

    lenuajesObtenidos = ejercicio21("Python","Java","PHP","Ruby","JavaScript")

    print(next(lenuajesObtenidos))
    print(next(lenuajesObtenidos))


# EXCEPCIONES  TRY - EXCEPT - FINALLY
def ejercicio22():
    numero1 = 20
    numero2 = 0

    #print("La division de {} entre {} es: ".format(numero1,numero2,(numero1/numero2)))
    
    try:
        resultado = numero1/numero2
    except ZeroDivisionError:
        print("Error. No se puede dividir entre 0... (except)")
    finally:
        print("Yo siempre aparezco. (finally)")
    
    print("Aquí termina el programa.")

#RAISE  -- lanza de forma intencional excepciones personalizadas
def ejercicio23(nota):
    if nota < 0:
        #raise ZeroDivisionError ("No se permiten valores negativos...")
        raise ValueError ("Valor incorrecto. INGRESA UN VALOR MAYOR QUE CERO")
    elif nota >= 16:
        print("Excelente")
    elif nota >= 11:
        print ("Aprobado")
    else:
        print("Desaprobado")

