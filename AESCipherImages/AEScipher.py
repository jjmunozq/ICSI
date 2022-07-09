#Hecho por Julio Javier Muñoz Quiñones
import base64 as bs
import pyaes
import matplotlib.pyplot as plt
import cv2
import requests
import base64
import os
from matplotlib import image

Url = 'https://pbs.twimg.com/profile_images/1506659402983608323/loCMmF3U.jpg'
getImage = requests.get(Url).content
image= open("lord.jpg","wb")
image.write(getImage)
image.close()
lordpetro = cv2.imread("lord.jpg")
plt.imshow(lordpetro)

def openArchivo(nombreArchivo):
  f = open(nombreArchivo, 'rb')
  text  = f.read()
  f.close()
  return text

def guardar(nombreArchivo,data):
	f = open(nombreArchivo, 'wb')
	f.write(data)
	f.close()
	
def encryptAES(plaintext,key):
  encode64 = base64.b64encode(plaintext)
  print("AES cipher representación Base64 imagen original:")
  print(encode64)
  data = pyaes.AESModeOfOperationCTR(key)
  ciphertext = data.encrypt(plaintext)
  encode64 = base64.b64encode(ciphertext)
  decode64 = base64.b64decode(ciphertext)
  print("AES cipher representación Base64 imagen encriptado:")
  print(encode64)
  print("AES cipher representación bits imagen encriptado:")
  print(decode64)
  return ciphertext

def decryptAES(mensaje,key):
  data = pyaes.AESModeOfOperationCTR(key)
  plaintext = data.decrypt(text)
  return plaintext

if __name__=="__main__":	
  print('''AES Cipher Images\nElige una de estas dos opciones:\n
        \t1) Cifrar una imagen.
        \t2) Descifrar una imagen.
        ''')
  opc = int(input("opcion >"))
  if opc == 1:
    op = int(input ("generar clave, nivel de seguridad del algoritmo ...\n1.128 bits\n2.192 bits\n3.256 bits\n"))
    if op == 1:
      key = os.urandom(16)
    if op == 2:
      key = os.urandom(24)
    if op == 3:
      key = os.urandom(32)
    guardar("key.txt",key)  
    print("Procesando imagen con pyAES espere...")
    ruta = "lord.jpg"
    fp = open(ruta, 'rb')
    text  = fp.read()
    fp.close()
    e_text = encryptAES(text,key)
    guardar("imagenEncriptada.jpg",e_text)
  else:
    print("Procesando imagen con pyDes espere...")   
    text = openArchivo("imagenEncriptada.jpg")
    key = openArchivo("key.txt")
    print("Clave: ",key,"\n")
    d_text = decryptAES(text,key)
    print(base64.b64encode(d_text))
    guardar("imagenDesencriptada.jpg",d_text)