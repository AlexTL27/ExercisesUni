import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo con Frame")

tk.Label(text="uwu").pack()
# Frame es una caja dentro de la ventana principal
miFrame = tk.Frame(ventana, bg="gray")
miFrame.pack(padx=10, pady=10)

# Widgets dentro del frame
tk.Label(miFrame, text="Nombre:").pack()
tk.Entry(miFrame).pack()
tk.Button(miFrame, text="Enviar").pack()

ventana.mainloop()
