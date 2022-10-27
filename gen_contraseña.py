import tkinter as tk
from tkinter import ttk

class App:
    ANCHO = 300
    ALTO = 200

    def __init__(self):

        self.root = tk.Tk()
        self.root.geometry()
        self.root.title("Generador de contraseña")

        self.root.mainloop()

def main():
    v= App()

if __name__ == "__main__":
    main()
