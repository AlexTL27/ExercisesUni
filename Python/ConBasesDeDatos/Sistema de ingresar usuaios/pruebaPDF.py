from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from datetime import datetime

w, h = letter
c = canvas.Canvas("Muestra.pdf", pagesize=letter)
fecha_actual = datetime.now()

# Texto con mezcla de negritas y normal
texto = f"""Zacualte Ángeles Hgo., a <b>{fecha_actual.strftime('%d')} de agosto del {fecha_actual.strftime('%Y')}</b>"""


# Estilo
styles = getSampleStyleSheet()
style = styles["Normal"]
style.fontName = "Helvetica"
style.fontSize = 12
fecha_actual = datetime.now()

c.rect(50,h-130,510,80)
c.drawImage(r"C:\Users\efren\OneDrive\Desktop\3erCuatri\Imagenes\logoUTSH.jpg",60,h-127,width=80,height=70)
c.line(150,h-50,150,h-130)

c.drawString(225,h-80, "Universidad Tecnológica de la Sierra Hidalguense")


# Crear párrafo
p = Paragraph(texto, style)

# Dibujar en coordenadas exactas
p.wrapOn(c, 400, 100)  # ancho y alto máximos
p.drawOn(c, 300, h-180)  # posición exacta
c.drawString(290,h-110, "Historial Académico")



c.drawString(255,h-230, "Datos del estudiante")


c.drawImage(r"C:\Users\efren\OneDrive\Desktop\3erCuatri\Imagenes\mclovin.jpg",50,h-350,width=100,height=100)


c.drawString(180,h-260, "Nombre:") #2 apellidos y direccion
c.drawString(180,h-280, "Matrícula:")
c.drawString(320,h-280, "Género:")
c.drawString(180,h-300, "Fecha de Nacimiento:")
c.drawString(180,h-320, "Dirección:")
c.drawString(180,h-340, "Carrera:")   


#Datos a ingresar
    #Nombre
c.drawString(240,h-260, "Alex Efrén Téllez Limón Alías:Maclovin")
    #Matrícula
c.drawString(240,h-280, "20240184")
    #Género
c.drawString(370,h-280, "Brujer")
    #Nacimiento
c.drawString(305,h-300, "27/11/2006")
    #Dirección
c.drawString(240,h-320, "Tecnologías de la información")
    #Carrera
c.drawString(240,h-340, "Desarrollo de Software multiplataforma")


#Calificaciones
c.drawString(255,h-400, "Calificaciones")

c.drawString(50,h-440, "Materia")
c.drawString(390,h-440, "Calificación")
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
c.drawString(440,h-470, "10")
    #Desarrollo
c.drawString(440,h-500, "10")
    #Inglés
c.drawString(440,h-530, "10")
    #Poo
c.drawString(440,h-560, "10")
    #Proyecto
c.drawString(440,h-590, "10")
    #Tópicos
c.drawString(440,h-620, "10")

#Promedio
c.drawString(390,h-670, "Promedio General:")

c.drawString(510,h-670, "10")
c.line(510,h-680,525,h-680)
c.save()