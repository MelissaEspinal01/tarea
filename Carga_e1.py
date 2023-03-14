from Banca import Banca

class Partido(Banca):
    def __init__(self, nombre, camisa, posicion):
        super().__init__(nombre)
        self.camisa = camisa
        self.posicion = posicion

    def jugar(self):
        return "El jugador {} con camisa {} juega la posicion {}".format(self.nombre, self.camisa, self.posicion)

jugador1 = Partido("Jonathan", 9, "de mediocampista")
jugador2 = Partido("Messi", 10, " de delantero")
jugador3 = Partido("Piqué", 5, " de defensa")

print(jugador1.jugar())
print(jugador2.jugar())
print(jugador3.jugar())