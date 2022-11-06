from tkinter import *
from playsound import playsound
import random

class App():

	opciones = {1:"PIEDRA",2:"PAPEL",3:"TIJERA"}

	def __init__(self):
		self.puntaje_usuario = 0
		self.puntaje_maquina = 0
		self.eleccion_maquina = 0
		self.eleccion_usuario =0

		self.root = Tk()

		self.show_jugador = StringVar()
		self.show_maquina = StringVar()
		self.show_info = StringVar()

		self.root.title("PIEDRA-PAPEL-TIJERA")
		self.root.resizable(height = 0, width = 0)

		self.root.config(bg="lightgrey",relief="groove", bd=8)  
	          
		self.frame1 = Frame(self.root,width="400", height="200")
		self.frame1.pack()
		self.frame1.config(bg="#6495ed",relief="sunken",bd=8)

		self.label_jugador = Label(self.frame1,text=" USUARIO ", font=('bold', 15),bg="navy",fg="white")
		self.label_jugador.place(x=10,y=10,width=160)

		self.label_maquina = Label(self.frame1,text=" MÁQUINA ", font=('bold', 15),bg="navy",fg="white")
		self.label_maquina.place(x=215,y=10,width=160)

		self.label_elecc_jugador = Label(self.frame1,textvariable= self.show_jugador, font=('bold', 15))
		self.label_elecc_jugador.place(x=40,y=75,width=100)

		self.label_elecc_maquina = Label(self.frame1,textvariable=self.show_maquina, font=('bold', 15))
		self.label_elecc_maquina.place(x=245,y=75,width=100)

		self.label_info = Label(self.frame1,textvariable=self.show_info , font=('bold', 20),bg="#6495ed",fg="navy")
		self.label_info.place(x=10,y=140,width=370)

		self.frame2 = Frame(self.root,width="400", height="30")
		self.frame2.pack()

		self.piedra_button = Button(self.frame2,text="PIEDRA",relief="groove",command=self.espiedra)
		self.piedra_button.grid(row=0,column=0,ipadx=25)

		self.papel_button = Button(self.frame2,text="PAPEL",relief="groove",command=self.espapel)
		self.papel_button.grid(row=0,column=1,ipadx=25)

		self.tijera_button = Button(self.frame2,text="TIJERA",relief="groove",command=self.estijera)
		self.tijera_button.grid(row=0,column=2,ipadx=25)

		self.frame3 = Label(self.root)
		self.frame3.pack()

		self.reset_button = Button(self.frame3,text="RESET",relief="groove",command=self.reset)
		self.reset_button.grid(row=0,column=0,ipadx=25)


		self.salir_button = Button(self.frame3,text="SALIR",relief="groove",command=self.salir)
		self.salir_button.grid(row=0,column=2,ipadx=25)

	def jugada_maquina(self):
		return random.randint(1,3)

	def mostrar_jugada(self):
		self.sonido()
		self.eleccion_maquina = self.jugada_maquina()
		self.show_jugador.set(App.opciones[self.get_jugador()])
		self.show_maquina.set(App.opciones[self.get_maquina()])

	def sonido(self):
		self.audio = playsound("agua.mp3")

	def espiedra(self):
		self.eleccion_usuario = 1
		self.mostrar_jugada()
		if self.eleccion_maquina == 2:
			self.gana_maquina()
		elif self.eleccion_maquina == 3:
			self.gana_usuario()
		else:
			self.empate()

	def espapel(self):
		self.eleccion_usuario = 2
		self.mostrar_jugada()
		if self.eleccion_maquina == 3:
			self.gana_maquina()
		elif self.eleccion_maquina == 1:
			self.gana_usuario()
		else:
			self.empate()

	def estijera(self):
		self.eleccion_usuario = 3
		self.mostrar_jugada()
		if self.eleccion_maquina == 1:
			self.gana_maquina()
		elif self.eleccion_maquina == 2:
			self.gana_usuario()
		else:
			self.empate()
		
	def get_jugador(self):
		return self.eleccion_usuario

	def get_maquina(self):
		return self.eleccion_maquina

	def get_puntos_usuario(self):
		return self.puntaje_usuario

	def get_puntos_maquina(self):
		return self.puntaje_maquina

	def gana_maquina(self):
		self.puntaje_maquina+= 1
		self.mostrar_info("PUNTO PARA LA MÁQUINA")

	def gana_usuario(self):
		self.puntaje_usuario+=1
		self.mostrar_info("PUNTO PARA El USUARIO")

	def empate(self):
		self.mostrar_info("EMPATE")

	def mostrar_info(self,mensaje):
		self.show_info.set(mensaje)

	def reset(self):
		self.mostrar_info(f"{self.get_puntos_usuario()} \t          {self.get_puntos_maquina()}")
		self.puntaje_maquina=0
		self.puntaje_usuario=0

	def salir(self):
		self.root.destroy()
		

def main():

	v1 = App()
	v1.root.mainloop()

if __name__=="__main__":
	main()
