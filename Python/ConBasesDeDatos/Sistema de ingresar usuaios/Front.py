import tkinter as tk
import datetime 
from tkinter import ttk
import back
from tkinter import messagebox;
from tkinter import filedialog
from PIL import Image, ImageTk #pil para Trabajar con imagenes
from io import BytesIO
from tkinter import messagebox


ventana = tk.Tk()
ventana.geometry("1120x600")
ventana.title("Registro de alumnos")
miImagen = None




def SeleccionarImagen():
    global miImagen

    miImagen = filedialog.askopenfilename(initialdir="/", title="Buscar Imagen",
                                          filetypes=(("Archivos de imagen", "*.jpg *.jpeg *.png *.gif"),("Todos los archivos","*.*")))
    if not miImagen:
        return  # Canceló

    if miImagen:
        try:
            imagen = Image.open(miImagen)
            imagen = imagen.resize((200, 100))  # O el tamaño exacto que quieras

            nvaImagen = ImageTk.PhotoImage(imagen)
            imagenLabel.config(image=nvaImagen)
            imagenLabel.image=nvaImagen
            botonImagen.configure(state="disabled")
            
           
        except Exception as err:
            messagebox.showinfo(f"Error al cargar la imagen {err}")
      

# Usar grid para todo
tk.Label(ventana, text="Registro de alumnos", font="Arial 12",width=20).grid(row=0, column=1, columnspan=2, pady=20)
fecha_actual = datetime.date.today()
tk.Label(ventana, text=(f"Fecha:{fecha_actual.strftime("%d/%m/%Y")}"), font="Arial 12",anchor="w").grid(row=0, column=4, padx=10, pady=10,sticky="w")


tk.Label(ventana, text="Mátricula:", font="Arial 15",anchor="w",width=20).grid(row=1, column=0, padx=10, pady=10)
matricula = tk.Entry()
matricula.grid(row=1, column=1)


#BOton para guardar imagen
botonImagen = tk.Button(ventana, text="Seleccionar imagen",width=40,command=SeleccionarImagen)
botonImagen.grid(row=1, column=3, columnspan=2)


frameImagen= tk.Frame(ventana, bg="black",width=200, height=100)
frameImagen.grid(row=2, column=3, pady=10,columnspan=2)

frameImagen.grid_propagate(False)


imagenLabel = tk.Label(frameImagen,text="Imagen a cargar aquí", bg="gray",width=200, heigh=100)
imagenLabel.grid()



#others labels

tk.Label(ventana, text="Nombre:", font="Arial 15",anchor="w",width=20).grid(row=2, column=0, padx=10, pady=10)
nombre = tk.Entry()
nombre.grid(row=2, column=1)

tk.Label(ventana, text="Apellidos:", font="Arial 15",anchor="w",width=20).grid(row=3, column=0, padx=10, pady=10) 
apellidos = tk.Entry()
apellidos.grid(row=3, column=1)

tk.Label(ventana, text="Fecha de nacimiento (aaaa/mm/dd):", font="Arial 15",anchor="w",width=30).grid(row=4, column=0, padx=10, pady=10) 
nac = tk.Entry()
nac.grid(row=4, column=1)


genLabel = tk.Label(ventana, text="Género:", font="Arial 15",anchor="w",width=20)
genLabel.grid(row=4, column=3, padx=10, pady=10) 

opciones = ["Masculino", "Femenino", "Otro"]
generoCombo = ttk.Combobox(ventana,values=opciones,state="readonly")
generoCombo.set("Selecciona una opción")
generoCombo.grid(row=4,column=4,pady=20)

opcionesD = ["Ciencias económicas administrativas", "Ciencias naturales e ingenieria", "Tecnologías de la información", "Ciencias exactas", "Ciencias de la salud"]
dirLabel = tk.Label(ventana, text="Dirección:", font="Arial 15",anchor="w",width=20)
dirLabel.grid(row=5, column=0, padx=10, pady=10) 
dirCombo = ttk.Combobox(ventana,values=opcionesD,state="readonly",width=30)
dirCombo.set("Selecciona una opción")
dirCombo.grid(row=5, column=1)

