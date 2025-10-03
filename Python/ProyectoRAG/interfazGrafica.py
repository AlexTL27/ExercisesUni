import tkinter as tk
from PIL import Image, ImageTk
import ReconocedorVoz as rag
import AgregarAlarmaJson as alarmaJson
import EstablecerAlarma 
import threading
import json
import cambiarAlarmaDeJson
import pyttsx3
import pygame
import documentos
import sys
import os



def ruta_recurso(rel_path):
    """Devuelve la ruta absoluta al recurso, compatible con PyInstaller."""
    try:
        base_path = sys._MEIPASS  # carpeta temporal cuando está compilado
    except Exception:
        base_path = os.path.abspath(".")  # carpeta actual en desarrollo
    return os.path.join(base_path, rel_path)


def ruta_datos(rel_path):
    if getattr(sys, 'frozen', False):
        return os.path.join(os.path.dirname(sys.executable), rel_path)
    return os.path.join(os.path.abspath("."), rel_path)


class interfaz_de_alarma:
    def __init__(self, ventana):
        # la interfaz principal: configuro la ventana,
        #  modo oscuro por defecto y creo los contenedores y botones.
        pygame.mixer.init()
        self.ventana = ventana
        self.banderaRecurrentes = True
        self.contadorRecurrentes = 0
        self.ventana.title("RAG")
        self.ventana.geometry("600x550")
        self.ventana.configure(bg="#1C2E33")
        self.ventana.attributes("-alpha", 100)
        self.alarmaVentana = None


        self.animando = False
        self.imagen_index = 0
        self.menu_visible = False
        self.tema_oscuro = True

        self.contenedor = tk.Frame(self.ventana, bg="#1C2E33")
        self.contenedor.pack(fill="both", expand=True)

        self.boton_menu = tk.Button(
            self.ventana, text="≡", font=("Arial", 12, "bold"),
            bg="#1c1c1c", fg="white", bd=0,
            activebackground="#2a2a2a", command=self.toggle_menu
        )
        self.boton_menu.place(x=10, y=10)
        self.boton_menu.lift()

        self.crear_menu_lateral()
        self.contenido_principal()

        self.InicializadorMicro = True
        

        self.leerAlarmasJson()
        self.leerAlarmasRecurrentesJson()

        self.verificarAlarma()
        self.verificarAlarmaRecurrentes()
        
       
    
    def hablarEnVozAlta(self, texto):
        print("jol")
        def hablar():
            try:
                engine = pyttsx3.init()
                engine.setProperty("rate", 140)

                # (opcional) seleccionar voz en español si está disponible
                for voice in engine.getProperty('voices'):
                    if "spanish" in voice.name.lower():
                        engine.setProperty('voice', voice.id)
                        break

                engine.say(texto)
                engine.runAndWait()
                print("TERMINO")
            except:
                 print("reconocedor en curso")
        threading.Thread(target=hablar, daemon=True).start()

    def detenerSonidoYVentana(self):
        try:
           pygame.mixer.music.stop()
        except:
         pass
        if self.alarmaVentana:
         self.alarmaVentana.destroy()



    def verificarAlarma(self):
        print("Verificando alarmas...")

        con, hora, mensaje =  EstablecerAlarma.iniciar(0)
        if con:
            print("Alarma Activada: ", hora, "Mensaje: ", mensaje)
            self.eliminarAlarma(hora)
           
            ##Agregar ventana nueva que muestra la alarma, hora es el valor de la alarma
            ##############################################################################################################
            if self.alarmaVentana is None or not self.alarmaVentana.winfo_exists():
                    self.alarmaVentana = tk.Toplevel(self.ventana)
                    self.alarmaVentana.geometry("500x300")
                    self.alarmaVentana.title((hora, "", mensaje))
                    self.alarmaVentana.configure(background="black")
                    pygame.mixer.music.load(ruta_recurso("sound.mp3"))
                    pygame.mixer.music.play(loops=-1)  # -1 indica que se repite infinitamente

                    tk.Label(self.alarmaVentana, text=hora, font=("arial", 20)).pack(expand=True)
                    tk.Label(self.alarmaVentana, text=mensaje, font=("arial", 20), wraplength=400).pack(expand=True)

                    tk.Button(self.alarmaVentana, text="Detener Alarma", bg="red", font=("arial", 20),
          command=self.detenerSonidoYVentana).pack(expand=True)

                    self.alarmaVentana.grab_set()  # <- Esto reemplaza el mainloop()
            ##########################################################################################################################
    

           
        self.ventana.after(30000,self.verificarAlarma)

    
    def verificarAlarmaRecurrentes(self):
            
            
            if self.banderaRecurrentes:
                print("Verificando alarmas recurrentes...", self.contadorRecurrentes)

                con, hora, mensaje =  EstablecerAlarma.iniciar(1)
                if con:
                    self.banderaRecurrentes = False
                    
                    print("Alarma Activada: ", hora, "Mensaje: ", mensaje)
                
                    ##Agregar ventana nueva que muestra la alarma, hora es el valor de la alarma        Recurrentes
                    ##############################################################################################################
                    if self.alarmaVentana is None or not self.alarmaVentana.winfo_exists():
                        self.alarmaVentana = tk.Toplevel(self.ventana)
                        self.alarmaVentana.geometry("500x300")
                        self.alarmaVentana.title((hora, "", mensaje))
                        self.alarmaVentana.configure(background="black")
                        pygame.mixer.music.load(ruta_recurso("sound.mp3"))
                        pygame.mixer.music.play(loops=-1)  # -1 indica que se repite infinitamente

                        tk.Label(self.alarmaVentana, text=hora, font=("arial", 20)).pack(expand=True)
                        tk.Label(self.alarmaVentana, text=mensaje, font=("arial", 20), wraplength=400).pack(expand=True)

                        tk.Button(self.alarmaVentana, text="Detener Alarma", bg="red", font=("arial", 20),
                          command=self.detenerSonidoYVentana).pack(expand=True)

                        self.alarmaVentana.grab_set()  # <- Esto reemplaza el mainloop()
                    ##########################################################################################################################
            else:
                     self.contadorRecurrentes += 1

                     if self.contadorRecurrentes > 1:
                          self.contadorRecurrentes = 0
                          self.banderaRecurrentes = True
                          

            
            self.ventana.after(20000,self.verificarAlarmaRecurrentes)

