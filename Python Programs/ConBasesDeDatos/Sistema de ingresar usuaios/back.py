import mysql.connector
from mysql.connector import Error,errors

import tkinter as tk
from tkinter import messagebox
#import conection as MyCn

#PDF
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

from fpdf import FPDF
from tkinter import filedialog

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet


import datetime

class alumnos:
    def __init__(self,Matricula, Nombre, Apellidos, Nac, Gen, Dir, Car, Img):
        self.matricula = Matricula
        self.nombre = Nombre
        self.apellidos = Apellidos
        self.nac = Nac
        self.gen = Gen
        self.dir = Dir
        self.car = Car
        self.img = Img
        self.GuardarEnBD()

    # Crear raíz oculta para que messagebox funcione sin ventana principal
        self.root = tk.Tk()
        self.root.withdraw()
    def GuardarEnBD(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="registrodealumnos")

            cursor = conexion.cursor()

            #preparar la consulta
            sql = "insert into alumno (matricula, nombre, apellidos, nac, gen, dir, carrera,img) values (%s, %s, %s, %s, %s, %s, %s,%s)"
            valores = (self.matricula,self.nombre,self.apellidos,self.nac,self.gen,self.dir,self.car,self.img)

            #ejecutar y guardar cambios
            cursor.execute(sql, valores)
            conexion.commit()
  
        except:
            
            print(f"Error al Guardar")
                    
           


        finally:
            if 'conexion' in locals() and conexion.is_connected():
                cursor.close()
                conexion.close()


def MostrarDatos():
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="registrodealumnos"
            )


            cursor = conexion.cursor()
            cursor.execute("select * from alumno")
            resultados = cursor.fetchall()

            cursor.close()
            conexion.close()
            return resultados

        except:
              print(f"Error al obtener alumno")
              return []

def EliminarAlumno(matricula):
    try:
            conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="registrodealumnos"
            )
            cursor = conexion.cursor()
            sql = "DELETE FROM alumno WHERE matricula = %s"
            cursor.execute(sql, (matricula,))
            conexion.commit()
            cursor.close()
            conexion.close()
            
     
    except:
              print(f"Error al ELiminar alumno")


def ExisteMatricula(matricula):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="registrodealumnos"
        )
        cursor = conexion.cursor()
        sql = "SELECT 1 FROM alumno WHERE matricula = %s LIMIT 1"
        cursor.execute(sql, (matricula,))
        resultado = cursor.fetchone()  # Obtiene una fila o None
        cursor.close()
        conexion.close()
        
        return resultado is not None

    except mysql.connector.Error as err:
        print(f"Error al verificar matrícula: {err}")
        return False
    


prom = 0
def ConocerIMG(matricula):
    try:
        conexion = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="registrodealumnos")

        cursor = conexion.cursor()

        #preparar la consulta
        sql = "select img from alumno where matricula=%s"

        
        valores = (matricula,)

        #ejecutar y guardar cambios
        cursor.execute(sql, valores)
        resultado = cursor.fetchone()

        conexion.close()
        if resultado:
            return resultado[0]  # devuelve el valor de img
        else:
            return None

    except Exception as e:
        print(f"Error al obtener imagen del alumno: {e}")
        return None
     


