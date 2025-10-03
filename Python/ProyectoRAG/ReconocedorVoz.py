from vosk import Model, KaldiRecognizer
import sounddevice as sd
import queue
import json
from datetime import datetime

"""
    vosk.Model: carga el modelo de reconocimiento de voz.

    KaldiRecognizer: hace el reconocimiento con ese modelo.

    sounddevice: permite escuchar el micrófono en tiempo real.

    queue: permite guardar audio mientras se procesa.

    json: para trabajar con el formato de texto que devuelve Vosk.
    
       


"""
def ReconocedorVoz(pantalla, ventana,microfonoImagen, framesMicro):
        

    ##Cargamos el modelo
    model = Model("vosk-model-small-es-0.42")


    ##Configuración básica del audio
    samplerate = 16000
    rec = KaldiRecognizer(model, samplerate)
    audioQueue = queue.Queue() #creamos una cola para el audio

    def callback(indata, frames, time, status):
        if status:
            print(status)
        audioQueue.put(bytes(indata))


    HoraDicha = ""
    #Escuchar la grabación en tiempo real

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype="int16", channels=1, callback=callback):
        print("Ahora estamos capturando tu audio...")
        
        while True:
            data = audioQueue.get()
            bandera = True
            #si vosk detecta que la frase esta correcta, devuekve true
            #ademas se guarda en rec lo que dije, y olvida lo anterior
            if rec.AcceptWaveform(data):
                resultado = json.loads(rec.Result())
                HoraDicha = resultado.get("text", "") 
                pantalla.config(text=resultado.get("text", ""))
                break

            else:
                partial = json.loads(rec.PartialResult())
                print("Parcial:", partial.get("partial", ""))
                pantalla.config(text=partial.get("partial", ""))
                
                microfonoImagen.config(image=framesMicro[2])
                
                """Por ahora no, falta un frame
                bandera = not bandera

                if bandera:
                    microfonoImagen.config(image=framesMicro[2])
                else:
                        
                    microfonoImagen.config(image=framesMicro[3])
                    """
                ventana.update_idletasks()  # <- Forzar que Tkinter actualice ya


    #####################################
    #Funcion, pasar texto a numeros(Horas)
    print("TextoReciensalido", HoraDicha)
    palabrasConvertidas = HoraDicha.split()
    minutos_a_numero = {
        "uno": 0, "una": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
        "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10,
        "once": 11, "doce": 12, "trece": 13, "catorce": 14, "quince": 15,
        "dieciséis": 16, "dieciseis": 16, "diecisiete": 17, "dieciocho": 18, "diecinueve": 19,
        "veinte": 20, "veintiuno": 21, "veintidós": 22, "veintidos": 22, "veintitrés": 23,
        "veintitres": 23, "veinticuatro": 24, "veinticinco": 25, "veintiséis": 26, "veintiseis": 26,
        "veintisiete": 27, "veintiocho": 28, "veintinueve": 29, "treinta": 30, "treinta y uno": 31,
        "treinta y dos": 32, "treinta y tres": 33, "treinta y cuatro": 34, "treinta y cinco": 35,
        "treinta y seis": 36, "treinta y siete": 37, "treinta y ocho": 38, "treinta y nueve": 39,
        "cuarenta": 40, "cuarenta y uno": 41, "cuarenta y dos": 42, "cuarenta y tres": 43,
        "cuarenta y cuatro": 44, "cuarenta y cinco": 45, "cuarenta y seis": 46, "cuarenta y siete": 47,
        "cuarenta y ocho": 48, "cuarenta y nueve": 49, "cincuenta": 50, "cincuenta y uno": 51,
        "cincuenta y dos": 52, "cincuenta y tres": 53, "cincuenta y cuatro": 54,
        "cincuenta y cinco": 55, "cincuenta y seis": 56, "cincuenta y siete": 57,
        "cincuenta y ocho": 58, "cincuenta y nueve": 59
    }

    palabras_a_numero = {
        "cero": 0, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
        "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
        "diez": 10, "once": 11, "doce": 12, "trece": 13, "catorce": 14,
        "quince": 15, "dieciseis": 16, "dieciséis": 16, "diecisiete": 17, "dieciocho": 18,
        "diecinueve": 19, "veinte": 20, "veintiuno": 21, "veintidós": 22,
        "veintitrés": 23, "cuarto": 15
        }
    print(palabrasConvertidas)#esta guarda lo dicho por usuario, pero en forma de array

    #limpiamos las palabras que no nos sirvan ejem: alarma para las dos y media, res: dos y media
    indice_Hora = -1

    for i in range(len(palabrasConvertidas)):
        
        palabra = palabrasConvertidas[i]

        if palabra in palabras_a_numero:      
            # Aceptamos "una" solo si viene después de "la"
            if palabra == "una":
                if i > 0 and palabrasConvertidas[i-1] == "la":
                        indice_Hora = i
                        break
                else:
                        continue
            # También ignoramos si viene después de "alarma", etc.
            if i + 1 < len(palabrasConvertidas) and palabrasConvertidas[i + 1] in ["alarma", "notificación", "alarmas", "notificaciones"]:
                continue

            indice_Hora = i
            break
        

    if indice_Hora != -1:
        palabrasConvertidas = palabrasConvertidas[indice_Hora:]
    else:
        palabrasConvertidas = []
        
                
    ##apartir de aqui, ya tengo el texto limpio, con solo la hora y el recordatorio



    ##aqui separo la hora dek recordatorio, siempre y cuando el usuario siga el orden:
    ##quiero una alarma + hora dicha + recordatorio

    horaFinalArray=[] ##hora final sera igual a la hora
    recordatorioFinalArray = []#guardara lo que sea que el usuario diga despues de hora


    #otra condicion
    if len(palabrasConvertidas) > 2 and (palabrasConvertidas[1] == "y" or palabrasConvertidas[2] == "punto"):
                horaFinalArray = palabrasConvertidas[0:3]
                recordatorioFinalArray = palabrasConvertidas[3:]
                
    elif len(palabrasConvertidas) > 1 and palabrasConvertidas[1] in minutos_a_numero:
                
                if len(palabrasConvertidas) > 2 and palabrasConvertidas[2] == "y" :
                    
                    if len(palabrasConvertidas) > 3 and palabrasConvertidas[3] in palabras_a_numero:
                            
                            horaFinalArray = palabrasConvertidas[0:4]
                            recordatorioFinalArray = palabrasConvertidas[4:]
                    else:           
                            horaFinalArray = palabrasConvertidas[0:2]
                            recordatorioFinalArray = palabrasConvertidas[2:]
                else:           
                    horaFinalArray = palabrasConvertidas[0:2]
                    recordatorioFinalArray = palabrasConvertidas[2:]
    elif len(palabrasConvertidas) > 0 and palabrasConvertidas[0] in palabras_a_numero:
                horaFinalArray = [palabrasConvertidas[0]]
                recordatorioFinalArray = palabrasConvertidas[1:]
        
    print("hora final recien salida:", horaFinalArray)

    horaFinal = " ".join(horaFinalArray)

    horaFinalNumeros = ""


    ##convierte ya la hora especificada por usuario
    for palabra, hora in palabras_a_numero.items():
        
        if f"{palabra} y media" == horaFinal:
            horaFinalNumeros = f"{hora:02d}:30"
            break
        elif f"{palabra} y cuarto" == horaFinal:
            horaFinalNumeros = f"{hora:02d}:15"
            break
        elif f"cuarto para las {palabra}" == horaFinal or f"cuarto para la {palabra}" == horaFinal:
                nueva_hora = hora - 1 if hora > 1 else 12
                horaFinalNumeros = f"{nueva_hora:02d}:45"
                break
        elif horaFinal == palabra or horaFinal == f"{palabra} en punto":
            horaFinalNumeros = f"{hora:02d}:00"
            break
        else:
            for minutosPalabra,minutos in minutos_a_numero.items():
                
                if f"{palabra} {minutosPalabra}" == horaFinal or f"{palabra} y {minutosPalabra}" == horaFinal or f"{palabra} con {minutosPalabra}" == horaFinal:
                    
                    if minutos < 10 and minutos > 0:
                        horaFinalNumeros = f"{hora:02d}:0{minutos}"
                        break
                    else:
                         horaFinalNumeros = f"{hora:02d}:{minutos}"
                         break
                         
    #ultimo cheque de horaFinalNumeros, si en recordatorio se incluye algo que referencie a la tarde se volvera en tarde la hora


    recordatorioFinal= " ".join(recordatorioFinalArray)
    if  horaFinalNumeros != "":

        ahora_str = datetime.now().strftime("%H:%M")
        ahora = datetime.strptime(ahora_str,"%H:%M")#la hora que muestre tu relog, se muestra en formato de 24 hrs
        #ahora = datetime.strptime("15:24", "%H:%M")
        hora1 = datetime.strptime(horaFinalNumeros, "%H:%M")
        palabrasActivadoras = ["tarde", "noche", "pm"]
        palabrasActivadorasDia = ["madrugada", "mañana", "am", "día"]
        
        if hora1.hour < 12:
              
                hora1_posible_pm = hora1.replace(hour=hora1.hour + 12)

                if len(recordatorioFinalArray) >= 1: 
                    if recordatorioFinalArray[0] == "p" and recordatorioFinalArray[1] == "m":
                        recordatorioFinalArray[1] = "pm"
                        recordatorioFinalArray = recordatorioFinalArray[1:]
                        recordatorioFinal= " ".join(recordatorioFinalArray)

                if any(p in recordatorioFinal for p in palabrasActivadorasDia):
                     
                    pass

                ##Se puede hacer la hora a pm
                   
                elif any(p in recordatorioFinal for p in palabrasActivadoras): 


                    print("(más tarde)")

                    horaFinalNumeros = (hora1.replace(hour=(hora1.hour + 12))).strftime("%H:%M")    
                
                    print(horaFinalNumeros)  # Resultado: 18:00

                elif ahora.hour < 13:
                     pass
                elif hora1_posible_pm > ahora:
                    # si la hora posible(Hora dicha mas 12) es mayor 
                    #QUE EL ahora, sumar 12
                    horaFinalNumeros = (hora1.replace(hour=hora1.hour + 12)).strftime("%H:%M")

     


        

              
        elif hora1.hour >= 12 and hora1.hour < 13:
               
                hora1_posible_pm = hora1.replace(hour=hora1.hour + 11)
                if any(p in recordatorioFinal for p in palabrasActivadorasDia):
                     
                    pass
               
                elif any(p in recordatorioFinal for p in palabrasActivadoras): 

                    horaFinalNumeros = "00" + horaFinalNumeros[2:]
                elif ahora.hour < 13:
                     pass
                elif hora1_posible_pm > ahora:
                    
                         horaFinalNumeros = "00" + horaFinalNumeros[2:]        
    else:
        #excede la hora, mayor a 12, las 13 pm no estaria bien, horaFInalNumeros se queda como estaba
        pass



    #limpiar el recordatorio final
    while recordatorioFinalArray and (recordatorioFinalArray[0] == "para" or recordatorioFinalArray[0] == "horas" or recordatorioFinalArray[0] == "a" or recordatorioFinalArray[0] == "de" or recordatorioFinalArray[0] == "la" or  recordatorioFinalArray[0] == "mañana" or recordatorioFinalArray[0] == "madrugada" or recordatorioFinalArray[0] == "tarde" or recordatorioFinalArray[0] == "noche" or recordatorioFinalArray[0] == "p" or recordatorioFinalArray[0] == "m"or recordatorioFinalArray[0] == "am" or recordatorioFinalArray[0] == "pm"):
        recordatorioFinalArray = recordatorioFinalArray[1:]


    #de aqui para abajo tenemos la hora escrita y en numeros, y el recordatorio en array. 
    print(horaFinalNumeros)



    recordatorioFinal= " ".join(recordatorioFinalArray)
    print("recordatorio final: ", recordatorioFinal)

    if recordatorioFinal == "" and horaFinalNumeros == "":
            pantalla.config(text="No entendi lo que dijiste, Prueba nuevamente.")
    
    
    return horaFinalNumeros, recordatorioFinal

#errores