carLabel = tk.Label(ventana, text="Carrera:", font="Arial 15",anchor="w",width=20)
carLabel.grid(row=5, column=3, padx=10, pady=10) 
#Carreras posibles dependiendo de la direccion
opcionesCienciasEconomicas = ["Maestría en innovación y negocios","Licenciatura en administración", "Licenciatura en contaduria", "Licenciatura en negocios y mercadotecnia"]
opcionesCienciasNaturales = ["Gestión ambiental","Ingenieria en manejo de recursos","Mantenimiento industrial","Ingenieria civil"]
opcionesTI = ["Desarrollo de software multiplataforma", "Redes digitales","Mecatrónica"]
opcionesCienciasExactas = ["Ingenieria mecánica", "Ingenieria industrial","Diseño textil y moda"]
opcionesCienciasSalud = ["Terapia física","Enfermeria","Médico cirujano"]
opcionFinal = [""]

carrerasCombo = ttk.Combobox(ventana,values=opcionFinal,state="readonly",width=30)
carrerasCombo.set("Selecciona antes una dirección")
carrerasCombo.grid(row=5,column=4,pady=20)

def AgregarCarreraCorrespondiente():
    if dirCombo.get() == "Ciencias económicas administrativas":
        carrerasCombo.configure(values=opcionesCienciasEconomicas)
    if dirCombo.get() == "Ciencias naturales e ingenieria":
        carrerasCombo.configure(values=opcionesCienciasNaturales)
    if dirCombo.get() == "Tecnologías de la información":
        carrerasCombo.configure(values=opcionesTI)
    if dirCombo.get() == "Ciencias exactas":
        carrerasCombo.configure(values=opcionesCienciasExactas)
    if dirCombo.get() == "Ciencias de la salud":
        carrerasCombo.configure(values=opcionesCienciasSalud)
    
dirCombo.bind("<<ComboboxSelected>>", lambda e: AgregarCarreraCorrespondiente()) #Dependiendo la opcion que se seleccione


ingresarAlumno = tk.Button(ventana, text="Ingresar",font="Arial 15",anchor="w",width=20,bg="green",fg="white")
ingresarAlumno.grid(row=6, column=0,columnspan=2, padx=10, pady=10) 

errores = tk.Label(ventana, text="Ingresa tus datos",font="Arial 15",anchor="w",width=35,bg="gray")
errores.grid(row=6, column=2,columnspan=2, padx=10, pady=10) 

tk.Label(ventana, text="Alumnos registrados:", font="Arial 15",anchor="w",width=20).grid(row=7, column=1,columnspan=2, padx=10, pady=10) 


#scroll con canvas para alumnos + boton
alumnosFrame = tk.Frame(ventana)
alumnosFrame.grid(row=8,column=0,columnspan=8,padx=10,pady=10)

canvas = tk.Canvas(alumnosFrame, width=1200, height=100)
scrollbar = tk.Scrollbar(alumnosFrame, orient="vertical",command=canvas.yview)
scrollableFrame = tk.Frame(canvas)

scrollableFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(
    scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0,0), window=scrollableFrame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left",fill="both",expand=True)
scrollbar.pack(side="right", fill="y")

def vaciarEntradas():
    global miImagen
    matricula.configure(state="normal")
    matricula.delete(0, tk.END)
    nombre.delete(0, tk.END)
    apellidos.delete(0,tk.END)
    nac.delete(0, tk.END)
    generoCombo.set("Selecciona una opción")
    dirCombo.set("Selecciona una opción")
    carrerasCombo.set("Selecciona antes una dirección")
    

    #LIMPIAMOS LAS ENTRADAS

    #se resetea ruta
    miImagen = None
    #se resetea label
    imagenLabel.config(image=None)
    
    try:
        del imagenLabel.image
    except:
        pass

    botonImagen.configure(state="normal")
    PintarBlanco()
    dejarDeEditar.configure(state="disabled")
    
   

