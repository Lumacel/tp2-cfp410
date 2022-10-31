import tkinter as tk
import key_gen

MAX_LENGHT=20

class App:
    ANCHO = 300
    ALTO = 200
    MAX_LENGHT=40

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry(f"{App.ANCHO}x{App.ALTO}")
        self.root.title("Generador de contraseña")
        self.root.resizable(0,0)

        self.texto1 = tk.Label(text=f"Longitud contraseña (MAX {App.MAX_LENGHT}):")
        self.texto1.place(x=20,y=20)

        self.text_input = tk.Entry(width=5)
        self.text_input.place(x=200,y=20)
        self.text_input.focus_set()
        
        self.password = tk.StringVar()
        self.notas = tk.StringVar()

        self.boton_gen = tk.Button(text="Generar clave", command = self.generar_contraseña )
        self.boton_gen.place(x = 20,y=50)

        self.text_key = tk.Label(textvariable= self.password)
        self.text_key.place(x = 20,y=110)

        self.notific = tk.Label(textvariable= self.notas, fg="blue")
        self.notific.place(x= 20, y = 170)

        self.root.bind('<Return>', self.generar_contraseña)

        self.root.mainloop()

    def clip(self, text):
            '''
            Copia el parámetro enviado 'text' al portapapeles
            '''
            self.root.clipboard_clear()
            self.root.clipboard_append(text)

    def generar_contraseña(self,*args):

        try:
            cant = abs(int(self.text_input.get()))
            if cant <= App.MAX_LENGHT:
                contraseña_generada = key_gen.gen_password(cant)
               
            else:
                contraseña_generada = key_gen.gen_password(App.MAX_LENGHT)

            self.password.set(contraseña_generada)
            self.clip(contraseña_generada)
            self.notas.set("Contraseña copiada al portapapeles")
            
        except:
            if self.text_input.get() == "":
                self.notas.set("ERROR!! ingrese algún valor")
            else:
                self.notas.set("ERROR!! ingrese valor numérico")

        
def main():
    v= App()

if __name__ == "__main__":
    main()
