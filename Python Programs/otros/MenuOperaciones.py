class Operaciones:
    
    def __init__(self, Val1,Val2):
        self.val1 = Val1
        self.val2 = Val2
    
    #SUMAR
    def Sumar(self):
        return(self.val1 + self.val2)
    #RESTAR
    def Restar(self):
        return(self.val1 - self.val2)
    #MULTIPLICAR
    def Multiplicar(self):
        return(self.val1 * self.val2)
    #DDIVIDIR
    def Dividir(self):
        if self.val2 == 0:
            return("EL SEGUNDO VALOR DADO ES 0... LA DIVISIÓN ES IMPOSIBLE")
        return(self.val1 / self.val2)


####       num1    num3
###        ---  +  ---
###        num2    num4
class Fracciones:
    def __init__(self, num1, num2, num3, num4):
        self.Num1 = num1
        self.Num2 = num2
        self.Num3 = num3
        self.Num4 = num4
    
    def Sumar(self):
        if self.Num2 == 0 or self.Num4 == 0:
            return("ALGÚN VALOR DADO ES 0... LA OPERACIÓN ES IMPOSIBLE")
        mul1 = self.Num1 * self.Num4
        mul2 = self.Num2 * self.Num3
        den = round(self.Num2 * self.Num4)

        num = round(mul1 + mul2)
       
        if den == num:
            return("El resultado es 1 (un entero)")

        con = 2
        if den > num :
            menor = num
        else:
            menor = den

        while con < menor:
           
            if den % con == 0:
                if num % con == 0:

                    den = den / con
                    num = num / con
                    con == 2
                    
            con+=1
        return(round(num),"/",round(den))
    
    def Restar(self):

        if self.Num2  == 0 or self.Num4 == 0:
            return("ALGÚN VALOR DADO ES 0... LA OPERACIÓN ES IMPOSIBLE")
        mul1 = self.Num1 * self.Num4
        mul2 = self.Num2 * self.Num3
        den = round(self.Num2 * self.Num4)

        num = round(mul1 - mul2)
       
        if den == num:
            return("El resultado es 1 (un entero)")

        con = 2
        if den > num :
            menor = num
        else:
            menor = den

        while con < menor:
           
            if den % con == 0:
                if num % con == 0:

                    den = den / con
                    num = num / con
                    con == 2
                    
            con+=1
        return(round(num),"/",round(den))
    
    def Multiplicar(self):
        if self.Num2 == 0  or self.Num4 == 0 or self.Num1 == 0  or self.Num3 == 0:
            return("ALGÚN VALOR DADO ES 0... LA OPERACIÓN ES IMPOSIBLE O IGUAL A \"0\"")
        
        num = round(self.Num1 * self.Num3)
        den = round(self.Num2 * self.Num4)
        return(num,"/",den)
        
    def Dividir(self):
        if self.Num2 == 0  or self.Num4 == 0 or self.Num1 == 0  or self.Num3 == 0:
            return("ALGÚN VALOR DADO ES 0... LA OPERACIÓN ES IMPOSIBLE O IGUAL A \"0\"")
        
        num = round(self.Num1 * self.Num4)
        den = round(self.Num2 * self.Num3)
        return(num,"/",den)


            
            

    

while True:
    bandera = True
    print("Bienvenido al menu de operaciones. Ingresa el número designado para:\n0.-Salir\n1.-Menu de fracciones\n2.-Sumar\n3.-Restar\n4.-Multiplicaciones\n5.-Divisiones")



    op = input()
    
     
    if not(op == "1" or op =="2" or op == "3" or op == "4" or op == "5" or op == "0"):
        ##Se ejecutara en caso de que se un valor invalido(letra, numero fura de rango)
        print("=======opción no válida========")
        continue
    
    if int(op) == 0:
        break
    #Asegurar que no se ejecute el menu de fracciones
    if int(op) != 1:
        print("Ingrese dos valores")
    
        #Instanciando objeto con dos valores numericos
        while True:

            try:
                if bandera:
                    print("Ingresa el primer número:")
                    num1 = float(input())
                    bandera = False
                print("Ingresa el Segundo número:")
                num2 = float(input())
                break
            except:
                print("Porfavor, Ingresa solo números...VUELVE A INTENTAR")

        operacion = Operaciones(num1, num2)
        
        print("Resultado: ")
    else:
        ##EJECUTAREMOS MENU DE FRACCIONES
        print("Ingresa 4 valores... RECUERDA: ")
        print("""
                 numerador        El Número de arriba
                ----------- 
                denominador       El Número de abajo
            
              
              """)
        
        while True:

            try:
                
                if bandera:
                    print("Ingresa el numerador de la primer fracción:")
                    num1 = float(input())
                    print("Ingresa el denominador de la primer fracción:")
                    num2 = float(input())
                    bandera = False
                
                print("Ingresa el numerador de la segunda fracción:")
                num3 = float(input())
                print("Ingresa el denominador de la segunda fracción:")
                num4 = float(input())
                break
                

            except:
                print("Porfavor, Ingresa solo números...VUELVE A INTENTAR")
        #INstanciamos el objeto fraccion
        fraccion = Fracciones(num1, num2, num3, num4)
     
    match op:
        
        case "1":
            print("Ingresa un número para: \n1.-Sumar\n2.-Restar\n3.-Multiplicar\n4.-Dividir")
            op = input()

            match op:
                case "1":
                 print(fraccion.Sumar())
                case "2":
                 print(fraccion.Restar())
                case "3":
                 print(fraccion.Multiplicar())
                case "4":
                    print(fraccion.Dividir())
        case "2":
            print(operacion.Sumar())
             
        case "3":
            print(operacion.Restar())
        case "4":
            print(operacion.Multiplicar())
        case "5":
            print(operacion.Dividir())
    
    
    input("Pulsa enter para continuar")


print("GRACIAS POR USAR NUESTRO MENU :)")