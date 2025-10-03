class Lapicera:
    def __init__(self, color, capacidad, compartimentos,):

        self.Color = color
        self.Capacidad = capacidad
        self.Compartimentos = compartimentos


    def AbrirCompartimentos(self):
        print("Se abrio el compartimento")
    
    def CerrarCompartimentos(self):
        print("Se cerro el compartimento")




Lapicera1 = Lapicera("azul", "Grande", "2")
Lapicera1.AbrirCompartimentos()
Lapicera2 = Lapicera("verde", "mediana", "2")
Lapicera3 = Lapicera("gris", "chiquita", "1")
Lapicera4 = Lapicera("rojo", "Grande", "3")
Lapicera5 = Lapicera("cafe", "mediana", "1")