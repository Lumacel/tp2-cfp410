"""Escriba un programa que tome por teclado la temperatura media de cada día 
de la semana.Una vez tomados los datos que deben ser ingresados por teclado,
 debe informar la temperatura máxima y la mínima y qué día ocurrió cada una.
 """
from tkinter import *

dias = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"]
temperaturas = []
temp_media=10
dia="Domingo"

def Ventana():
    root= Tk()
    root.title("Temperatura")
    root.geometry("300x100")

    temp = IntVar()
    temp_media = IntVar()


    Label(text=f"Ingrese temperatura dia {dia}:").grid(row=0,column=0)
    Entry(textvariable=temp,width=4).grid(row=1,column=0)
    Button(text="ACEPTAR",command=guardar_datos).grid(row=1,column=2)

    root.mainloop()

def guardar_datos():
   temperaturas.append(temp)



def informes():
    Label(text=f"La temperatura media ha sido: ").grid(row=2,column=0)
    Label(text=temp_media,width=4).grid(row=3,column=0)

def main():
    Ventana()

if __name__== "__main__":
    main()