def exportarAlumno(alumno):
    global prom
    prom = 0
    w, h = letter

       # Pedir ubicación y nombre del archivo
    ruta_pdf = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Archivos PDF", "*.pdf")],
        title="Guardar historial académico como..."
    )
    if not ruta_pdf:
        return  # Si el usuario cancela, no hace nada

    c = canvas.Canvas(ruta_pdf, pagesize=letter)

    

      # === Imagen de fondo ===
    c.drawImage(
        r"C:\Users\efren\OneDrive\Desktop\3erCuatri\Imagenes\fondo.jpg",  # ruta de tu imagen
        0, 0,                    # coordenadas esquina inferior izquierda
        width=w, height=h        # ocupar toda la página
    )

    c.rect(50,h-130,510,80)
    c.drawImage(r"C:\Users\efren\OneDrive\Desktop\3erCuatri\Imagenes\logoUTSH.jpg",60,h-127,width=80,height=70)
    c.line(150,h-50,150,h-130)

      # Estilo
    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Helvetica"
    style.fontSize = 12

    texto = f"""<b>Universidad Tecnológica de la Sierra Hidalguense</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 255, h-80)  # posición exacta




    
    texto = f"""<b>Historial Académico</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 290, h-110)  # posición exacta


    fecha_actual = datetime.date.today()
   
    #################################################

    # Texto con mezcla de negritas y normal
    texto = f"""Zacualtipán de Ángeles Hgo., a <b>{fecha_actual.strftime('%d')} de agosto</b> del{fecha_actual.strftime('%Y')}"""

    
  
    # Crear párrafo
    p = Paragraph(texto, style)

        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 300, h-180)  # posición exacta

    #################################################

    texto = f"""<b>Datos del estudiante</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)

        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 255, h-230)  # posición exacta

    #imagen
    
    #Sacar imagen
    img = ConocerIMG(alumno[0])

    
    #Guardar temporal y poner imagen
    from tempfile import NamedTemporaryFile

    with NamedTemporaryFile(delete=False, suffix=".jpg") as temp_img_file:
      temp_img_file.write(img)
      temp_img_path = temp_img_file.name

    c.drawImage(temp_img_path,50,h-350,width=100,height=100)


    c.drawString(180,h-260, "Nombre:") #2 apellidos y direccion
    c.drawString(180,h-280, "Matrícula:")
    c.drawString(320,h-280, "Género:")
    c.drawString(180,h-300, "Fecha de Nacimiento:")
    c.drawString(180,h-320, "Dirección:")
    c.drawString(180,h-340, "Carrera:")   


    #Datos a ingresar
        #Nombre
    texto = f"""<b>{alumno[1]} {alumno[2]}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 240, h-260)  # posición exacta

        #Matrícula
    texto = f"""<b>{alumno[0]}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 240, h-280)  # posición exacta

        #Género
    texto = f"""<b>{alumno[4]}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 370, h-280)  # posición exacta

        #Nacimiento
    texto = f"""<b>{alumno[3]}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 305, h-300)  # posición exacta

        #Dirección
    texto = f"""<b>{alumno[5]}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 240, h-320)  # posición exacta

        #Carrera

    texto = f"""<b>{alumno[6]}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 240, h-340)  # posición exacta




    #Calificaciones
    texto = f"""<b>Calificaciones</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 255, h-400)  # posición exacta


    texto = f"""<b>Materia</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 50, h-440)  # posición exacta

    
   
    texto = f"""<b>Calificación</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 390, h-440)  # posición exacta


    c.line(50,h-450,510,h-450)
    c.line(380,h-450,380,h-620)

    #Materias
    c.drawString(50,h-470, "Base de Datos")
    c.drawString(50,h-500, "Desarrollo y Pensamiento y Toma de Decisiones")
    c.drawString(50,h-530, "Inglés 3")
    c.drawString(50,h-560, "Programación Orientada a Objetos")
    c.drawString(50,h-590, "Proyecto Integrador |")
    c.drawString(50,h-620, "Tópicos de Calidad para el Diseño de Software")

 
    #Calificaciones
        #BD
    texto = f"""<b>{conocerCalfNombre("base", alumno[0])}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 440, h-470)  # posición exacta


        #Desarrollo
    texto = f"""<b>{conocerCalfNombre("desarrollo", alumno[0])}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 440, h-500)  # posición exacta

        #Inglés
    texto = f"""<b>{conocerCalfNombre("ingles", alumno[0])}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 440, h-530)  # posición exacta

        #Poo
    texto = f"""<b>{conocerCalfNombre("programacion", alumno[0])}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 440, h-560)  # posición exacta

        #Proyecto
    texto = f"""<b>{conocerCalfNombre("proyecto", alumno[0])}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 440, h-590)  # posición exacta


        #Tópicos

    texto = f"""<b>{conocerCalfNombre("topicos", alumno[0])}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 440, h-620)  # posición exacta


    #Promedio
    texto = f"""<b>Promedio General:</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 390, h-670)  # posición exacta



    promFinal = float(prom / 6)
    promFinal = round(promFinal,1)
    texto = f"""<b>{str(promFinal)}</b>"""
    # Crear párrafo
    p = Paragraph(texto, style)
        # Dibujar en coordenadas exactas
    p.wrapOn(c, 400, 100)  # ancho y alto máximos
    p.drawOn(c, 510, h-670)  # posición exacta


    c.line(510,h-680,525,h-680)
    c.save()



def conocerCalfNombre(materia, matricula):
    global prom
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="registrodealumnos"
        )
        cursor = conexion.cursor()
        sql = "select calificacion from calificacion where id_alumno=%s and id_materia = (select id_materia from materia where nombre = %s)"
       
        cursor.execute(sql, (matricula, materia))
        resultado = cursor.fetchone()
        print("Resultado de la consulta:", resultado)
        

        cursor.close()
        conexion.close()

        if resultado:
            prom += int(resultado[0])
            return str(resultado[0])  # Aquí tomamos solo el valor
        else:
            return "No Registrada"
    except:
         print("Error al guardar calificaciones")






def calfBD(matricula, calf):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="registrodealumnos"
        )
        cursor = conexion.cursor()

        for i in range(len(calf)):
      
            #Insertamos datos o actualizamos
            
            sql = "insert into calificacion(id_alumno, id_materia, calificacion) values (%s,%s,%s) on duplicate key update calificacion = values(calificacion)"
            cursor.execute(sql, (matricula,i+1,calf[i]))
            conexion.commit()
            
        cursor.close()
        conexion.close()
    except:
         print("Error al guardar calificaciones")

def conocerCalf(matricula, id):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="registrodealumnos"
        )
        cursor = conexion.cursor()

        sql = """
            SELECT calificacion 
            FROM calificacion 
            WHERE id_alumno = %s 
              AND id_materia = %s;
        """
       
        print(f"Buscando calificación para alumno: {matricula}, materia: '{id}'")
        cursor.execute(sql, (matricula, id))

        resultado = cursor.fetchone()
        print("Resultado de la consulta:", resultado)

        cursor.close()
        conexion.close()

        if resultado:
            return str(resultado[0])  # Aquí tomamos solo el valor
        else:
            return "No Registrada"
    except mysql.connector.Error as err:
        print(f"Error en la consulta: {err}")
        return "UWU"
