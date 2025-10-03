import json
def cambiarJson(alarma):
    
    if " " in alarma:
        hora, mensaje = alarma.split(" ", 1)
    else:
        hora, mensaje = alarma, ""

     # --- Paso 1: Leer alarmas originales ---
    with open("alarmas.json", "r", encoding="utf-8") as f:
        alarmasOriginales = json.load(f)

    #Buscar la alarma exacta
    lista=[] ##aqui se guardara la nueva lista sin la alarma que se paso al metodo
    
    for a in alarmasOriginales:
        if a["Hora"] == hora and a["Mensaje"] == mensaje:
            alarmaRecurrente = a
        else:
            lista.append(a)

    #Ahora hay que mover la alarma
    if alarmaRecurrente:
        try:
            with open("alarmasRecurrentes.json", "r", encoding="utf-8") as f:
                alarmas_recurrentes = json.load(f)
        except FileNotFoundError:
            alarmas_recurrentes = []

        alarmas_recurrentes.append(alarmaRecurrente)

    
        with open("alarmasRecurrentes.json", "w", encoding="utf-8") as f:
            json.dump(alarmas_recurrentes, f, indent=4, ensure_ascii=False)

 # --- Paso 3: Guardar lista original sin esa alarma ---
        with open("alarmas.json", "w", encoding="utf-8") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)

def EliminarAlarma(alarma):
    horaEliminar = alarma.split(" ", 1)[0]
    mensajeEliminar = alarma.split(" ", 1)[1] if " " in alarma else ""

    print(horaEliminar, "and", mensajeEliminar)
    with open("alarmasRecurrentes.json", "r", encoding="utf-8") as f:
            alarmas = json.load(f)
            nuevasAlarmas= []
            for a in alarmas:
                if not (a["Hora"] == horaEliminar and a["Mensaje"] == mensajeEliminar):
                    nuevasAlarmas.append(a)
                
    with open("alarmasRecurrentes.json" , "w", encoding="utf-8") as f:
            json.dump(nuevasAlarmas, f, indent=4, ensure_ascii=False)