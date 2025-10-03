import tkinter as tk
from tkinter import ttk
import time
#Array donde se guardaran mis contactos, de manera temporal
contactos = []
ventana = tk.Tk()
ventana.title("Menú")
ventana.geometry("400x600")
ventana.configure(bg="#8cdb86")


#Titulos
textoBienvenida = tk.Label(text="===Agenda===", font=("Arial",12))
textoBienvenida.grid(row=0,column=0,columnspan=3,padx=110, pady=40)



##apartados,registrar persona
class persona_a_registrar:
    def __init__(self, Nombre, Apellido, Telefono, Genero):
        self.nombre = Nombre
        self.apellido = Apellido
        self.telefono = Telefono
        self.genero = Genero




###
nombreEtiqueta = tk.Label(ventana,text="Nombre:")
nombreEtiqueta.grid(row=1,column=0,padx=40,pady=20)

nombreCajaTexto = tk.Entry(ventana)
nombreCajaTexto.grid(row=1,column=1,pady=20)


apellidoEtiqueta = tk.Label(ventana,text="Apellido:")
apellidoEtiqueta.grid(row=2,column=0,padx=40,pady=20)

apellidoCajaTexto = tk.Entry(ventana)
apellidoCajaTexto.grid(row=2,column=1,pady=20)


telefonoEtiqueta = tk.Label(ventana,text="Teléfono:")
telefonoEtiqueta.grid(row=3,column=0,padx=40,pady=20)

telefonoCajaTexto = tk.Entry(ventana)
telefonoCajaTexto.grid(row=3,column=1,pady=20)

erroresEtiqueta = tk.Label(ventana,text=":)")
erroresEtiqueta.grid(row=6,column=0,columnspan=3,pady=20)

#creamos el boton combo
generoEtiqueta = tk.Label(ventana,text="Género")
generoEtiqueta.grid(row=4,column=0,padx=40,pady=20)

opciones = ["Masculino", "Femenino", "Otro"]
generoCombo = ttk.Combobox(ventana,values=opciones,state="readonly")
generoCombo.set("Selecciona una opción")
generoCombo.grid(row=4,column=1,pady=20)


botonAgregar = tk.Button(ventana,text="Agregar")
botonAgregar.grid(row=5,column=0,columnspan=3,padx=10, pady=40)

botonContactos = tk.Button(ventana,text="Contactos")
botonContactos.grid(row=5,column=2,padx=10, pady=40)

def resetRed():
    nombreCajaTexto.configure(background="white")
    apellidoCajaTexto.configure(background="white") 
    telefonoCajaTexto.configure(background="white")
    generoEtiqueta.configure(background="white")



def AntesResetear():
    ResetearInterfaz(5)

def ResetearInterfaz(con):
    
    if con > 0:
        erroresEtiqueta.config(text=f"usuario agregado, reseteando en {con}")
        ventana.after(1000,ResetearInterfaz,con - 1)
    else:

        nombreCajaTexto.delete(0, tk.END)
        apellidoCajaTexto.delete(0, tk.END)
        telefonoCajaTexto.delete(0, tk.END)
        generoCombo.set("Selecciona una opción")  # Para el Combobox
        erroresEtiqueta.config(text=":)")

def ObtenerDatos():
    resetRed()
    nombre = nombreCajaTexto.get()
    apellidos = apellidoCajaTexto.get()
    telefono = telefonoCajaTexto.get()
    genero = generoCombo.get()
    print(nombre)
    if nombre == "" or apellidos == "" or telefono == "" or genero == "Selecciona una opción":
        erroresEtiqueta.config(text="Asegurate de llenar todos los campos")
        
        if nombre == "":
            nombreCajaTexto.configure(background="red")
        if apellidos == "":
            apellidoCajaTexto.configure(background="red")
        if telefono == "":
            telefonoCajaTexto.configure(background="red")
        if genero == "Selecciona una opción":
            generoEtiqueta.configure(background="red")
            
        return
    
    try:
        telefonoInt = int(telefono)
        if telefonoInt < 0 or len(str(telefono)) > 10:
            
            erroresEtiqueta.config(text="Solo números en teléfono y no más de 10")
            telefonoCajaTexto.configure(background="red")
            return
    except:
        erroresEtiqueta.config(text="Solo números en teléfono")
        
        telefonoCajaTexto.configure(background="red")
        return
    
    erroresEtiqueta.config(text=":)")
    personaNueva = persona_a_registrar(nombre,apellidos,telefono,genero)
    contactos.append(personaNueva)
    AntesResetear()

#Agregamos al usuario
botonAgregar.config(command=ObtenerDatos)

def MostrarContactos():
    contactosventana = tk.Toplevel()  # mejor usar Toplevel para subventanas
    contactosventana.title("Lista de contactos")
    contactosventana.geometry("400x400")
    ypos = 0

    for i in contactos:
        contactoStr = f"""
        ==========================
        {i.nombre} {i.apellido} | Tel: {i.telefono} | Género: {i.genero}
        ==========================
        """
        etiqueta = tk.Label(contactosventana, text=contactoStr, anchor="w", justify="left")
        etiqueta.grid(row=ypos, column=0, sticky="w", padx=10, pady=5)
        ypos += 1
    contactosventana.mainloop()
#boton mostrar contactos
botonContactos.config(command=MostrarContactos)
ventana.mainloop()