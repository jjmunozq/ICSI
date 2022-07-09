#hecho por Julio Javier Muñoz Quiñones
import pyDes as ds
import base64 as bs

def guardar(nombreArchivo,data):
	f = open(nombreArchivo, 'wb')
	f.write(data)
	f.close()
	
def encryptDES(plaintext):
	BLOCK_SIZE = 8
	padding = b"@"
	plaintext = plaintext + ((BLOCK_SIZE - len(plaintext)) % BLOCK_SIZE) * padding
	cipherkey = ds.des(b"DESCRYPT", ds.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=ds.PAD_PKCS5)
	ciphertext = cipherkey.encrypt(plaintext)
	print("Imagen Encriptada\n")
	return ciphertext

def decryptDES(mensaje):
	cipherkey = ds.des(b"DESCRYPT", ds.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=ds.PAD_PKCS5)
	plaintext = cipherkey.decrypt(mensaje)
	print("Imagen Desencriptada\n")
	return plaintext

if __name__=="__main__":	
	print('''Des Cipher Images\nElige una de estas dos opciones:\n
        \t1) Cifrar una imagen.
        \t2) Descifrar una imagen.
        ''')
	opc = int(input("opcion >"))
	if opc == 1:
		print("Procesando imagen con pyDes espere...")
		ruta = "original.png"
		fp = open(ruta, 'rb')
		text  = fp.read()
		fp.close()
		e_text = encryptDES(text)
		eBase64 = bs.b64encode(e_text)
		#print ("mensaje cifrado en Base64: ", eBase64 )
		guardar("imagenEncriptada.png",eBase64)
	else:	
		print("Procesando imagen con pyDes espere...")   
		ruta = "imagenEncriptada.png"
		fp = open(ruta, 'rb')
		text  = fp.read()
		fp.close()
		dBase64 = bs.b64decode(text)
		d_text = decryptDES(dBase64)
		#print ("mensaje descifrado en bits: ", dBase64)
		guardar("imagenDesencriptada.png",d_text)

