import tkinter as tk
from tkinter import ttk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Simple")
        
        # Variable para almacenar el resultado
        self.result_var = tk.StringVar()
        
        # Crear y configurar el campo de resultado
        self.result_entry = ttk.Entry(root, textvariable=self.result_var, justify="right", state="readonly")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Botones de la calculadora
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        
        # Crear y posicionar los botones
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(root, text=button, command=cmd).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Configurar el redimensionamiento de la cuadrícula
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        
        self.equation = ""
    
    def click(self, button):
        if button == '=':
            try:
                self.result_var.set(eval(self.equation))
                self.equation = str(self.result_var.get())
            except:
                self.result_var.set("Error")
                self.equation = ""
        elif button == 'C':
            self.equation = ""
            self.result_var.set("")
        else:
            self.equation += button
            self.result_var.set(self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x400")
    app = Calculator(root)
    root.mainloop()