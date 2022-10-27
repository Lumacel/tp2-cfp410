import tkinter as tk
from tkinter import ttk

class Ventana:
	ANCHO,ALTO= 300,200

	def __init__(self):

		self.root = tk.Tk()
		self.root.title("Saludo con GUI")
		self.root.geometry(f"{Ventana.ANCHO}x{Ventana.ALTO}")

		self.text1= tk.Label(text="Ingrese su nombre: ")
		self.text1.place(x=20,y=20)

		self.nombre= tk.StringVar()

		self.text_input = ttk.Entry(textvariable = self.nombre, width=20)
		self.text_input.place(x=130,y=20)

		
		self.boton = tk.Button(text="saludo",command = self.saludar)
		self.boton.place(x=20,y=120)

		self.root.mainloop()

	

	def saludar(self):
		if len (self.text_input.get()) == 0:
			self.text_saludo = tk.Label(text="Hola amigo")
		else:

			self.text_saludo = tk.Label(text=f"Hola {self.text_input.get()}")
		self.text_saludo.place(x=20,y=70)


def main():
	v = Ventana()


if __name__ == "__main__":
	main()	


