from tkinter import *

class App_sorteo:
	def __init__(self):

		self.root = Tk()
		self.root.title("Sorteo (Rifa)") 
		self.root.geometry("350x500")

		self.participantes = {}
		self.numeros = []

		self.cant_num = StringVar()
		self.info = StringVar()
	
		self.label_cant_num = Label(self.root,text="CANTIDAD DE NÚMEROS A SORTEAR ")
		self.label_cant_num.place(x=10 , y=10)

		self.entry_cant_num = Entry(self.root,textvariable = self.cant_num,width=3)
		self.entry_cant_num.place(x=230,y=10)

		self.btn_cant_num = Button(self.root,text="ACEPTAR", command= self.generar_numeros)
		self.btn_cant_num.place(x=265,y=10)

		self.entry_cant_num.focus_set()

		self.btn_ingr_part = Button(self.root,text="INGRESAR PARTICIPANTES", command= self.ingresar_participantes)
		self.btn_ingr_part.place(x=10,y=50)

		self.label_info = Label(self.root,textvariable = self.info,fg="blue",relief= "groove",width =46)
		self.label_info.place(x=10 , y=100)

		self.root.bind('<Return>', self.generar_numeros)
		
	def get_cant_num(self):
		return self.cant_num.get()

	def generar_numeros(self,*args):
		self.numeros = []		
		try:
			cantidad = abs(int(self.get_cant_num()))
			for i in range(0,cantidad):
				self.numeros.append(i)
			print(self.numeros)
			self.info.set(f"SE SORTEARÁN {cantidad} NÚMEROS")
		except:
			self.info.set("POR FAVOR INGRESE UN NÚMERO VÁLIDO")

	def ingresar_participantes(self):
		self.top_level= Toplevel()
	
		

def main():
	s = App_sorteo()
	s.root.mainloop()

if __name__== "__main__":
	main()