#funcion para eliminar alumnos
def EliminarAlumno(matricula):
    confirmado = messagebox.askyesno("Confirmar eliminación", f"¿Deseas eliminar al alumno con matrícula {matricula}?")
    if confirmado:
        back.EliminarAlumno(matricula)
        errores.config(text=f"Alumno {matricula}, eliminado.")
        mostrarAlumnos()

def cancelarEdicion(boton):
    vaciarEntradas()
    matricula.configure(state="normal")
    errores.configure(text="Edición cancelada")
    dejarDeEditar.configure(state="disabled")

 #boton dejar de editar
dejarDeEditar = tk.Button(ventana,text="Cancelar Edición", command=lambda: cancelarEdicion(dejarDeEditar), state="disabled")
dejarDeEditar.grid(row=6,column=4)
    
def editarAlumno(valores):
    
    global miImagen
    vaciarEntradas()


    
    #boton dejar de editar
    dejarDeEditar.configure(state="active")
   
    
    errores.configure(text=f"Editando a matrícula: {valores[0]}")
    matricula.insert(0,valores[0])
    matricula.configure(state="readonly")
    nombre.insert(0,valores[1])
    apellidos.insert(0,valores[2])
    # Convertir la fecha de '2006-11-27' a '2006/11/27'
    fecha_formateada = valores[3].strftime("%Y/%m/%d")
    nac.insert(0, fecha_formateada)
   
    generoCombo.set(valores[4])
    dirCombo.set(valores[5])
    carrerasCombo.set(valores[6])
   #hacer consukta a BD para conocer la img guardada
    miImagen = back.ConocerIMG(matricula.get())

    imagen = Image.open(BytesIO(miImagen))
    imagen = imagen.resize((200, 100))
    nvaImagen = ImageTk.PhotoImage(imagen)
    imagenLabel.config(image=nvaImagen)
    imagenLabel.image=nvaImagen


############################################
#Se crea una nueva ventana
############################################
def subirCalificaciones(alumno):
    calfVentana = tk.Toplevel()
    opcionFinal = ["10","9","8","7","6","5","4","3","2","1","0"]

    materias = [
        ("Base de Datos"),
        ("Pensamiento y Toma de Decisiones"),
        ("Inglés 3"),
        ("Programación Orientada a Objetos"),
        ("Proyecto Integrador"),
        ("Tópicos de Calidad")
    ]

    tk.Label(calfVentana,text=f"Alumno:{alumno[1]} {alumno[2]}").grid(row=0,column=0, sticky="w")
    tk.Label(calfVentana,text=f"Matrícula:{alumno[0]}").grid(row=1,column=0,sticky="w")

    tk.Label(calfVentana,text="Materia").grid(row=2,column=0)
    tk.Label(calfVentana,text="Calificación").grid(row=2,column=1)

    #######Materias

    comboboxes = []
    con = 1
    for i, nombre in enumerate(materias, start=3):
        
        tk.Label(calfVentana,text=f"{nombre}:").grid(row=i,column=0,sticky="w")

        combo = ttk.Combobox(calfVentana,values=opcionFinal,state="readonly")
        combo.set(back.conocerCalf(alumno[0], con))
        combo.grid(row=i,column=1)

        comboboxes.append(combo)
        con += 1
    # Pasamos las comboboxes y el alumno al botón
    subirCalf = tk.Button(
        calfVentana,
        text="Subir",
        bg="green",
        fg="white",
        width=20,
        command=lambda: subirCalfBD(alumno[0], comboboxes, calfVentana)
    )
    subirCalf.grid(row=len(materias)+3,column=0,columnspan=2,pady=20)

def subirCalfBD(matricula, combo, calfVentana):
    calf = [i.get() for i in combo]

    for a in calf:
        if a == "No Registrada":
            return
   
    back.calfBD(matricula,calf)

    
    calfVentana.destroy()
    messagebox.showinfo(f"Datos Actualizados con exito")


