# Hecho por Julio Javier Muñoz Quiñones
import numpy


def main():
    print('''
████████╗██╗░░░██╗██████╗░███╗░░██╗██╗███╗░░██╗░██████╗░██████╗░██╗██╗░░░░░██╗░░░░░░█████╗░██╗██████╗░██╗░░██╗███████╗██████╗░
╚══██╔══╝██║░░░██║██╔══██╗████╗░██║██║████╗░██║██╔════╝░██╔══██╗██║██║░░░░░██║░░░░░██╔══██╗██║██╔══██╗██║░░██║██╔════╝██╔══██╗
░░░██║░░░██║░░░██║██████╔╝██╔██╗██║██║██╔██╗██║██║░░██╗░██████╔╝██║██║░░░░░██║░░░░░██║░░╚═╝██║██████╔╝███████║█████╗░░██████╔╝
░░░██║░░░██║░░░██║██╔══██╗██║╚████║██║██║╚████║██║░░╚██╗██╔══██╗██║██║░░░░░██║░░░░░██║░░██╗██║██╔═══╝░██╔══██║██╔══╝░░██╔══██╗
░░░██║░░░╚██████╔╝██║░░██║██║░╚███║██║██║░╚███║╚██████╔╝██║░░██║██║███████╗███████╗╚█████╔╝██║██║░░░░░██║░░██║███████╗██║░░██║
░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝░╚════╝░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝''')
    print('''Elige una de estas dos opciones:\n
        \t1) Cifrar un mensaje.
        \t2) Descifrar un criptograma.
        ''')
    #bloque de entrada de datos
    opcion = int(input("Opción >"))
    if opcion == 1:
        index = 1
        tamano = int(input("Tamaño de la cardboard >\n"))
        hoyo = numpy.chararray((tamano, tamano))
        hoyo[:] = "-"
        print("Matriz:\n")
        coordenadas = imprimirCoordenadas(tamano)
        while True:
            print('''Elige la coordenada donde quieres realizar el hoyo ''',index,''':\n
            \t0) Marca coordenada X e Y.
            ''')
            x = int(input("Coordenada X >"))
            y = int(input("Coordenada Y >"))
            hoyo[x][y] = "0"
            print("Perforación realizada!")
            opcion1 = int(input('''¿Desea continuar perforando?
            \t1) Continuar.
            \t2) Terminar.
            '''))
            index += 1
            if opcion1 == 1:
                continue
            else:
                imprimirMatriz(hoyo, tamano)
                break
            
        mensaje = input("Mensaje >")
        print('''Elige la dirección de rotación:\n
        \t1) Dirección horario.
        \t2) Dirección antihorario.
        ''')
        dir_R = int(input("Dirección de rotación >"))
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        resultado = cifrar(mensaje.upper().replace(
            ' ', ''), hoyo, tamano, dir_R)
        print("Resultado: ", funcionT(resultado,tamano))
    else:
        tamano = int(input("Tamaño de la cardboard >\n"))
        hoyo = numpy.chararray((tamano, tamano))
        hoyo[:] = "-"
        print("Matriz:\n")
        coordenadas = imprimirCoordenadas(tamano)
        while True:
            index = 1
            print('''Elige dla coordenada donde quieres realizar el hoyo ''',index,''':\n
            \t0) Marca coordenada X e Y.
            ''')
            x = int(input("Coordenada X >"))
            y = int(input("Coordenada Y >"))
            hoyo[x][y] = "0"
            print("Perforación realizada!")
            opcion1 = int(input('''¿Desea continuar perforando?
            \t1) Continuar.
            \t2) Terminar.
            '''))
            index += 1
            if opcion1 == 1:
                continue
            else:
                imprimirMatriz(hoyo, tamano)
                break
        mensaje = input("Mensaje >")
        print('''Elige la dirección de rotación:\n
        \t1) Dirección horario.
        \t2) Dirección antihorario.
        ''')
        dir_R = int(input("Dirección de rotación >"))
        print("--------------------------------------------------------")
        print("--------------------------------------------------------")
        mensaje = mensaje.upper().replace(' ', '')
        resultado = descifrar(mensaje, hoyo, tamano, dir_R)
        print("Resultado: ", funcionT(resultado,tamano))


def cifrar(mensaje, tabla, tamano, rotacion):  # función para cifrado
    print('Cifrado Turning Grill'. center(20, '*'))
    return procesar(mensaje, tabla, rotacion, tamano, 'cifrar')


def descifrar(mensaje, tabla, tamano, rotacion):  # función para descifrado
    print('Descifrado Turrning Grill'. center(24, '*'))
    return procesar(mensaje, tabla, rotacion, tamano, 'descifrar')


# función encargada de realizar el cifrado y descifrada del mensaje
def procesar(mensaje, tabla, rotacion, tamano, modo):
    resultado = ""
    if (modo == "cifrar"):
        cuadrilla = numpy.chararray((tamano, tamano))

        aux = 0
        for k in range(4):
            for i in range(tamano):
                for j in range(tamano):
                    if tabla[i][j] == b'0':
                        cuadrilla[i][j] = mensaje[aux]
                        aux += 1
            if(rotacion == 1):
                tabla = girarHorario(tabla, tamano)
            else:
                tabla = girarAntihorario(tabla, tamano)
        print("\nMatriz resultado\n")
        imprimirMatriz(cuadrilla, tamano)
        print("\nTexto Cifrado\n")
        resultado=cuadrilla.flatten(order='A').decode('utf-8')       
    else:
        cuadrilla = numpy.chararray((tamano, tamano))
        cuadrilla = crearMatriz(mensaje, tamano)
        for k in range(4):
            for i in range(tamano):
                for j in range(tamano):
                    if tabla[i][j] == b'0':
                        resultado += cuadrilla[i][j].decode('utf-8')
            if(rotacion == 1):
                tabla = girarHorario(tabla, tamano)
            else:
                tabla = girarAntihorario(tabla, tamano)
        print("\nMatriz resultado\n")
        imprimirMatriz(cuadrilla, tamano)
        print("\nTexto descifrado\n")       
    return resultado

# funciones encargadas de hacer los giros
def girarHorario(tabla, tamano):
    matrix_R = numpy.chararray((tamano, tamano))
    contj = tamano - 1
    for i in range(tamano):
        conti = tamano - 1
        for j in range(tamano):
            matrix_R[i][j] = tabla[conti][i]
            conti -= 1
        contj -= 1
    return matrix_R

def girarAntihorario(tabla, tamano):
    matrix_R = numpy.chararray((tamano, tamano))
    contj = tamano - 1
    for i in range(tamano):
        conti = tamano - 1
        for j in range(tamano):
            matrix_R[i][conti] = tabla[conti][contj]
            conti -= 1
        contj -= 1
    return matrix_R

# crea la matriz que vamos a usa para desencriptar el mensaje
def crearMatriz(mensaje, tamano):
    aux = 0
    matriz = numpy.chararray((tamano, tamano))
    for i in range(tamano):
        for j in range(tamano):
            matriz[i][j] = mensaje[aux]
            aux += 1
    return matriz

# funciones de impresión de matrices
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

def imprimirCoordenadas(tamano):
    coord = []
    for i in range(tamano):
        for j in range(tamano):
            msj = str(i)+","+str(j)
            coord.append(msj)
            print(msj, "\t", end='')
        print("\n")
    return coord

def imprimirMatriz(charar, tamano):
    print("Tabla Terminada")
    for i in range(tamano):
        for j in range(tamano):
            print(charar[i][j].decode('utf-8'), "\t", end='')
        print("\n")

if __name__ == '__main__':
    main()
