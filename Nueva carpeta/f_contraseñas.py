import random
def hacer_archivo (passwords):
	archivo= open("passwords.txt","w")
	archivo.close()

def hacer_password(cant_password, longitud, letras):
	passwords = []
	for i in range(cant_password):
		passf=[]
		random.shuffle(letras)
		for i in range(longitud):
			passf.append(letras[i])
		passwords.append(passf)
	return passwords		

def convert_en_txt (listasa):
		

			




