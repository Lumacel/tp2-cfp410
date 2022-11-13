"""Escriba un programa que tome por teclado la temperatura media de cada día 
de la semana.Una vez tomados los datos que deben ser ingresados por teclado,
 debe informar la temperatura máxima y la mínima y qué día ocurrió cada una.
 """
from tkinter import *

class Ventana():
    def __init__(self):
        self.temperaturas = []
        self.indice = 0
        self.dias = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
        
        self.root= Tk()
        self.root.title("Temp. media semanal")
        self.root.geometry("400x100")

        self.texto_dias = StringVar()
        self.temp = StringVar()
        self.informe = StringVar()

        self.label1=Label(self.root,textvariable=self.texto_dias).place(x=10,y=10,width=140)

        self.texto_dias.set(f"Temperatura dia {self.dias[self.indice]}:")

        self.entry1=Entry(self.root,textvariable=self.temp,width=4)
        self.entry1.place(x=160,y=10,width=30)
        self.entry1.focus_set()

        self.root.bind('<Return>', self.guardar_datos)

        self.button1=Button(self.root,text="ACEPTAR",command=self.guardar_datos).place(x=210,y=7)

        self.label_informes = Label(self.root,textvariable=self.informe).place(x=10,y=50)

    def guardar_datos(self,*args):
        self.informe.set("")
        try:
            valor= float(self.temp.get())
            if self.get_indice() < 7:
                self.temperaturas.append(valor) 
                print(self.temperaturas)
                self.temp.set("")
                self.informe.set("Valor ingresado!")
                if self.get_indice() == 6:
                    self.mostrar_informe()
                    self.reset_valores()
                else:
                    self.indice+= 1
                    self.texto_dias.set(f"Temperatura dia {self.dias[self.indice]}:")     
        except:
            print("Valor incorrecto")
            self.informe.set("ERROR!! Ingrese un valor numérico por favor")
            self.temp.set("")
     
    def mostrar_informe(self):
        temp_min,temp_max = self.ver_max_min()

        index_min = self.temperaturas.index(temp_min)
        index_max = self.temperaturas.index(temp_max)

        dia_min = self.dias[index_min]
        dia_max = self.dias[index_max]
    
        mensaje = f"MINIMA= {temp_min}º ({dia_min}) \t\t MAXIMA= {temp_max}º ({dia_max})"
    
        self.informe.set(mensaje)
       
    def ver_max_min(self):
        return min(self.temperaturas),max(self.temperaturas)
       
    def reset_valores(self):
        self.temperaturas = []
        self.indice=0
        self.temp.set("")
        self.texto_dias.set(f"Temperatura dia {self.dias[self.indice]}:")
        
    def get_indice(self):
        return self.indice

def main():
    app = Ventana()
    app.root.mainloop()

if __name__== "__main__":
    main()

