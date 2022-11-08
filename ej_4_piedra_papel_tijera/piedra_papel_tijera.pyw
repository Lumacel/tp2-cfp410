from tkinter import *
from playsound import playsound
import random

jugada_sound = "agua.mp3"
reset_sound = "metalico.mp3"

class App():

	opciones = {1:"PIEDRA",2:"PAPEL",3:"TIJERA"}

	def __init__(self):
		self.puntaje_usuario = 0
		self.puntaje_maquina = 0
		self.eleccion_maquina = 0
		self.eleccion_usuario = 0 

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

		self.label_jugador = Label(self.frame1,text=" USUARIO ", font=('bold', 15),bg="navy",fg="white").place(x=10,y=10,width=160)
	
		self.label_maquina = Label(self.frame1,text=" MÁQUINA ", font=('bold', 15),bg="navy",fg="white").place(x=215,y=10,width=160)
	
		self.label_elecc_jugador = Label(self.frame1,textvariable= self.show_jugador, font=('bold', 15)).place(x=40,y=75,width=100)
		
		self.label_elecc_maquina = Label(self.frame1,textvariable=self.show_maquina, font=('bold', 15)).place(x=245,y=75,width=100)
		
		self.label_info = Label(self.frame1,textvariable=self.show_info , font=('bold', 20),bg="#6495ed",fg="navy").place(x=10,y=130,width=370)
	
		self.frame2 = Frame(self.root,width="400", height="30")
		self.frame2.pack()

		self.piedra_button = Button(self.frame2,text="PIEDRA",relief="groove",command=self.espiedra).grid(row=0,column=0,ipadx=25)

		self.papel_button = Button(self.frame2,text="PAPEL",relief="groove",command=self.espapel).grid(row=0,column=1,ipadx=25)
		
		self.tijera_button = Button(self.frame2,text="TIJERA",relief="groove",command=self.estijera).grid(row=0,column=2,ipadx=25)
	
		self.frame3 = Label(self.root)
		self.frame3.pack()

		self.reset_button = Button(self.frame3,text="RESET",relief="groove",command=self.reset).grid(row=0,column=0,ipadx=25)

		self.salir_button = Button(self.frame3,text="SALIR",relief="groove",command=self.salir).grid(row=0,column=2,ipadx=25)
	
	def jugada_maquina(self):
		return random.randint(1,3)

	def mostrar_jugada(self):

		self.sonido(jugada_sound)
		self.eleccion_maquina = self.jugada_maquina()
		self.show_jugador.set(App.opciones[self.get_elecc_jugador()])
		self.show_maquina.set(App.opciones[self.get_elecc_maquina()])

	def reset(self):
		self.mostrar_info(f"{self.get_puntos_usuario()} \t          {self.get_puntos_maquina()}")
		self.sonido(reset_sound)
		self.puntaje_maquina=0
		self.puntaje_usuario=0

	def sonido(self,sonido):
		try:
			self.audio = playsound(sonido)
		except Exception as e:
			print(f"Error: {e}")

	def espiedra(self):
		self.eleccion_usuario = 1
		self.mostrar_jugada()
		if self.get_elecc_maquina() == 2:
			self.gana_maquina()
		elif self.get_elecc_maquina() == 3:
			self.gana_usuario()
		else:
			self.empate()

	def espapel(self):
		self.eleccion_usuario = 2
		self.mostrar_jugada()
		if self.get_elecc_maquina() == 3:
			self.gana_maquina()
		elif self.get_elecc_maquina() == 1:
			self.gana_usuario()
		else:
			self.empate()

	def estijera(self):
		self.eleccion_usuario = 3
		self.mostrar_jugada()
		if self.get_elecc_maquina() == 1:
			self.gana_maquina()
		elif self.get_elecc_maquina() == 2:
			self.gana_usuario()
		else:
			self.empate()

	def gana_maquina(self):
		self.puntaje_maquina+= 1
		self.mostrar_info("PUNTO PARA LA MÁQUINA")

	def gana_usuario(self):
		self.puntaje_usuario+=1
		self.mostrar_info("PUNTO PARA El USUARIO")

	def empate(self):
		self.mostrar_info("EMPATE")
		
	def get_elecc_jugador(self):
		return self.eleccion_usuario

	def get_elecc_maquina(self):
		return self.eleccion_maquina

	def get_puntos_usuario(self):
		return self.puntaje_usuario

	def get_puntos_maquina(self):
		return self.puntaje_maquina

	def mostrar_info(self,mensaje):
		self.show_info.set(mensaje)

	def salir(self):
		self.root.destroy()
		
def main():

	v1 = App()
	v1.root.mainloop()

if __name__=="__main__":
	main()
