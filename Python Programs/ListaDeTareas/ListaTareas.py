import tkinter as tk
import os as os
import backend

mainVentana = tk.Tk()
mainVentana.configure(background="Black")

tk.Label(mainVentana,text="Lista de tareas",font=("Arial",20),bg="Black",fg="white",padx=80,pady=20).grid(row=0,column=0, columnspan=3)


tk.Label(mainVentana,text="Tarea: ",font=("Arial",15),bg="Black",fg="white",padx=10,pady=20).grid(row=1,column=0, columnspan=1)

cajaTextoTarea = tk.Entry(background="Black",fg="White")
cajaTextoTarea.grid(row=1,column=1, columnspan=3)

botonAceptarTarea = tk.Button(text="Agregar tarea",font=("Arial",15),bg="Black",fg="white")
botonAceptarTarea.grid(row=2,column=0,pady=20,columnspan=3)


#Radio buttons
opcion = tk.StringVar() #opcion que sera seleccionada
opcion.set("1")

botonTareaPendiente = tk.Radiobutton(mainVentana,text="Tareas pedientes",font=("Arial",15),bg="Black",fg="white",padx=20,pady=20,variable=opcion,value="1")
botonTareaPendiente.grid(row=3,column=0,columnspan=1)


botonTareaTerminada = tk.Radiobutton(mainVentana,text="Tareas Terminadas",font=("Arial",15),bg="Black",fg="white",padx=20,pady=20,variable=opcion,value="2")
botonTareaTerminada.grid(row=3,column=1)


checkboxvars = []
frame = None
#tareas pendientes
def VerTareas():
    global checkboxvars, frame, frameTermindas

    if frame is not None:
        frame.destroy()
    if frameTermindas is not None:
        frameTermindas.destroy()
    frame = tk.Frame(mainVentana,bg="black")
    frame.grid(row=4,column=0,columnspan=2,padx=60,pady=10, rowspan=1)
    

    canvas = tk.Canvas(frame, bg="black", height=200, highlightthickness=0)

    #Crear scrollbar
    scrollbar = tk.Scrollbar(frame,orient="vertical",command=canvas.yview)
    

    #No se puede meter widgets directamente al Canvas fácilmente, 
    # así que se usa este frame dentro.
    innerFrame = tk.Frame(canvas,bg="black")
    
    innerFrame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0,0),window=innerFrame,anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="left", fill="y")
    canvas.pack(side="left", fill="both",expand=True)
  
    textoTareas = backend.VerTareas()
    checkboxvars = []
    for i in textoTareas:
        var = tk.IntVar()
        pintar = tk.Checkbutton(innerFrame,text=i,bg="gray",variable=var,anchor="w")
        pintar.pack(anchor="w")
        checkboxvars.append((i, var))
    btnRevisar = tk.Button(mainVentana, text="Marcar como terminadas", command=RevisarTareasMarcadas, bg="black", fg="white")
    btnRevisar.grid(row=7, column=0, pady=10)


def RevisarTareasMarcadas():  
    global checkboxvars      
    for text, var in checkboxvars:
        if var.get() == 1:
            print("Tarea Marcada: ", text)
            backend.TareaTerminada(text)
            VerTareas()
           

#tareas terminadas
checkboxvarsTerminadas = []
frameTermindas = None
def VerTareasTerminadas():
    global checkboxvarsTerminadas,frame
    if frame is not None:
        frame.destroy()


    frame = tk.Frame(mainVentana,bg="black")
    frame.grid(row=4,column=1,columnspan=2,padx=60,pady=10, rowspan=1)
    

    canvas = tk.Canvas(frame, bg="black", height=200, highlightthickness=0)

    #Crear scrollbar
    scrollbar = tk.Scrollbar(frame,orient="vertical",command=canvas.yview)
    

    #No se puede meter widgets directamente al Canvas fácilmente, 
    # así que se usa este frame dentro.
    innerFrame = tk.Frame(canvas,bg="black")
    
    innerFrame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    
    canvas.create_window((0,0),window=innerFrame,anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="left", fill="y")
    canvas.pack(side="left", fill="both",expand=True)
  

    textoTareas = backend.VerTareasTerminadas()
    checkboxvarsTerminadas = []
    
    
    for i in textoTareas:
        var = tk.IntVar()
        pintar = tk.Checkbutton(innerFrame,text=i,bg="gray",variable=var,anchor="w")
        pintar.pack(anchor="w")
        checkboxvarsTerminadas.append((i, var))
    btnRevisar = tk.Button(mainVentana, text="Eliminar Tarea", command=EliminarTareasMarcadas, bg="black", fg="white")
    btnRevisar.grid(row=7, column=1,pady=10)

def EliminarTareasMarcadas():  
    global checkboxvarsTerminadas
    for text, var in checkboxvarsTerminadas:
        if var.get() == 1:
            
            print("Tarea Marcada: ", text)
            backend.eliminarTareaTerminada(text)
            VerTareasTerminadas()

            


def tareaCadenaTextoNoNull():  
    if cajaTextoTarea.get() == "":
        cajaTextoTarea.config(bg="red")
    else:
        backend.CrearTarea(cajaTextoTarea.get())
        cajaTextoTarea.config(bg="black")
        cajaTextoTarea.delete(0,tk.END)
        VerTareas()


botonTareaTerminada.configure(command=VerTareasTerminadas)
botonTareaPendiente.configure(command=VerTareas)
botonAceptarTarea.configure(command=tareaCadenaTextoNoNull)
mainVentana.mainloop()