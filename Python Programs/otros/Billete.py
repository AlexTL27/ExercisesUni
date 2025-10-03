class Billete:
    def __init__(self, valor, tipo):
        self.Valor = valor
        self.Tipo = tipo

    def Devaluarse():
        print("El billete se devaluo")
    def Valuarse():
        print("El billete aumento en valor")



billete1 = Billete("50", "Dolar")
billete2 = Billete("100", "peso")
billete3 = Billete("500", "Euros")
billete4 = Billete("2000", "yen")
billete5 = Billete("200", "soles")