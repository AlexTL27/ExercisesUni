import tkinter as tk

#Ventana principal
VentanaPrincipal = tk.Tk()
VentanaPrincipal.geometry("370x350")
VentanaPrincipal.title("Calculadora")
VentanaPrincipal.configure(background=("black"))
#etiquetas principales
cajaResultado = tk.Label(VentanaPrincipal,text="Ingresa algo..",font="Arial,20")
cajaResultado.grid(row=1,column=0,columnspan=3)

cajaResultadoDes = tk.Label(VentanaPrincipal,text="\\\\\\Resultado///",font="Arial,20")
cajaResultadoDes.grid(row=7,column=0,columnspan=3)
cajaFinal = tk.Label(VentanaPrincipal,text="Esperando Resultado :)",font="Arial,20")
cajaFinal.grid(row=0,column=1,columnspan=3)

#variables globales
cadena = ""
cantidad1 = ""
cantidad2 = ""
QueCantidadEstoy = True
signoUsado = True
bandera = False
parteEcuacion = 0
res = 0
#metodo para no repetir codigo
def Valor():

    
    global QueCantidadEstoy, signoUsado, bandera
    bandera = True
    QueCantidadEstoy = True
    QueCantidadEstoy = False
    
def ConsegirResultado():
    global res, cadena, cantidad2, cantidad1
    cajaResultado.configure(text=res)
    BorrarTodo()
    cantidad1 = res
    ObtenerValor(cantidad1)
    print(res)


#metodo ue invocan los botones
def ObtenerValor(valor):
    global cadena, cantidad1,res, cantidad2, QueCantidadEstoy, signoUsado, bandera, parteEcuacion
    bandera = False
    if cadena and str(valor) in "+-*/" and cadena[-1] in "+-*/":
        cadena = cadena[:-1] + str(valor)
        cajaResultado.configure(text=cadena)
        return
    if (valor == "." and "." in cantidad1) or  (valor == "+" and "+" in cadena) or (valor == "-" and "-" in cadena) or (valor == "*" and "*" in cadena) or (valor == "/" and "/" in cadena):
    
        return
  



    if  valor == "+":
        if cantidad1 == "":
            return
        Valor()
        if signoUsado == False:
             return
        signoUsado = False
    if valor == "-":
        if cantidad1 == "":
         return
        Valor()
        if signoUsado == False:
             return
        signoUsado = False
    if valor == "*":
        if cantidad1 == "":
            return
        Valor()
        if signoUsado == False:
             return
        signoUsado = False
    if valor == "/":
        if cantidad1 == "":
            return
        Valor()
        if signoUsado == False:
             return
        signoUsado = False
    
    cadena = cadena + "" + str(valor)
    cajaResultado.configure(text=cadena)
    if cantidad2 == "":
        parteEcuacion = 3
    if bandera:
        bandera = False
        return
    else:
        if QueCantidadEstoy:
            parteEcuacion = 1
            signoUsado = True
            try:
                cantidad1 = cantidad1 +""+str(valor)
                print("hola")
                print("Cantidad1: ",cantidad1, "Cantidad2:", cantidad2)
            except:
                pass

        else:
            parteEcuacion=2 
            cantidad2 = cantidad2 +""+ str(valor)
            print("Cantidad1: ",cantidad1, "Cantidad2:", cantidad2)
            
            try:
                if "+" in cadena:
                    res = float(cantidad1) + float(cantidad2)
                if "-" in cadena:
                    res = float(cantidad1) - float(cantidad2)
                if "*" in cadena:
                    res = float(cantidad1) * float(cantidad2)
                if "/" in cadena:
                    if "0" in cantidad2:
                        print("Error en cantdad")
                        res="Error, División por cero"
                        
                    else:
                        res = float(cantidad1) / float(cantidad2)
                        

            except:
                if cadena in ("+-/*"):
                    parteEcuacion=2
                else:
                    parteEcuacion=1
                print(parteEcuacion)
 

    


   



#botones
sieteBoton = tk.Button(VentanaPrincipal,text="7",width=6,height=2)
sieteBoton.grid(row=2,column=0,padx=10,pady=10)
sieteBoton.configure(command=lambda: ObtenerValor(7))

ochoBoton = tk.Button(VentanaPrincipal,text="8",width=6,height=2)
ochoBoton.grid(row=2,column=1,padx=10,pady=10)
ochoBoton.configure(command=lambda: ObtenerValor(8))

nueveBoton = tk.Button(VentanaPrincipal,text="9",width=6,height=2)
nueveBoton.grid(row=2,column=2,padx=10,pady=10)
nueveBoton.configure(command=lambda: ObtenerValor(9))

