import json
from datetime import datetime

def cargarAlarmas(val):
        if val == 0:
              archivo = "alarmas.json"
        elif val == 1:
              archivo = "alarmasRecurrentes.json"
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    

#este script activa la alarma cuando llegue a hora

def esperar_y_activar(alarmas):
        alarmas_activadas = set()

       
        ahora = datetime.now().strftime("%H:%M")#la hora que muestre tu relog, se muestra en formato de 24 hrs
        mensaje = ""
        hora = ""
        for alarma in alarmas:
                hora = alarma["Hora"]
                mensaje = alarma["Mensaje"]
                


                if hora == ahora and hora not in alarmas_activadas:
                    print(f"Alarma ({hora}):{mensaje}")
                    alarmas_activadas.add(hora)
                    return True, hora, mensaje
            
               
        return False, ahora, mensaje
       
def iniciar(val):
     return esperar_y_activar(cargarAlarmas(val))



def eliminarAlarmas(alarmaEliminar):
        horaEliminar = alarmaEliminar.split(" ", 1)[0]
        mensajeEliminar = alarmaEliminar.split(" ", 1)[1] if " " in alarmaEliminar else ""

        print(horaEliminar, "and", mensajeEliminar)
        with open("alarmas.json", "r", encoding="utf-8") as f:
                alarmas = json.load(f)
                nuevasAlarmas= []
                for a in alarmas:
                    if not (a["Hora"] == horaEliminar and a["Mensaje"] == mensajeEliminar):
                        nuevasAlarmas.append(a)
                    
        with open("alarmas.json" , "w", encoding="utf-8") as f:
                json.dump(nuevasAlarmas, f, indent=4, ensure_ascii=False)

