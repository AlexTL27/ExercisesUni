import json
import os

def guardarAlarma(hora, mensaje, archivo = "alarmas.json"):
 
    nueva = {"Hora": hora, "Mensaje": mensaje}
    alarmas = []
    if hora == "":
         return
    
    
    if os.path.exists(archivo):
        if os.path.getsize(archivo) > 0:
            with open(archivo, "r", encoding="utf-8") as f:
             alarmas = json.load(f)
    else:
        alarmas = []

    alarmas.append(nueva)

    with open(archivo, "w", encoding="utf-8") as f:
        print("Modifique")
        json.dump(alarmas,f,indent=4,ensure_ascii=False)


