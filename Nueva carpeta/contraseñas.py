import f_contraseñas
print ("Bienvenido al creador de contraseñas.")
letras=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S","T","U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
cant_password= int(input("Ingrese cuantas contraseñas quiere crear: "))
longitud=int(input("Ingrese la longitud de la contraseña: "))
print (f_contraseñas.hacer_password(cant_password, longitud, letras))
