import tkinter as tk
#from tkinter import ttk

class Ventana:
	ANCHO,ALTO= 300,200

	def __init__(self):

		self.root = tk.Tk()
		

		self.root.title("Saludo con GUI")
		self.root.resizable(0, 0)
		self.root.geometry(f"{Ventana.ANCHO}x{Ventana.ALTO}")

		self.text1= tk.Label(text="Ingrese su nombre: ")
		self.text1.place(x=20,y=20)

		self.nombre= tk.StringVar()

		self.text_input = tk.Entry( width=20)
		self.text_input.place(x=130,y=20)
		self.text_input.focus_set()

		self.boton = tk.Button(text="saludo",command = self.saludar, relief="groove", borderwidth=4)
		self.boton.place(x=20,y=120)

		self.text_saludo = tk.Label(textvariable = self.nombre)
		self.text_saludo.place(x=20,y=70)

		self.root.bind('<Return>', self.saludar)
		self.root.mainloop()

	def saludar(self, *args):
		if len (self.text_input.get()) == 0:
			self.nombre.set("Hola amigazo!")
		else:
			self.nombre.set(f"Hola {self.text_input.get()}")

def main():
	v = Ventana()

if __name__ == "__main__":
	main()	


