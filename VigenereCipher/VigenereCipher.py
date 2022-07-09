# Hecho por Julio Javier Muñoz Quiñones
global alfabeto
Alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
COL_CLAVE = list(Alfabeto)
Numero = len(Alfabeto)
alfabeto = [''] * Numero


def main():
    print('''██╗░░░██╗██╗░██████╗░███████╗███╗░░██╗███████╗██████╗░███████╗░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
██║░░░██║██║██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
╚██╗░██╔╝██║██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝█████╗░░██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
░╚████╔╝░██║██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══╝░░██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
░░╚██╔╝░░██║╚██████╔╝███████╗██║░╚███║███████╗██║░░██║███████╗╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░░░╚═╝░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝''')
    print('''Elige una de estas dos opciones:\n
        \t1) Cifrar un mensaje.
        \t2) Descifrar un criptograma.
        ''')

    opcion = int(input("Opción >"))
    if opcion == 1:
        clave = input("Clave >")
        mensaje = input("Mensaje >")
        t = int(input("t >"))
        generarTabla()
        print("--------------------------------------------------------")
        print("Clave: ",funcionT(claveN(clave.upper(), mensaje),t))
        print("Mensaje: ",funcionT(mensaje.upper().replace(' ',''), t))
        print("--------------------------------------------------------")
        resultado = cifrar(clave, mensaje.upper().replace(' ',''))
        print("Resultado: ",funcionT(resultado, t))
    else:
        clave = input("Clave >")
        mensaje = input("Mensaje >")
        t = int(input("t >"))
        generarTabla()
        print("--------------------------------------------------------")
        print("Clave: ",funcionT(claveN(clave.upper(), mensaje),t))
        print("Mensaje: ",funcionT(mensaje.upper().replace(' ',''), t))
        print("--------------------------------------------------------")
        resultado = descifrar(clave, mensaje.upper().replace(' ',''))
        print("Resultado: ",funcionT(resultado, t))


def generarTabla():
    alfabeto[0] = Alfabeto
    for i in range(1, Numero):
        cadena = ''
        for j in range(0, Numero):
            pos = (j+1) % Numero
            cadena += alfabeto[i-1][pos]
        alfabeto[i] = cadena
    mostrarTabla(alfabeto)
    return alfabeto


def mostrarTabla(alfabeto):
    print('Tabla Vigenere'. center(20))
    for i in range(0, Numero):
        for j in range(0, Numero):
            print(alfabeto[i][j], end=' ')
            if j == Numero - 1:
                print()


def funcionT(Texto, t):
    index = 1
    resultado = ''
    for caracter in Texto:
        if index % t == 0:
            resultado += caracter + " "
            index += 1
        else:
            resultado += caracter
            index += 1

    return resultado


def cifrar(clave, mensaje):  # función para cifrado
    print('Cifrado Vigenere'. center(20, '*'))
    return procesar(clave, mensaje, 'cifrar')


def descifrar(clave, mensaje):  # función para descifrado
    print('Descifrado Vigenere'. center(24, '*'))
    return procesar(clave, mensaje, 'descifrar')


def claveN(clave, mensaje):
    multiple = int(len(mensaje)/len(clave) + 1)
    repeated_string = clave * multiple
    clave = repeated_string[:len(mensaje)]
    return clave


# función encargada de realizar el cifrado y descifrada del mensaje
def procesar(clave, mensaje, modo):
    clave = claveN(clave, mensaje)
    clave = ''.join(clave.split()).upper()
    salida = ''
    indice_clave = 0
    for simbolo in mensaje:
        pos = Alfabeto.find(simbolo)
        if pos != -1:

            n = Alfabeto.find(clave[indice_clave])
            if modo == 'cifrar':
                salida += alfabeto[n][pos]
            elif modo == "descifrar":
                pos = alfabeto[n].find(simbolo)
                salida += Alfabeto[pos]

            indice_clave += 1
            if indice_clave == len(clave):
                indice_clave = 0

    return salida


if __name__ == '__main__':
    main()
