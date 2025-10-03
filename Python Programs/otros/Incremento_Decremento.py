##Aplicacion que tenga un valor inicial 

import time
incremento = 0


class Contador():
    def __init__(self):
        self.__valor = 10

    def getValor(self):
        return self.__valor


    def Incremento(self, incremento):
        self.__valor += incremento
        return self.__valor
    
    def Decremento(self, decremento):
        self.__valor -= decremento
        return self.__valor



contador = Contador()






def IncrementoDecremento():

    while True:
                try:
                    print("Solo se aceptan números enteros")
                    incremento = int(input())
                    return incremento
                except:
                    ("Solo se aceptan números enteros :((")
                


print("Bienvenido a Incremento/Decremento")
time.sleep(1.3)
while True:
        
    print("seleccion el número de la acción para:\n0.-Salir\n1.-Incrementar\n2.-Decrementar\n======:V====== ")
   


    print(f"""
        ######################
        El valor actual es de:
        ######################
        ####    {contador.getValor()}    #####
        """)

    op = input("Ingresa la opción ahora:  ")


    match op:
        case "1":
            print("Ingresa cuanto quieres incrementar :)")
            
            contador.Incremento(IncrementoDecremento())
            print("Incrementando...")
            time.sleep(1)


        case "2":
            print("Ingresa cuanto quieres decrementar :(")
            contador.Decremento(IncrementoDecremento())
            print("Decrementando...")
            time.sleep(1)
        
        case "0":
            print("Byeeee")
            break
        case _:
            print(f"la opción \"{op}\" no esta disponible por el momento, sera agregada en una futura actualización!!!!!")
            time.sleep(2)