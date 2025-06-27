import tkinter as tk

def presionar_tecla(tecla):
    if tecla == "=":
        try:
            resultado = str(eval(entrada.get()))
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, resultado)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Error")
    elif tecla == "C":
        entrada.delete(0, tk.END)
    else:
        entrada.insert(tk.END, tecla)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Entrada para mostrar los números
entrada = tk.Entry(ventana, font=("Arial", 20), borderwidth=2, relief="solid", justify="right")
entrada.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipadx=10, ipady=10)

# Definir botones
botones = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "=", "+"),
    ("C",)
]

# Crear los botones dinámicamente
for i, fila in enumerate(botones):
    for j, tecla in enumerate(fila):
        tk.Button(
            ventana,
            text=tecla,
            width=5,
            height=2,
            font=("Arial", 18),
            command=lambda tecla=tecla: presionar_tecla(tecla)
        ).grid(row=i+1, column=j, padx=5, pady=5)

# Ejecutar la aplicación
ventana.mainloop()

