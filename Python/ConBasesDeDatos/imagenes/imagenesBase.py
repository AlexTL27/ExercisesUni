import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk #pil para Trabajar con imagenes
import io
import mysql
import mysql.connector
miImagen = None
mainWindow = tk.Tk()
mainWindow.geometry("400x600")

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
            visualizador.config(image=nvaImagen)
            visualizador.image=nvaImagen
            guardarBD.configure(state="normal")
        except Exception as err:
            messagebox.showinfo(f"Error al cargar la imagen {err}")
            
        
        


def GuardarImagen():
    global miImagen

    if not miImagen:
        messagebox.showerror("Error, debes seleccionar una imagen")
        return
    
    else:
        with open(miImagen, "rb") as file:
            imagenBytes = file.read()
            cn = Conectar()
            miCursor = cn.cursor()
            sql = "insert into imagenes (nombre,imagen) values(%s,%s)"
            valores=(miImagen.split("/")[-1], imagenBytes)
            miCursor.execute(sql,valores)
            cn.commit()
            cargarDatos()
            messagebox.showinfo("Informació","La imagen se ha guardado...")


def cargarDatos():
    eliminarDatos()
    cn = Conectar()
    miCursor = cn.cursor()
    sql = "select nombre from imagenes"
    miCursor.execute(sql)

    for nombre in miCursor:
        print(nombre)
        lstImagen.insert("", tk.END, text=nombre)

def eliminarDatos():
    for item in lstImagen.get_children():
        lstImagen.delete(item)


def itemSeleccionado(event):
    item = lstImagen.selection()
    nombre=lstImagen.item(item,"text")
    BuscarImagen(nombre)
    
def BuscarImagen(nombre):
    cn=Conectar()
    micursor = cn.cursor()
    sql = "select imagen from imagenes where nombre =%s"
    valores = (nombre,)
    micursor.execute(sql, valores)

    img = micursor.fetchone()[0]
    miImagen = Image.open(io.BytesIO(img))
    miImagen=miImagen.resize((300,200))

    foto = ImageTk.PhotoImage(miImagen)
    visualizador.config(image=foto)
    visualizador.image=foto

#BOton para guardar imagen
tk.Button(mainWindow, text="Seleccionar imagen",width=40,command=SeleccionarImagen).pack(pady=10)
visualizador = tk.Label(mainWindow)
visualizador.pack(pady=10)


#BOton para guardar en BD
guardarBD = tk.Button(mainWindow, text="Guardar en BD",width=40,command=GuardarImagen,state="disabled")
guardarBD.pack(pady=10)

#Imágenes inferiores

frmImagen = tk.LabelFrame(mainWindow,text="lista de imágenes",pady=10)

frmImagen.pack(fill="x")
lstImagen=ttk.Treeview(frmImagen)
lstImagen.column("#0")
lstImagen.heading("#0",text="Nombre")
lstImagen.pack(fill="both")

lblImagenPrevia = tk.Label(frmImagen,text="Texto aqui")
lblImagenPrevia.pack()
cargarDatos()
lstImagen.bind("<Double-Button-1>", itemSeleccionado)
mainWindow.mainloop()

