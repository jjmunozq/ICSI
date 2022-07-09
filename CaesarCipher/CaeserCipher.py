# Hecho por Julio Javier Muñoz Quiñones

ABCDARIO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def cifrar(mensaje, k):
    mensaje = mensaje.replace(" ", "")
    resultado = ''
    index = 1
    print("Cifrado cesar (Cifrar)")
    for caracter in mensaje.upper():
        if caracter in ABCDARIO:
            pos = ABCDARIO.find(caracter)

            pos = (pos + k) % 26
            if index % 5 == 0:
                resultado += ABCDARIO[pos] + " "
                index += 1
            else:
                resultado += ABCDARIO[pos]
                index += 1
        else:
            resultado += caracter

    return resultado


def descifrar(mensaje, k):
    mensaje = mensaje.replace(" ", "")
    resultado = ''
    index = 1
    print("Cifrado cesar (Descifrar)")
    for caracter in mensaje.upper():
        if caracter in ABCDARIO:
            pos = ABCDARIO.find(caracter)

            pos = (pos - k) % 26
            if index % 5 == 0:
                resultado += ABCDARIO[pos] + " "
                index += 1
            else:
                resultado += ABCDARIO[pos]
                index += 1

        else:
            resultado += caracter

    return resultado


def caeserCipher(mensaje, k, op):
    if op == 0:
        salida = cifrar(mensaje, k)
    else:
        salida = descifrar(mensaje, k)

    return salida


#print(caeserCipher('njsbe efusbt qjabssb', 1, 1))

#print(caeserCipher('hola mundo', 9, 0))
#print(caeserCipher('qxujvdwmx', 9, 1))

#print(caeserCipher('Lleva el nombre de Julio Cesar es uno de los tipos de cifrados mas antiguos y se basa en el cifrado monoalfabetico mas simple', 9, 0))
print(caeserCipher('UUNEJ NUWXV KANMN SDURX LNBJA NBDWX MNUXB CRYXB MNLRO AJMXB VJBJW CRPDX BHBNK JBJNW NULRO AJMXV XWXJU OJKNC RLXVJ BBRVY UN', 9, 1))