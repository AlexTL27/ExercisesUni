class Vaso:
    def __init__(self, capacidad, forma, color, material):

        self.Color = color
        self.Capacidad = capacidad
        self.Forma = forma
        self.Color = color
        self.Material = material


    def Rellenar(self):
        print("Se relleno el vaso de color")
    
    def Vaciar(self):
        print("Se vacio el vaso")



vaso1 = Vaso("1L","Botella", "Azul", "Plástico")
vaso1.Rellenar()
vaso2 = Vaso("3L","Botella", "transparente", "Plástico")
vaso3 = Vaso("500ml","vaso", "verde", "vidrio")
vaso4 = Vaso("200ml","esférica", "blanco", "plástico")
vaso5 = Vaso("700ml","vaso", "transparente", "vidrio")