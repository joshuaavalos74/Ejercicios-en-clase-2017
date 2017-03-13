from notas import calcular_notas
ingresa="si"
prom=0
notass=0
nota=0
while ingresa == "si":
	
	nota=int(input("ingrese nota : "))
	if nota >100:
		print ("la nota esta fuera de rango")
		nota=int(input("ingrese nota : "))
	if nota <=100:
		prom+=nota
	notass+=1		
	ingresa=input("quiere ingresar otra nota: ")	
promedio=calcular_notas(notas,prom)	
print (promedio)		
