import time
import random
from datetime import datetime





def CargarBanco():
    print("Accediendo al menu principal del Banco...")
    time.sleep(1)
    print("""
          0%                                          100%
          
          """)

    time.sleep(random.uniform(0,1))

    print("""
          0%                                          100%
          ####
          """)
    time.sleep(random.uniform(0,1))
    print("""
          0%                                          100%
          #######
          """)
    time.sleep(random.uniform(0,1))
    print("""
          0%                                          100%
          ###############
          """)
    time.sleep(random.uniform(0,1))
    print("""
          0%                                          100%
          ############################
          """)
    time.sleep(random.uniform(0,1))
    print("""
          0%                                          100%
          ##########################################
          """)
    time.sleep(random.uniform(0,1))
    print("""
          0%                                          100%
          ##############################################
          """)
    time.sleep(random.uniform(0,1))
    print("""
          0%                                          100%
          ###############################################
          """)
    time.sleep(random.uniform(0,2))


def VerificarSaldoCorrecto():
     while True:
                print("Ingresa solo numeros mayores a 0")
                try:
                    print(f"Saldo actual: {propietario.getDinero()}")
                    cantidad = float(input("Ingrese la cantidad:  "))
                    if cantidad >= 0:
                        return cantidad

                except:
                    print("Error")


###############Clase principal del programa###################
class CuentaBancaria():
    def __init__(self):
        
        self.__Propietario = ""
        self.__Dinero = 0
        self.__FechaApertura = 0
        self.__AccIngresarDinero = 0
        self.__AccRetirarDinero = 0
        self.__AccCambiarPropietario = 0
        self.__bandera = True


    def IngresarDinero(self, cantidad: float):
        self.__Dinero = self.__Dinero + cantidad
        print("HECHO")
        self.__AccIngresarDinero += 1

    def RetirarDinero(self, cantidad: float):
        self.__Dinero = self.__Dinero - cantidad
        self.__AccRetirarDinero += 1

        print("HECHO")
    def getDinero(self):
        return self.__Dinero
    
    def setPropietario(self):

        print("Las políticas de nuestro banco no son complicadas, solo necesitamos su nombre :)")
        self.__Propietario = input("Ingresa el nombre del nuevo propietario:  ")
        
        if self.__bandera:
            self.__bandera = False
        else:
            self.__AccCambiarPropietario += 1
            self.__bandera = True
        self.__FechaApertura = datetime.now().date()
        return self.__Propietario
    
    def getPropietario(self):
        return self.__Propietario
    def getFechaIngreso(self):
        return self.__FechaApertura
    def VerAcciones(self):
        print("Veces que ingresaron dinero:  ", self.__AccIngresarDinero )
        print("Veces que retiraron dinero:  ", self.__AccRetirarDinero )
        print("Veces que cambiaron el propietario:  ", self.__AccCambiarPropietario)
        input("Pulsa enter para continuar")


##Primer Contacto con el usuario
print("===Bienvenido===")
print("Antes de ingresar, necesitas registrarte...")

propietario = CuentaBancaria()

propietario.setPropietario()


while True:
        

    CargarBanco()
        
    print(f"\nBienvenido, Usuario: {propietario.getPropietario()} ")
    print((f"\nUsted es usuario desde: {propietario.getFechaIngreso()}"))
    print("Saldo actual")
    print(f"====={propietario.getDinero()}=====")
    print("""      
        0-Salir :(   
        1.-Ingresar dinero
        2.-Retirar Dinero
        3.-Cambiar propietario
        4.-Ver movimientos recientes   
        """)

    op = input("Porfavor, Selecciona el número de la acción deseada:  ")

    match op:
        case "1":        
            print("Ingresa 0 para regresar")
            while True:
                print("El deposito no puede ser mayor a 5000")
                resto = VerificarSaldoCorrecto()
                if resto < 5000:
                    break
            propietario.IngresarDinero(resto)

        case "2":
            print("Ingresa 0 para regresar")
            while True:
                    
                resto = VerificarSaldoCorrecto()
                if resto > propietario.getDinero():
                    print("Saldo insuficiente... Vuelve a intentar")
                else:
                    break
            
            propietario.RetirarDinero(resto)
        case "3":
            propietario.setPropietario()
        case "4":
            propietario.VerAcciones()
        case "0":
            print("Gracias por usar nuestros servicios...")
            break


