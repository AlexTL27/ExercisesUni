import tkinter as tk
class Tareas():
    def __init__(self,Tarea):
        self.tarea = Tarea
        
    #se pulsa boton aceptar tarea
def CrearTarea(tarea):
        
        lineas = []
        ficheroPendiente = "tareaPendiente.txt"
        with open(ficheroPendiente,"r", encoding="utf-8") as f:
              lineas = f.readlines()

        lineas.insert(0,tarea.strip() + "\n")

        with open(ficheroPendiente, "w", encoding="utf-8") as f:
            f.writelines(lineas)
           
        

#MRegresa las tareas en forma de lista
def VerTareas():
        ficheroPendiente = "tareaPendiente.txt"
        
        
        with open(ficheroPendiente, "r", encoding="utf-8") as f:
               lineas = f.readlines()
              
        return lineas

#Recibe los valores que el usuario marco y los agrega a tarea terminada
def TareaTerminada(tareas):
        ficheroPendiente = "tareaPendiente.txt"
        ficheroTerminada = "tareaTerminada.txt"
        nuevasLineas = []


        print("tareaElminar: ", tareas.strip())
        nuevasLineas = []
        with open(ficheroPendiente, "r", encoding="utf-8") as f:
              lineas = f.readlines()
        
        for i in lineas:
              if i.strip() == tareas.strip():
                    
                    continue
              nuevasLineas.append(i)

        with open(ficheroPendiente, "w", encoding="utf-8") as f:
            for a in nuevasLineas:
                  
                  f.write(a)


        #Agregamos la tarea al fichero tarea terminada
        with open(ficheroTerminada, "a", encoding="utf-8") as f:
            f.write(tareas)


            
      
def VerTareasTerminadas():
        ficheroTerminada = "tareaTerminada.txt"
        
        
        with open(ficheroTerminada, "r", encoding="utf-8") as f:
               lineas = f.readlines()
              
        return lineas


def eliminarTareaTerminada(tareaEliminar):
        print("tareaElminar: ", tareaEliminar.strip())
        ficheroTerminada = "tareaTerminada.txt"
        nuevasLineas = []
        with open(ficheroTerminada, "r", encoding="utf-8") as f:
              lineas = f.readlines()
        
        for i in lineas:
              if i.strip() == tareaEliminar.strip():
                    print("Entre")
                    continue
              nuevasLineas.append(i)

        with open(ficheroTerminada, "w", encoding="utf-8") as f:
            for a in nuevasLineas:
                  
                  f.write(a)
            