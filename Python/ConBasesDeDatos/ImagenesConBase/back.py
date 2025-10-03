from PIL import Image, ImageTk
import io
import tkinter as tk
import mysql.connector

class pregunta:
    def __init__(self, Pregunta, Respuesta, Imagen, NombreIMG):
        self.pregunta = Pregunta
        self.respuesta = Respuesta
        self.img = Imagen
        self.nombreImg = NombreIMG

        self.guardarBD()

    def guardarBD(self):
      
        cn = self.Conectar()
        miCursor = cn.cursor()
        sql = "insert into yesnoquestion (pregunta,respuesta,imagen,nombreImg) values(%s,%s,%s,%s)"
        valores=(self.pregunta,self.respuesta,self.img,self.nombreImg)
        miCursor.execute(sql,valores)
        cn.commit()
        


    def Conectar(self):
        cn = mysql.connector.connect(host="localhost",
                                            user="root",
                                            password = "",
                                            port="3306",
                                            database="universidad")
        return cn
    
def mover_boton(event, boton):
    import random
    import math

    ventana = event.widget.winfo_toplevel()
    ancho_ventana = ventana.winfo_width()
    alto_ventana = ventana.winfo_height()

    # Coordenadas del mouse en la ventana
    mouse_x = event.x_root - ventana.winfo_rootx()
    mouse_y = event.y_root - ventana.winfo_rooty()

    ultima_x, ultima_y = 0.5, 0.5  # por si no encuentra buena ubicación

    for _ in range(20):
        nueva_x_rel = random.uniform(0.1, 0.9)
        nueva_y_rel = random.uniform(0.4, 0.8)

        nueva_x = nueva_x_rel * ancho_ventana
        nueva_y = nueva_y_rel * alto_ventana

        # Distancia entre el mouse y la nueva posición del centro del botón
        distancia = math.hypot(nueva_x - mouse_x, nueva_y - mouse_y)

        if distancia > 100:
            ultima_x, ultima_y = nueva_x_rel, nueva_y_rel
            break

    boton.place(relx=ultima_x, rely=ultima_y, anchor="center")

def VentanaNueva(valores):
    # Conexión a base de datos
    cn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        port="3306",
        database="universidad"
    )
    cursor = cn.cursor()

    cursor.execute("SELECT imagen FROM yesnoquestion WHERE id = %s", (int(valores[0]),))
    resultado = cursor.fetchone()
    miImagen = resultado[0]

    # Crear ventana
    ventana = tk.Toplevel()
    ventana.geometry("800x400")
    ventana.title("Pregunta con Fondo")

    # Convertir bytes a imagen
    imagen = Image.open(io.BytesIO(miImagen))
    imagen = imagen.resize((800, 400))
    fondo = ImageTk.PhotoImage(imagen)

    # Crear Label de fondo
    fondo_label = tk.Label(ventana, image=fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    fondo_label.image = fondo  # Mantener referencia
    fondo_label.lower()  # Enviar al fondo

    # Pregunta
    pregunta = tk.Label(ventana, text=valores[1], font=("Arial", 18), bg="gray",fg="white")
    pregunta.place(relx=0.5, rely=0.2, anchor="center")

    # Botones
    btn_si = tk.Button(ventana, text="Sí", font=("Arial", 14), width=10, bg="lightgreen",
                       command=lambda: print("Respuesta: sí"))
    btn_si.place(relx=0.4, rely=0.6, anchor="center")

    btn_no = tk.Button(ventana, text="No", font=("Arial", 14), width=10, bg="lightcoral",
                       command=lambda: print("Respuesta: no"))
    btn_no.place(relx=0.6, rely=0.6, anchor="center")

    if valores[2] == "si":
        btn_si.bind("<Enter>",lambda event: mover_boton(event,btn_si))
        btn_no.configure(command=ventana.destroy)
    else:
        btn_no.bind("<Enter>",lambda event: mover_boton(event,btn_no))
        btn_si.configure(command=ventana.destroy)




    ventana.mainloop()
