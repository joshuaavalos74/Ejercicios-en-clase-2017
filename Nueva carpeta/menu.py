import clases
import clase_tab
print ("Bienvenido al navegador \n")
whattdo=int(input("""
1.Eliga el navegador.
2. Crear tab.
3. Cambiar URL del tab.
4. Cerrar un tab.
5. Cerrar todos los tabs
6. Mostrar los tabs.
7. Guardar los tabs.
8. Salir."""))

if whattdo == 1:
	nave= input("Que navegador desea utilizar? ")
	el_navegador= Navegador(nave)

elif whattdo== 2:
	pag= input("Ingrese el nombre de la pagina: ")	
	pag_url= input("Ingrese el URL deseado: ")
	mi_tab = Tab(pag, pag_url)
	el_navegador.agregar_tabs(mi_tab)
elif whattdo == 3:
	que_tab= input("Ingrese el numero del tab que desea cambiar: ")
	n_url= input("Ingrese el url nuevo: " )
	mi_tab.cambiar_url(que_tab, n_url)
elif whattdo == 4:
	que_tab= input("Ingrese el numero del tab que desea cerrar: ")
	el_navegador.cerrar_tab(que_tab)
elif whattdo == 5:
	seguro= input("Esta seguro que desea cerrar todas las tabs?  ")
	seguror= seguro.upper()
	el_navegador.cerrar_todas_tabs()
elif whattdo == 6:
	el_navegador.mostrar_tabs()	

	








































