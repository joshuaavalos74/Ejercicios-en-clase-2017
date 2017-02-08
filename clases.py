class Navegador(object):
	def __init__(self, nombre):
		self.nombre= nombre
		self.tabs=[]
	
	def agregar_tabs(self, tab):
		self.tabs.append(tab)	
	
	def cerrar_tab(self, quitar):
		quitar=-1
		self.tabs.pop(quitar)

	def	cerrar_todas_tabs(self):
		self.tabs = []


	def mostrar_tabs(self):
		for i in range(len(self.tabs)):
		return self.tabs[i]



	def guardar_tabs(self):
		atabs= open ("alltabs.txt","w")
		for i in len(self.tabs):
			atabs.write(i)
			atabs.write("\n")
		atabs.close()
		return atabs

		 