cuatroBoton = tk.Button(VentanaPrincipal,text="4",width=6,height=2)
cuatroBoton.grid(row=3,column=0,padx=10,pady=10)
cuatroBoton.configure(command=lambda: ObtenerValor(4))

cincoBoton = tk.Button(VentanaPrincipal,text="5",width=6,height=2)
cincoBoton.grid(row=3,column=1,padx=10,pady=10)
cincoBoton.configure(command=lambda: ObtenerValor(5))

seisBoton = tk.Button(VentanaPrincipal,text="6",width=6,height=2)
seisBoton.grid(row=3,column=2,padx=10,pady=10)
seisBoton.configure(command=lambda: ObtenerValor(6))

unoBoton = tk.Button(VentanaPrincipal,text="1",width=6,height=2)
unoBoton.grid(row=4,column=0,padx=10,pady=10)
unoBoton.configure(command=lambda: ObtenerValor(1))

dosBoton = tk.Button(VentanaPrincipal,text="2",width=6,height=2)
dosBoton.grid(row=4,column=1,padx=10,pady=10)
dosBoton.configure(command=lambda: ObtenerValor(2))

tresBoton = tk.Button(VentanaPrincipal,text="3",width=6,height=2)
tresBoton.grid(row=4,column=2,padx=10,pady=10)
tresBoton.configure(command=lambda: ObtenerValor(3))

ceroBoton = tk.Button(VentanaPrincipal,text="0",width=6,height=2)
ceroBoton.grid(row=5,column=0,padx=10,pady=10)
ceroBoton.configure(command=lambda: ObtenerValor(0))

puntoBoton = tk.Button(VentanaPrincipal,text=".",width=6,height=2)
puntoBoton.grid(row=5,column=1,padx=10,pady=10)
puntoBoton.configure(command=lambda: ObtenerValor("."))


#operadores botones
sumaBoton = tk.Button(VentanaPrincipal,text="+",width=6,height=2)
sumaBoton.grid(row=2,column=5,padx=10,pady=10)
sumaBoton.configure(command=lambda: ObtenerValor("+"))

restaBoton = tk.Button(VentanaPrincipal,text="-",width=6,height=2)
restaBoton.grid(row=3,column=5,padx=10,pady=10)
restaBoton.configure(command=lambda: ObtenerValor("-"))

multiplicacionBoton = tk.Button(VentanaPrincipal,text="*",width=6,height=2)
multiplicacionBoton.grid(row=4,column=5,padx=10,pady=10)
multiplicacionBoton.configure(command=lambda: ObtenerValor("*"))

divisionBoton = tk.Button(VentanaPrincipal,text="/",width=6,height=2)
divisionBoton.grid(row=5,column=5,padx=10,pady=10)
divisionBoton.configure(command=lambda: ObtenerValor("/"))

igualBoton = tk.Button(VentanaPrincipal,text="=",width=6,height=2)
igualBoton.grid(row=6,column=5,padx=10,pady=10)
igualBoton.configure(command=ConsegirResultado)



#boton para borrar
def BorrarTodo():
    global cadena, cantidad1, cantidad2, QueCantidadEstoy,signoUsado,bandera
    cadena = ""
    cantidad1 = ""
    cantidad2 = ""
    QueCantidadEstoy = True
    signoUsado = True
    bandera = False
    cajaResultado.configure(text="")
    cajaFinal.configure(text="")

    
borrarBoton = tk.Button(VentanaPrincipal,text="<-",width=6,height=2)
borrarBoton.grid(row=5,column=2,padx=10,pady=10)
borrarBoton.configure(command=BorrarTodo)

#boton borrar por partes

def BorrarPorPartes():
    global parteEcuacion, cantidad1, cantidad2, cadena, signoUsado, QueCantidadEstoy
    if not cadena:
        return
    if cadena[-1] in "+-*/":
        QueCantidadEstoy = True
        valTem = cadena[:-1]
        cadena = valTem
        ObtenerValor(cadena[-1])
        signoUsado = True
        print(cadena)
    
    
    if parteEcuacion == 2:
        
        valTem = cantidad2
        cantidad2 = ""
        cadena = cadena[:-(len(valTem))]
        ObtenerValor(valTem[:-1])
       
    elif parteEcuacion == 1:
        valTem = cantidad1
        cantidad1 = ""
        cadena = cadena[:-(len(valTem))]
        cajaResultado.configure(text=cantidad1)
        ObtenerValor(valTem[:-1])
      
    


borrarPartesBoton = tk.Button(VentanaPrincipal,text="\\\\\\<-///",width=6,height=2)
borrarPartesBoton.grid(row=6,column=3,padx=10,pady=10,rowspan=6)
borrarPartesBoton.configure(command=BorrarPorPartes)

print("Cantidad1: ",cantidad1, "Cantidad2:", cantidad2)

VentanaPrincipal.mainloop()

