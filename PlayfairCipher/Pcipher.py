#Realizado por Julio Javier Muñoz Quiñones 

import re,sys

ABCEDARIO = "ABCDEFGHIKLMNOPQRSTUVWXYZ" #la letra I es igaul a IJ

def playfair(clave,mensaje,opcion): 
    print("Playfair cipher")    
    
    if opcion == 1:
        print("Cifrar") 
        claveGenerada = matrizClave(clave)
        mostrarMatrix(claveGenerada)
        resultado = cifrar(claveGenerada,mensaje)
        print("\n",resultado)
    elif opcion == 2:
        print("Descifrar") 
        claveGenerada = matrizClave(clave)
        mostrarMatrix(claveGenerada)
        resultado = descifrar(claveGenerada,mensaje)
        print("\n",resultado)
    

def matrizClave(clave): #Creación de matriz
    nuevaClave=""
    clave = re.sub(r'[J]','I',clave)
    alfabeto = list(ABCEDARIO)
    for i in range(len(clave)):
        if clave[i] not in nuevaClave:
            nuevaClave += clave[i]
            alfabeto.remove(clave[i])
    clave = nuevaClave + "".join(alfabeto)
    return clave

def mostrarMatrix(clave): #muestra martriz creada
    print("Matriz Generada")
    for x in range(0,5):
        for y in range(5*x,5*(1+x)):
                print(clave[y]," ",end="")
        print() 

def cifrar(clave,mensaje): #función para cifrado
    return procesar(clave,mensaje,'cifrar')

def descifrar(clave, mensaje): #función para descifrado
    return procesar(clave,mensaje,'descifrar')


def diagramar(a,b,clave,modo): #Sustitución diagrámica del texto plano
    if modo == 'cifrar':
        if a == b:
            b = 'X'
    else:
        if a == b:
            print("Error, existen dos letras iguales en una tupla")
            sys.exit()
    
    fila_a,col_a = clave.index(a)//5,clave.index(a)%5 #Encargadas de hallar las coordenadas
    fila_b,col_b = clave.index(b)//5,clave.index(b)%5 #de las variables a y b en la matriz
    
    if modo == 'cifrar':
        posicion = 1
    elif  modo == 'descifrar':
        posicion = -1

    if fila_a == fila_b:#Sustitución simple (misma fila) => un lugar a la derecha o uno a la izquierda
        return (clave[fila_a*5+(col_a+posicion)%5] + clave[fila_b*5+(col_b+posicion)%5])          
    elif col_a == col_b:#Sustitución simple (misma columna)=> un lugar abajo o uno arriba
        return (clave[((fila_a+ posicion)%5)*5+col_a] + clave[((fila_b+ posicion)%5)*5+col_b]) 
    else:#no están alineadas => se reemplazan por aquellas que estan en la misma fila, pero 
        #en el otro par de vértices del rectangulo que define el par original       
        return (clave[fila_a*5 + col_b] + clave[fila_b*5 + col_a])


def procesar(clave, mensaje,modo):#función encargada de realizar el cifrado y descifrada del mensaje
    mensaje =re.sub(r'[J]','I',mensaje)
    salida = ''
    if len(mensaje) % 2 == 1:
        mensaje += 'X'
        salida = ''
    for c in range(0,len(mensaje),2):
        salida += diagramar(mensaje[c],mensaje[c+1],clave,modo)+' '
    return salida        

#UGRMKCSXHMUFMKBTOXGCMVATLUIV 
inClave = 'MONARCHY'
inMensaje = 'WEAREDISCOVEREDSAVEYOURSELFX'
inopcion = 1

playfair(inClave,inMensaje,inopcion)