###################################################################################
#Ingresar las alarmas a las listas
    def leerAlarmasJson(self):
            self.lista.delete(0,tk.END)
            with open(ruta_datos("alarmas.json"), "r", encoding="utf-8") as archivo:
        
                alarmas = json.load(archivo)

                ##Orden de agregadas
                for a in alarmas:
                    self.agregar_alarma(a["Hora"],a["Mensaje"])
  
    def leerAlarmasRecurrentesJson(self):
            self.listaRecurrentes.delete(0,tk.END)
            with open(ruta_datos("alarmasRecurrentes.json"), "r", encoding="utf-8") as archivo:
        
                alarmas = json.load(archivo)

                ##Orden de agregadas
                for a in alarmas:
                    self.listaRecurrentes.insert(tk.END, f"{a['Hora']} {a['Mensaje']}")
    

###################################################################################
        
    
    def eliminarAlarma(self, alarmaEliminar):
         with open("alarmas.json", "r", encoding="utf-8") as f:
                alarmas = json.load(f)
                nuevasAlarmas= []
                for a in alarmas:
                    if not a["Hora"] == alarmaEliminar:
                        nuevasAlarmas.append(a)

         with open("alarmas.json" , "w", encoding="utf-8") as f:
                json.dump(nuevasAlarmas, f, indent=4, ensure_ascii=False)
         self.leerAlarmasJson()

   
    def crear_menu_lateral(self):
        # menú lateral con botones para agregar, editar y eliminar alarmas.
        self.panel_menu = tk.Frame(self.contenedor, bg="#1e1e1e", width=140)

        tk.Button(self.panel_menu, text="ℹ️ Acerca de la APP", bg="#1e1e1e", fg="white",
                  activebackground="#2a2a2a", font=("Arial", 10), bd=0,
                  anchor="w", command=documentos.abrir_pdf).pack(fill="x", pady=(30, 5), padx=10)

        tk.Button(self.panel_menu, text="🗒️ Importante", bg="#1e1e1e", fg="white",
                  activebackground="#2a2a2a", font=("Arial", 10), bd=0,
                  anchor="w", command=documentos.abrir_readme).pack(fill="x", pady=5, padx=10)

    def toggle_menu(self):
        # Este método me permite mostrar u ocultar el panel lateral.
        if self.menu_visible:
            self.panel_menu.pack_forget()
            self.menu_visible = False
        else:
            self.panel_menu.pack(side="left", fill="y")
            self.menu_visible = True

    def contenido_principal(self):
        # construyo el área principal: la pantalla de estado del micrófono
        # y la lista donde se muestran las alarmas.
        self.zona = tk.Frame(self.contenedor, bg="#1C2E33")
        self.zona.pack(side="right", fill="both", expand=True)

        self.pantalla = tk.Label(self.zona, text="Micrófono inactivo", bg="#1C2E33", fg="#FFFFFF",
                                 font=("Courier", 11), anchor="nw", justify="left",
                                 width=45, height=7, bd=2, relief="ridge")
        self.pantalla.pack(pady=(50, 5))

        self.microfono()

        #contenedor para los dos labels de alarmas
        self.contenedorLabels = tk.Frame(self.zona, bg="#1C2E33")
        self.contenedorLabels.pack(pady=(10, 0))

        self.label_alarmas = tk.Label(self.contenedorLabels, text="🕒 Mis Alarmas:",
                                      fg="white", bg="#1C2E33",
                                      font=("Arial", 10, "bold"))
        self.label_alarmas.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")

        self.label_alarmasRecurrentes = tk.Label(self.contenedorLabels, text="🕒 Alarmas recurrentes:",
                                      fg="white", bg="#1C2E33",
                                      font=("Arial", 10, "bold"))
        self.label_alarmasRecurrentes.grid(row=0, column=1, padx=20, pady=(10, 0), sticky="w")


        # --- Contenedor horizontal para listas ---    
        self.lista = tk.Listbox(self.contenedorLabels, width=30, height=7, bg="#1e1e1e", fg="#00FFAA",
                                selectbackground="#00FFAA", selectforeground="black")
        self.lista.grid(row=1, column=0, padx=20, pady=(5, 0))


                # Lista de "Alarmas recurrentes"
        self.listaRecurrentes = tk.Listbox(self.contenedorLabels, width=30, height=7, bg="#1e1e1e", fg="#FFD700",
                                        selectbackground="#FFD700", selectforeground="black")
        self.listaRecurrentes.grid(row=1, column=1, padx=20, pady=(5, 0))


        self.lista.bind("<<ListboxSelect>>", self.alarmaSeleccionada)
        self.listaRecurrentes.bind("<<ListboxSelect>>", self.alarmaSeleccionada)
        self.lista.insert(tk.END, )
        self.lista.insert(tk.END, )

    def microfono(self):      
        
        #  imágenes del micrófono y las asigno al botón para la animación.
        self.imagenes = [
           ImageTk.PhotoImage(Image.open(ruta_recurso("imagenes/micro1.png")).resize((50, 50))),
           ImageTk.PhotoImage(Image.open(ruta_recurso("imagenes/micro2.png")).resize((50, 50))),
           ImageTk.PhotoImage(Image.open(ruta_recurso("imagenes/micro3.png")).resize((50, 50)))
        ]

        self.boton_microfono = tk.Button(self.zona, image=self.imagenes[0],
                                         bg="#1c1c1c", bd=0, activebackground="#2a2a2a",
                                         command=self.toggle_animacion)
        self.boton_microfono.pack(pady=(0, 10))

    ################################################################################################
    def AlarmaRecurrente(self, seleccion):
        #Pasar la alarma del json alarmas a json alarmasrecurrentes

        cambiarAlarmaDeJson.cambiarJson(alarma = self.lista.get(seleccion[0]))#cambia la alarma de json

        self.botonAlarmaRecurrente.destroy()
        self.botonEliminarAlarma.destroy()
        self.pantalla.config(text=f"Se estableció como recurrente: {self.lista.get(seleccion[0])}")
        self.hablarEnVozAlta(f"Se estableció como recurrente: {self.lista.get(seleccion[0])}")

        self.leerAlarmasJson()               # 🔄 Refresca la lista de alarmas normales
        self.leerAlarmasRecurrentesJson()    # 🔄 Refresca la lista de recurrentes
        
    def SeleccionMet(self, seleccion):
            self.botonAlarmaRecurrente.destroy()
            self.botonEliminarAlarma.destroy()
            alarma = self.lista.get(seleccion[0])
            self.pantalla.config(text=f"Se eliminó la alarma: {alarma}")
            self.hablarEnVozAlta(f"Se eliminó la alarma: {alarma}")
            EstablecerAlarma.eliminarAlarmas(alarma)
            self.leerAlarmasJson()
            
    def SeleccionMetRecurrentes(self, seleccion):
            #Metodo para borrar alarmas recurrenes         
            self.botonEliminarAlarma.destroy()

            alarma = self.listaRecurrentes.get(seleccion[0])
            self.pantalla.config(text=f"Se eliminó la alarma recurrente: {alarma}")
            self.hablarEnVozAlta(f"Se eliminó la alarma recurrente: {alarma}")

            cambiarAlarmaDeJson.EliminarAlarma(alarma)
            self.leerAlarmasRecurrentesJson()
           


    #Cuando se toca una alarma se ejecuta el sig metodo, Eliminar alarma por boton
    def alarmaSeleccionada(self, event):
        # El listbox que generó el evento
        widget = event.widget

        # Destruye botones anteriores
        if hasattr(self, "botonEliminarAlarma") and self.botonEliminarAlarma.winfo_exists():
            self.botonEliminarAlarma.destroy()
        if hasattr(self, "botonAlarmaRecurrente") and self.botonAlarmaRecurrente.winfo_exists():
            self.botonAlarmaRecurrente.destroy()

        # Si es lista normal
        if widget == self.lista:
            seleccion = widget.curselection()
            if seleccion:
                texto = widget.get(seleccion[0])
                self.hablarEnVozAlta(texto)

        # Si es lista recurrente
        elif widget == self.listaRecurrentes:
            seleccion = widget.curselection()
            if seleccion:
                texto = widget.get(seleccion[0])
                self.hablarEnVozAlta(texto)



        if self.lista.curselection():
            
            seleccion = self.lista.curselection()
            self.pantalla.configure(text=f"Alarma seleccionada: {self.lista.get(seleccion[0])}")
            self.botonAlarmaRecurrente = tk.Button(self.ventana, text="Establecer como recurrente",
                                        command=lambda: self.AlarmaRecurrente(seleccion),
                                        bg="yellow", fg="black") 
            self.botonAlarmaRecurrente.pack(pady=5)

            self.botonEliminarAlarma = tk.Button(self.ventana, text="🗑️ Borrar alarma",
                                        command=lambda: self.SeleccionMet(seleccion),
                                        bg="red", fg="white")
            self.botonEliminarAlarma.pack(pady=5)

        elif self.listaRecurrentes.curselection():
                seleccion = self.listaRecurrentes.curselection()
                self.pantalla.configure(text=f"Alarma seleccionada: {self.listaRecurrentes.get(seleccion[0])}")
                self.botonEliminarAlarma = tk.Button(self.ventana, text="🗑️ Borrar alarma",
                                            command=lambda: self.SeleccionMetRecurrentes(seleccion),
                                            bg="red", fg="white")
                self.botonEliminarAlarma.pack(pady=5)
             

        
    ################################################################################################
    def toggle_animacion(self):
        if not self.InicializadorMicro:
            return
        self.InicializadorMicro = False  # Lo marcamos inmediatamente
        self.hablarEnVozAlta("tres, dos, uno")
        self.pantalla.config(text="Espera un poco")
        self.boton_microfono.config(image=self.imagenes[1])
       
        self.ventana.update_idletasks()
        
        # Crear un hilo para ejecutar el reconocimiento de voz sin bloquear la interfaz
        def ejecutar_reconocedor():
            
            recordatorio = rag.ReconocedorVoz(self.pantalla, self.ventana, self.boton_microfono, self.imagenes)
            self.boton_microfono.config(image=self.imagenes[0])
            alarmaJson.guardarAlarma(recordatorio[0], recordatorio[1])
            self.InicializadorMicro = True  # Liberamos el botón después de todo
            self.leerAlarmasJson()
            if recordatorio[0]:
                texto = "Se creo la alarma", recordatorio[0], recordatorio[1]
            else:
                 texto="No entendí, intenta nuevamente"
            self.hablarEnVozAlta(texto)
        threading.Thread(target=ejecutar_reconocedor, daemon=True).start()
        

    def animar(self):
        # bucle que cambia la imagen del micrófono para simular movimiento.
        if self.animando:
            self.imagen_index = (self.imagen_index + 1) % len(self.imagenes)
            self.boton_microfono.config(image=self.imagenes[self.imagen_index])
            self.ventana.after(1300, self.animar)

    def agregar_alarma(self, Hora,Mensaje):
        # Cuando agrego una nueva alarma, la inserto en la lista,
        # muestro un mensaje y doy retroalimentación visual.
        alarma = Hora + " " + Mensaje
        self.lista.insert(tk.END, alarma)
        
        self.boton_microfono.config(bg="#228B22")
        self.ventana.after(800, lambda: self.boton_microfono.config(bg="#1c1c1c"))

    def editar_alarma(self):
        # Si el usuario selecciona una alarma,  activo el micrófono.
        seleccion = self.lista.curselection()
        if seleccion:
            alarma = self.lista.get(seleccion[0])
            self.pantalla.config(text=f"Editando: {alarma}")
            self.animando = True
            self.pantalla.config(text="")
            self.animar()
        else:
            self.pantalla.config(text="Selecciona una alarma para editar")

    def eliminar_alarma(self):
        # Elimino la alarma seleccionada. 
        seleccion = self.lista.curselection()
        if seleccion:
            self.lista.delete(seleccion[0])
            self.pantalla.config(text="🚫 Alarma eliminada")
        else:
            self.pantalla.config(text="Selecciona una alarma para eliminar")

    def alternar_tema(self):
        #  modo claro (azul claro) y oscuro (azul profundo),
        # y actualizo todos los colores relevantes.
        if self.tema_oscuro:
            self.ventana.configure(bg="#ABE1FE")
            self.zona.configure(bg="#ABE1FE")
            self.pantalla.configure(bg="#ABE1FE", fg="#333333")
            self.label_alarmas.configure(bg="#ABE1FE", fg="#000000")
            self.label_alarmasRecurrentes.configure(bg="#ABE1FE", fg="#000000")
            self.lista.configure(bg="#ABE1FE", fg="#003366", selectbackground="#cccccc", selectforeground="black")
            self.listaRecurrentes.configure(bg="#ABE1FE", fg="#003366", selectbackground="#cccccc", selectforeground="black")
            self.contenedorLabels.configure(bg="#ABE1FE")
        else:
            self.ventana.configure(bg="#1C2E33")
            self.zona.configure(bg="#1C2E33")
            self.pantalla.configure(bg="#1C2E33", fg="#FFFFFF")
            self.label_alarmas.configure(bg="#1C2E33", fg="white")
            self.label_alarmasRecurrentes.configure(bg="#1C2E33", fg="white")
            self.lista.configure(bg="#1C2E33", fg="#00FFAA", selectbackground="#1C2E33", selectforeground="black")
            self.listaRecurrentes.configure(bg="#1C2E33", fg="#00FFAA", selectbackground="#1C2E33", selectforeground="black")
            self.contenedorLabels.configure(bg="#1C2E33")
        self.tema_oscuro = not self.tema_oscuro

    def boton(self):
        # Este es el botón de cambio de tema con ícono gráfico.
        self.imagen = ImageTk.PhotoImage(Image.open(ruta_recurso("imagenes/oscuro.png")).resize((25, 25)))
        self.claro = tk.Button(self.ventana, image=self.imagen,
                               command=self.alternar_tema,
                               bd=0, bg="black", width=25, height=25)
        self.claro.image = self.imagen
        self.claro.place(x=420, y=16)
        self.claro.lift()


    # creo la ventana, instancio la interfaz, y lanzo el bucle principal.
ventana = tk.Tk()
app = interfaz_de_alarma(ventana)
app.boton()
ventana.mainloop()