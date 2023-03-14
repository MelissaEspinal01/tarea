from Servicio import Servicio
from Cliente import Cliente
from Servicio import ServicioSpa

class Factura(Servicio, Cliente):
    pass 
    def ticket():
        propina = (ServicioSpa.precio*0.10)
        total =  (ServicioSpa.precio*0.10)+ServicioSpa.precio
        return "Cliente {} Cantidad 1 {} Precio ${} propina ${} total a pagar {}".format(Cliente.nombre,ServicioSpa.servicio,ServicioSpa.precio,propina,total)
        
CrearTicket = Factura
print(CrearTicket.ticket())


