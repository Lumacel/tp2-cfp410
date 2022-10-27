import tkinter as tk
import key_gen

class App:
    ANCHO = 300
    ALTO = 200

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry(f"{App.ANCHO}x{App.ALTO}")
        self.root.title("Generador de contraseña")

        self.texto1 = tk.Label(text="Cantidad de caracteres")
        self.texto1.place(x=20,y=20)

        self.text_input = tk.Entry(width=2)
        self.text_input.place(x=160,y=20)

        self.cantidad = tk.IntVar

        self.text_key = tk.Label(textvariable= self.cantidad)
        self.text_key.place(x = 20,y=40)

        self.boton_gen = tk.Button(text="Generar clave", command = self.generar_contraseña )
        self.boton_gen.place(x = 20,y=50)

        self.root.mainloop()

    def generar_contraseña(self):

        cant = int(self.text_input.get())
      
        contraseña_generada = key_gen.gen_password(cant)
        self.cantidad.set(contraseña_generada)
        
       

def main():
    v= App()

if __name__ == "__main__":
    main()
