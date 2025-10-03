class Persona:
    def __init__(self, nombre: str, apellidos: str, curp: str, edad: int, genero: str):
        self.__Nombre = nombre ###Variable Nombre ahora es de tipo privada, Se hace privada von __NomVar
        self.Apellidos = apellidos
        self.Curp = curp
        self.__Edad = edad
        self.__Genero = genero
   
    ##Como la variable solo esta displible dentro de la clase, creamos un metodo
    #intermediario el cual tiene acceso y que envie la variable privada
    def recuperarNombre(self):
        return self.__Nombre 

    def setGenero(self,genero):
        self.__Genero = genero
    def getGenero(self):
        return self.__Genero
    
    def cumplirAnios(self):
        print(f"Felicidades {self.__Nombre}, ahora tienes: ")
        self.__Edad += 1
        return self.__Edad 
    def morder(self, peso):
        print(self.__Nombre, "TE ha mordido con una fuerza de:  ", peso)
"""
personita = Persona("german", "Gutierrez", "GGGHMKDKF12", 23,"" )
personita.setGenero("Hombre")
personita.morder(23)

print(personita.recuperarNombre())
print("El genero es:", personita.getGenero())

print(personita.getGenero())


print(personita.recuperarNombre(), "a cumplido años, ahora tiene: ", personita.cumplirAnios())
"""




##############PROGRAMA "REGRESA EDAD MÁS UNO"##########################
personita = Persona(input("Ingresa el nombre:  "), "","TELA061127HHGLMLA5", int(input("Ingresa la edad:  ")), "")

print(personita.cumplirAnios())