###########################################^^^^^

    
def mostrarAlumnos():
    datos = back.MostrarDatos()
    
    # Limpiar contenido anterior
    for widget in scrollableFrame.winfo_children():
        widget.destroy()

    for alumno in datos:
        alumnosTexto = f"{alumno[0]} | {alumno[1]} {alumno[2]} | {alumno[3]} | {alumno[4]} | {alumno[5]} | {alumno[6]}"
        fila = tk.Frame(scrollableFrame,bg="lightgray")
        fila.pack(fill="x", pady=2)

        label = tk.Label(fila, text=alumnosTexto, anchor="w", width=100, bg="lightgray", font=("Arial", 12))
        label.pack(side="left", padx=5)

        btnExportar = tk.Button(fila, text="Exportar", command=lambda a=alumno: ExportarAlumno(a),bg="orange",fg="white")
        btnExportar.pack(side="right", padx=5)

        boton = tk.Button(fila, text="Calf",  command=lambda a=alumno: subirCalificaciones(a),bg="green",fg="white")
        boton.pack(side="right", padx=5)

        boton = tk.Button(fila, text="Editar",  command=lambda a=alumno: editarAlumno(a),bg="blue",fg="white")
        boton.pack(side="right", padx=5)

        btnEliminar = tk.Button(fila, text="Eliminar", command=lambda a=alumno: EliminarAlumno(a[0]),bg="red",fg="white")
        btnEliminar.pack(side="right", padx=5)


def ExportarAlumno(alumno):
    back.exportarAlumno(alumno)

mostrarAlumnos()
bandera = False


def PintarBlanco():
    matricula.configure(bg="white")
    nombre.configure(bg="white")
    apellidos.configure(bg="white")
    nac.configure(bg="white")
    genLabel.configure(bg="white")
    dirLabel.configure(bg="white")
    carLabel.configure(bg="white")
    errores.configure(bg="gray")
    

def PintarRojo(val):
    global bandera

    bandera = True
    val.configure(bg="red")
    errores.configure(bg="red")




def ObtenerDatosAlumno():
    global bandera
    PintarBlanco()
    matriculaText = matricula.get().strip()
    nombreText = nombre.get().strip()
    apellidosText = apellidos.get().strip()
    nacText = nac.get().strip()
    generoText = generoCombo.get().strip()
    direccionText = dirCombo.get().strip()
    carreraText = carrerasCombo.get().strip()

  

    bandera = False

    if not matriculaText:
        PintarRojo(matricula)
    if not nombreText:
        PintarRojo(nombre)
    if not apellidosText:
        PintarRojo(apellidos)
    if not nacText:
        PintarRojo(nac)
    if generoText == "Selecciona una opción":
        PintarRojo(genLabel)
    if direccionText == "Selecciona una opción":
        PintarRojo(dirLabel)
    if carreraText == "Selecciona una opción":
        PintarRojo(carLabel)
    if miImagen == None:
        messagebox.showerror("asigna una imagen")
        bandera = True
        errores.configure(bg="red")
    
    if bandera:
        errores.configure(text="Campos incompletos")
        return
    
    try:
        matriculaNum = int(matriculaText)
    except:
        errores.configure(text="Solo números en matrícula")
        PintarRojo(matricula)
        return


    try:
        fechaNac = datetime.datetime.strptime(nacText, "%Y/%m/%d")
    except:
        errores.configure(text="Fecha inválida. Use el formato aaaa/mm/dd.")
        PintarRojo(nac)
        return
    
    #imagen
    try:

        with open(miImagen, "rb") as file:
                imagenBytes = file.read()
    except:
                imagenBytes = miImagen


    if back.ExisteMatricula(matriculaNum):
        print("Debo borrarte")
        confirmado = messagebox.askyesno("Confirmar", f"¿Deseas editar al alumno con matrícula {matriculaNum}?")
        if confirmado:
            back.EliminarAlumno(matriculaNum)
            errores.config(text=f"Alumno {matriculaNum}, editado.")
            
    back.alumnos(matriculaNum,nombreText,apellidosText,fechaNac,generoText,direccionText,carreraText,imagenBytes)

    errores.config(text="Registrado con exito") 
    mostrarAlumnos()
    vaciarEntradas()



ingresarAlumno.config(command=ObtenerDatosAlumno)
ventana.mainloop()