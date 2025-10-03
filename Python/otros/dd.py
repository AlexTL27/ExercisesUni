import tkinter as tk

ventana = tk.Tk()
ventana.title("Ejemplo Radiobuttons")

# Variable que guarda el valor del Radiobutton seleccionado
opcion = tk.StringVar()
opcion.set("1")  # valor por defecto

# Crear Radiobuttons
radio1 = tk.Radiobutton(ventana, text="Opción 1", variable=opcion, value="1")
radio2 = tk.Radiobutton(ventana, text="Opción 2", variable=opcion, value="2")
radio3 = tk.Radiobutton(ventana, text="Opción 3", variable=opcion, value="3")

radio1.pack()
radio2.pack()
radio3.pack()

# Función para mostrar la opción seleccionada
def mostrar_seleccion():
    print("Seleccionaste la opción:", opcion.get())

boton = tk.Button(ventana, text="Aceptar", command=mostrar_seleccion)
boton.pack()

ventana.mainloop()
