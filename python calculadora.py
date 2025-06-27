import tkinter as tk
import math

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
    elif tecla == "√":
        try:
            resultado = str(math.sqrt(float(entrada.get())))
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, resultado)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Error")
    elif tecla == "%":
        try:
            resultado = str(float(entrada.get()) / 100)
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, resultado)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Error")
    elif tecla in ["sin", "cos", "tan", "log", "exp"]:
        try:
            valor = float(entrada.get())
            if tecla == "sin":
                resultado = str(math.sin(math.radians(valor)))
            elif tecla == "cos":
                resultado = str(math.cos(math.radians(valor)))
            elif tecla == "tan":
                resultado = str(math.tan(math.radians(valor)))
            elif tecla == "log":
                resultado = str(math.log10(valor))
            elif tecla == "exp":
                resultado = str(math.exp(valor))
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, resultado)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "Error")
    else:
        entrada.insert(tk.END, tecla)

def alternar_calculadora():
    global modo_cientifico
    modo_cientifico = not modo_cientifico
    actualizar_botones()

def actualizar_botones():
    for widget in frame_botones.winfo_children():
        widget.destroy()

    if modo_cientifico:
        botones_cientificos = [
            ("sin", "cos", "tan", "log"),
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+"),
            ("C", "√", "exp", "")
        ]
    else:
        botones_cientificos = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", ".", "=", "+"),
            ("C", "√", "%", "")
        ]

    for i, fila in enumerate(botones_cientificos):
        for j, tecla in enumerate(fila):
            if tecla:  # Solo crear botones si la tecla no está vacía
                tk.Button(
                    frame_botones,
                    text=tecla,
                    width=5,
                    height=2,
                    font=("Arial", 18),
                    command=lambda tecla=tecla: presionar_tecla(tecla),
                    bg="#00ff00",  # Color fluorescente
                    fg="#000000",  # Color del texto
                    relief="raised",  # Efecto 3D
                    bd=5,  # Grosor del borde
                    activebackground="#ff00ff",  # Color al presionar
                    activeforeground="#000000"  # Color del texto al presionar
                ).grid(row=i, column=j, padx=5, pady=5)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("400x500")
ventana.configure(bg="#000000")  # Color de fondo negro

# Entrada para mostrar los números
entrada = tk.Entry(ventana, font=("Arial", 20), borderwidth=2, relief="solid", justify="right", bg="#ffffff", fg="#000000")
entrada.grid(row=0, column=0, columnspan=4, pady=10, padx=10, ipadx=10, ipady=10)

# Frame para los botones
frame_botones = tk.Frame(ventana, bg="#000000")
frame_botones.grid(row=1, column=0, columnspan=4)

# Modo de calculadora
modo_cientifico = False

# Botón para alternar entre calculadora normal y científica
tk.Button(
    ventana,
    text="Modo Científico",
    command=alternar_calculadora,
    bg="#ff00ff",
    fg="#000000",
    font=("Arial", 16),
    relief="raised",
    bd=5
).grid(row=2, column=0, columnspan=4, pady=10)

# Inicializar botones
actualizar_botones()

# Ejecutar la aplicación
ventana.mainloop()

