class Servicio:
    def __init__(self, servicio, precio):
        self.servicio = servicio
        self.precio = precio

    def ObtenerServicio(self):
        return "Servicio de la empresa {} con un precio de {}".format(self.servicio, self.precio)
    
ServicioSpa = Servicio ("Masaje corporal", 15.00)
print(ServicioSpa.ObtenerServicio())