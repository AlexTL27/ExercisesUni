class Operaciones:
    def __init__(self, valor1, valor2):
        self.num1 = valor1
        self.num2 = valor2

    def sumar(self):
        return(self.num1+ self.num2)
    
    #valor1 y valo2 estan declaradas dentro del metodo constructor,
    #sin embargo esas variables solo existen en ese metodo.
    #AUNQUE SON LAS MISMAS VARIABLES, EXISTEN EN ESPACIOS DISTINTOS
    def restar(self, valor1, valor2 ):
        return(valor1 - valor2)
    

##creamos la instancia de operaion
#operacion debe ser inicializada con dos valores
oper = Operaciones(4,5)
print(oper.sumar())