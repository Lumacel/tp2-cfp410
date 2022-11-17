from tkinter import *
from tkinter import ttk


class App:
	MIN_NUM=2
	MAX_NUM=1000

	def __init__(self):

		self.root = Tk()
		self.root.title("SORTEO (RIFA)") 
		self.root.geometry("350x500")
		self.root.resizable(0,0)

		self.participantes = {}
		self.numeros = []

		self.cant_num = StringVar()
		self.info = StringVar()
	
		self.lbl_cant_num = Label(self.root,text="CANTIDAD DE NÚMEROS A SORTEAR ",relief="groove")
		self.lbl_cant_num.place(x=10 , y=10)

		self.entry_cant_num = Entry(self.root,textvariable = self.cant_num,width=4)
		self.entry_cant_num.place(x=230,y=10)

		self.btn_cant_num = Button(self.root,text="ACEPTAR", command= self.generar_numeros)
		self.btn_cant_num.place(x=265,y=10)

		self.entry_cant_num.focus_set()

		self.lbl_info = Label(self.root,textvariable = self.info,fg="blue",relief= "groove",width =46)
		self.lbl_info.place(x=10 , y=50)

		self.btn_ingr_particip1 = Button(self.root,text="INGRESAR PARTICIPANTES", command= self.ventana_ingreso)
		self.btn_ingr_particip1.place(x=95,y=85)

		self.root.bind('<Return>', self.generar_numeros)

		self.btn_ingr_particip1.config(state='disable')
	
	def get_cant_num(self):
		return self.cant_num.get()

	def generar_numeros(self,*args):
		self.numeros = []		
		try:
			cantidad = abs(int(self.get_cant_num()))
			if 1000 >= cantidad >= 2 :
				for i in range(0,cantidad):
					self.numeros.append(i)
				print(self.numeros)
				self.info.set(f"SE SORTEARÁN {cantidad} NÚMEROS")

				self.entry_cant_num.config(state="disable")
				self.btn_cant_num.config(state="disable")
				self.btn_ingr_particip1.config(state='normal')
				self.root.bind('<Return>', self.ventana_ingreso)
			else:
				self.info.set(f"NUMÉRO FUERA DE RANGO ({App.MIN_NUM}-{App.MAX_NUM})")

		except:
			if self.get_cant_num() == "":
				self.info.set("POR FAVOR INGRESE ALGÚN VALOR")
			else:
				self.info.set("POR FAVOR INGRESE SOLO VALORES NUMÉRICOs")

	
	def ventana_ingreso(self,*args):
		self.top_level = Toplevel()
		self.top_level.resizable(0,0)
		self.nombre_participante = StringVar()
		self.numero_elegido = StringVar()
		self.top_level.title("Ingrese participante")
		self.top_level.geometry("340x150")

		self.lbl_ing_particip = Label(self.top_level, text="PARTICIPANTE",width=15,relief="groove")
		self.lbl_ing_particip.place(x=10,y=10)

		self.entry_ing_particip = Entry(self.top_level,textvariable = self.nombre_participante,width=30)
		self.entry_ing_particip.place(x=140,y=10)

		self.lbl_ing_numero = Label(self.top_level, text="NUMEROS",width=15,relief="groove")
		self.lbl_ing_numero.place(x=10,y=35)

		self.entry_ing_numero = ttk.Combobox(self.top_level,values=self.numeros,state="readonly",width=4)
		self.entry_ing_numero.place(x=140,y=35)

		self.btn_aceptar = Button(self.top_level, text="INGRESAR",command = self.ingresar_participante,width=10)
		self.btn_aceptar.place(x=10,y=110)

		self.btn_salir = Button(self.top_level, text="SALIR",command = self.salir_top_level,width=10)
		self.btn_salir.place(x=245,y=110)

		self.btn_ingr_particip1.config(state='disable') #desabilita boton de primer ventana mientras se abre la segunda

	def ingresar_participante(self):
		pass

	def salir_top_level(self):
		self.top_level.destroy()
		self.btn_ingr_particip1.config(state='normal')



def main():
	s = App()
	s.root.mainloop()

if __name__== "__main__":
	main()

