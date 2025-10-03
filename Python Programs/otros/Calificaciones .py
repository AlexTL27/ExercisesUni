
from itertools import count
instanciaAlumno = []



class Alumno:
    def __init__(self, Calificacion1: float,Calificacion2: float,Calificacion3: float,Calificacion4: float,Calificacion5: float):
        
        self.promMay = 0
        self.calificacion1 = Calificacion1
        self.calificacion2 = Calificacion2
        self.calificacion3 = Calificacion3
        self.calificacion4 = Calificacion4
        self.calificacion5 = Calificacion5
        
    def promedio(self):
        return (self.calificacion1 + self.calificacion2 +  self.calificacion3 +  self.calificacion4 +  self.calificacion5) / 5
    
    
    def promMayMet(self):
    
        return max(self.calificacion1, self.calificacion2, self.calificacion3, self.calificacion4, self.calificacion5)

    def promMenMet(self):
        return min(self.calificacion1, self.calificacion2, self.calificacion3, self.calificacion4, self.calificacion5)

        


def VerificarEntero(con):
    while True:
        print("Introduce la calificación número:  ", con)
        
        try:
            num = float(input())
            if num >= 0 and num <= 10:

                return num
            else:
                 print("SOLO SE ACEPTAN NÚMEROS ENTRE 0 - 10... VUELVE A INTENTAR")
            
        except:
            print("SOLO SE ACEPTAN NÚMEROS ENTRE 0 - 10... VUELVE A INTENTAR")

        
            
        
        

print("Porfavor Ingresa al alumno seguido del nombre")

conCreador = 0
for a in count():
    
    print(f"Introduce los valores del Alumno {a + 1}") 
    
    instanciaAlumno.append(Alumno(VerificarEntero(1),VerificarEntero(2),VerificarEntero(3),VerificarEntero(4),VerificarEntero(5)))
   
   
   ##Seguimos añadiendo a alumnos, o rompemos en caso de no querer más
    print("""######Pulsa -l para terminar de ingresar alumnos######
             ##Cualquier otro valor para seguir añadiendo alumnos##""")
    op = input()
    if op == "-l":
        break

suma = 0
promAlto = -1
promBajo = 11

conA = 1
for a in instanciaAlumno:
    
    print("#######################################################")
    print(f"El promedio del alumno {conA} es:  ")
    print(a.promedio())

    print(f"La calificación mayor obetenida por alumno {conA} es:  ")
    print(a.promMayMet())

    print(f"La calificación menor obetenida por alumno {conA} es:  ")
    print(a.promMenMet())

    print("#######################################################")
    conA += 1
