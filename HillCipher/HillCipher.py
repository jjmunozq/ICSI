# Hecho por Julio Javier Muñoz Quiñones
from calendar import c
import math
import numpy


# Diccionario para convertir los numeros a letras para cifrar
def abcedarioC(diccionario):
    return {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25}


# Diccionario para convertir los numeros a letras para descifrar
def abcedarioD(diccionario):
    return {'0': "A", '1': "B", '2': "C", '3': "D", '4': "E", '5': "F", '6': "G", '7': "H", '8': "I", '9': "J",
            '10': "K", '11': "L", '12': "M", '13': "N", '14': "O", '15': "P", '16': "Q", '17': "R", '18': "S", '19': "T", '20': "U", '21': "V", '22': "W",
            '23': "X", '24': "Y", '25': "Z", }


def main():
    print('''
╭╮╱╭╮╭╮╭╮╭━━━╮╱╱╱╭╮
┃┃╱┃┃┃┃┃┃┃╭━╮┃╱╱╱┃┃
┃╰━╯┣┫┃┃┃┃┃╱╰╋┳━━┫╰━┳━━┳━╮
┃╭━╮┣┫┃┃┃┃┃╱╭╋┫╭╮┃╭╮┃┃━┫╭╯
┃┃╱┃┃┃╰┫╰┫╰━╯┃┃╰╯┃┃┃┃┃━┫┃
╰╯╱╰┻┻━┻━┻━━━┻┫╭━┻╯╰┻━━┻╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰╯''')
    print('''Elige una de estas dos opciones:\n
        \t1) Cifrar un mensaje.
        \t2) Descifrar un criptograma.
        ''')

    opcion = int(input("Opción >"))
    if opcion == 1:
        clave = []
        for k in range(0, 4):
            clave.append(int(input("Clave >")))
        isInv(clave)
        mensaje = input("Mensaje >")

        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        resultado = cifrar(clave, mensaje.upper().replace(' ', ''))
        print("Resultado: ", resultado)
    else:
        clave = []
        for k in range(0, 4):
            clave.append(int(input("Clave >")))
        isInv(clave)
        mensaje = input("Mensaje >")

        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        resultado = descifrar(clave, mensaje.upper().replace(' ', ''))
        print("Resultado: ", resultado)


def cifrar(clave, mensaje):  # función para cifrado
    print('Cifrado Hill'. center(20, '*'))
    return procesar(clave, mensaje, 'cifrar')


def descifrar(clave, mensaje):  # función para descifrado
    print('Descifrado Hill'. center(24, '*'))
    return procesar(clave, mensaje, 'descifrar')


# función encargada de realizar el cifrado y descifrada del mensaje
def procesar(clave, mensaje, modo):
    if (modo == "cifrar"):
        abecedario = {}
        abecedario2 = {}
        abecedario = abcedarioC(abecedario)
        abecedario2 = abcedarioD(abecedario2)
        matrizllave = [1, 2, 3, 4]
        matriztexto = []
        cifrado = []
        final = []
        resultado = ""
        # convertir len de texto en par agregando un espacio si es necesario.
        if len(mensaje) % 2 != 0:
            mensaje = mensaje + " "

        # crear matriz clave
        for i in range(0, 4):
            matrizllave[i] = int(clave[i])

        # crear matriz para texto. las letras son numeros
        for i in range(0, len(mensaje)):
            matriztexto.append(abecedario[mensaje[i]])

        # multiplicacion de matriz de llave y texto
        x = 0
        y = 1

        while y < len(mensaje):
            # Se multiplican las llaves de la matriz por una matriz del rexto para encriptarlo
            a = (matrizllave[0] * matriztexto[x]) + \
                (matrizllave[2] * matriztexto[y])
            b = (matrizllave[1] * matriztexto[x]) + \
                (matrizllave[3] * matriztexto[y])

            # Se emplea el modulo 26 por el abecedario
            a = a % 26
            b = b % 26

            # En una lista escribe el dato y lo adjunta en una cadena
            cifrado.append(a)
            cifrado.append(b)

            x = x + 2
            y = y + 2

        for i in range(0, len(cifrado)):
            final.append(abecedario2[str(cifrado[i])])

        # imprimir cifrado
        for i in range(0, len(final)):
            resultado = resultado + final[i]

        
    else:
        abecedario = {}
        abecedario2 = {}
        abecedario = abcedarioC(abecedario)
        abecedario2 = abcedarioD(abecedario2)
        matrizllave = [1, 2, 3, 4]
        matriztexto = []
        descifrado = []
        final = []
        resultado = ""
        if len(mensaje) % 2 != 0:
            mensaje = mensaje + " "


        # crear matriz para texto. las letras son numeros
        for i in range(0, len(mensaje)):
            matriztexto.append(abecedario[mensaje[i]])

        a = int(clave[0])
        b = int(clave[1])
        c = int(clave[2])
        d = int(clave[3])

        # La matriz adjunta
        matrizllave = [[a, c], [b, d]]
        matrizADJ = [[d, c*-1], [b*-1, a]]
        # La determinante
        determinante = int(numpy.linalg.det(matrizllave))
        determinante = determinante % 26

        # calcular inverso de determinante por modulo inverso, tomado de:
        # https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
        inv = pow(determinante, 24, 26)

        matrizADJ[0][0] = (matrizADJ[0][0]*inv) % 26
        matrizADJ[1][0] = (matrizADJ[1][0]*inv) % 26
        matrizADJ[0][1] = (matrizADJ[0][1]*inv) % 26
        matrizADJ[1][1] = (matrizADJ[1][1]*inv) % 26

        x = 0
        y = 1
        # print matriztexto
        while y < len(mensaje):
            a = (matrizADJ[0][0] * matriztexto[x]) + \
                (matrizADJ[0][1] * matriztexto[y])
            b = (matrizADJ[1][0] * matriztexto[x]) + \
                (matrizADJ[1][1] * matriztexto[y])

            a = a % 26
            b = b % 26

            descifrado.append(a)
            descifrado.append(b)

            x = x + 2
            y = y + 2

        for i in range(0, len(descifrado)):
            final.append(abecedario2[str(descifrado[i])])

        # imprimir descifrado
        for i in range(0, len(final)):
            resultado = resultado + final[i]

        

    return resultado

# funcion encargada de  de validar que la matriz tiene inversa modular
def isInv(A):
    a = A[0]
    b = A[1]
    c = A[2]
    d = A[3]
    array = numpy.array([[a, b], [c, d]])
    print("\nclave:\n",array)
    determinante = numpy.linalg.det(array)
    gcd = math.gcd(int(determinante),26)
    if (determinante != 0) & (gcd == 1):
       print("La matriz tiene inversa modular => det(A)=", determinante,"y el determinante es coprimo con 26 gcd(deta,26) = ",gcd)
    else:
        print("La matriz no tiene inversa modular, det(A)=", determinante)
        print("Ingresa otra matriz")
        exit(0)


if __name__ == '__main__':
    main()
