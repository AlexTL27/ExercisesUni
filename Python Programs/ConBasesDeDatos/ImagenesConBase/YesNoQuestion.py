import tkinter as tk
from tkinter import ttk, filedialog, messagebox

import mysql.connector


from PIL import Image, ImageTk #pil para Trabajar con imagenes

import back
ventanaPrincipal = tk.Tk()

miImagen = None

def Conectar():
    cn = mysql.connector.connect(host="localhost",
                                         user="root",
                                         password = "",
                                         port="3306",
                                         database="universidad")
    return cn


def SeleccionarImagen():
    global miImagen
    miImagen = filedialog.askopenfilename(initialdir="/", title="Buscar Imagen",
                                          filetypes=(("Archivos de imagen", "*.jpg *.jpeg *.png *.gif"),("Todos los archivos","*.*")))
    
    if miImagen:
        try:
            imagen = Image.open(miImagen)
            imagen.thumbnail((400,200))
            nvaImagen = ImageTk.PhotoImage(imagen)
            imagenLabel.config(image=nvaImagen)
            imagenLabel.image=nvaImagen
            
           
        except Exception as err:
            messagebox.showinfo(f"Error al cargar la imagen {err}")
            

def limpiarEntradas():
    global miImagen

    #LIMPIAMOS LAS ENTRADAS
    pregunta.delete(0,tk.END)
    dirCombo.set("Selecciona una opción")
    #se resetea ruta
    miImagen = None
    #se resetea label
    imagenLabel.config(image=None)
    imagenLabel.image=None
    



def GuardarBD():
    global miImagen

    if not pregunta.get():
        messagebox.showerror("Ingresa la pregunta")
        return
    if dirCombo.get() == "Selecciona una opción":
        messagebox.showerror("Ingresa de que manera se resolvera la pregunta")
        return 
    if  not miImagen:
        messagebox.showerror("Carga la imagen")
        return
    
    with open(miImagen, "rb") as file:
            imagenBytes = file.read()

   
    #Invocamos al back y creamos un objeto, despues limpiamos entradas
    back.pregunta(pregunta.get(), dirCombo.get(), imagenBytes, miImagen.split("/")[-1])

    limpiarEntradas()
    InsertarDatosTree()
    messagebox.showinfo("Se guardo en la BD")
    

def InsertarDatosTree():
    eliminarDatos()
    cn = Conectar()
    miCursor = cn.cursor()
    sql = "select id,pregunta,respuesta, nombreImg from yesnoquestion"
    miCursor.execute(sql)

    for fila in miCursor:
        # fila es una tupla como (1, "¿Te gusta el café?", "sí")
        lstImagen.insert("", "end", values=fila)

def eliminarDatos():
    for item in lstImagen.get_children():
        lstImagen.delete(item)


def itemSeleccionado(event):
    item = lstImagen.selection()
    valores = lstImagen.item(item, "values")
    print(valores)
    back.VentanaNueva(valores)



tk.Label(ventanaPrincipal, text="Yes No Question",bg="pink").pack()

frameContenidoPrincipal = tk.Frame(ventanaPrincipal, bg="gray",pady=20,padx=20)
frameContenidoPrincipal.pack(fill="both",expand=True)


#pregunta
tk.Label(frameContenidoPrincipal,text="Ingresa la pregunta:  ",pady=20, bg="gray").grid(row=0,column=0,sticky="w")
pregunta = tk.Entry(frameContenidoPrincipal, width=30)
pregunta.grid(row=0, column=1)

#Respuesta imposible de selecionar
tk.Label(frameContenidoPrincipal,text="Selecciona le respuesta imposible de seleccionar:  ",pady=20, bg="gray").grid(row=1,column=0,sticky="w")
opciones = ("si","no")
dirCombo = ttk.Combobox(frameContenidoPrincipal,values=opciones,state="readonly",width=30)
dirCombo.set("Selecciona una opción")
dirCombo.grid(row=1, column=1)

#Respuesta usuario
tk.Label(frameContenidoPrincipal,text="Carga la imagen de broma:  ",pady=20, bg="gray").grid(row=2,column=0,sticky="w")

#BOton para guardar imagen
tk.Button(frameContenidoPrincipal, text="Seleccionar imagen",width=40,command=SeleccionarImagen).grid(row=2,column=1)


frameImagen= tk.Frame(frameContenidoPrincipal, bg="black",width=400, height=200)
frameImagen.grid(row=0, column=2, rowspan=3, padx=30, pady=10)

frameImagen.grid_propagate(False)


imagenLabel = tk.Label(frameImagen,text="Imagen a cargar aquí", bg="gray")
imagenLabel.grid()

#BOton para guardar pregunta
tk.Button(ventanaPrincipal, text="Guardar yes no question",width=40,command=GuardarBD).pack(pady=10)


#preguntas inferiores

style = ttk.Style()
style.configure("Treeview", font=("Arial", 12))  # Filas
style.configure("Treeview.Heading", font=("Arial", 14, "bold"))  # Encabezados

frmPreguntas= tk.LabelFrame(ventanaPrincipal,text="lista de preguntas",pady=10)
frmPreguntas.pack(fill="x")

lstImagen=ttk.Treeview(frmPreguntas,  columns=("id","pregunta", "respuesta", "imagen"), show="headings")


lstImagen.heading("id",text="ID")
lstImagen.heading("pregunta",text="Pregunta")
lstImagen.heading("respuesta",text="Respuesta")
lstImagen.heading("imagen",text="Imagen")

# Opcional: ajustar ancho y alineación
lstImagen.column("id", width=20, anchor="center")
lstImagen.column("pregunta", width=300)
lstImagen.column("respuesta", width=100, anchor="center")
lstImagen.column("imagen", width=200, anchor="center")

lstImagen.pack(fill="both")

lstImagen.bind("<Double-Button-1>", itemSeleccionado)
InsertarDatosTree()
ventanaPrincipal.mainloop()
