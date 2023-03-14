from Estudiantes import Estudiante

class Asistencia(Estudiante):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad, carrera)
        self.asistencia = 0

    def marcar_asistencia(self):
        self.asistencia += 1
        print("El estudiante {} de {} años, de la carrera {} asistió a la clase".format(self.nombre, self.edad, self.carrera))

estudiante1 = Asistencia("Juan", 20, "Ingeniería")
estudiante2 = Asistencia("Pedro", 21, "Medicina")
estudiante3 = Asistencia("María", 19, "Arquitectura")

estudiante1.marcar_asistencia()
estudiante2.marcar_asistencia()
estudiante3.marcar_asistencia()

print("El estudiante {} tiene {} asistencias.".format(estudiante1.nombre, estudiante1.asistencia))
print("El estudiante {} tiene {} asistencias.".format(estudiante2.nombre, estudiante2.asistencia))
print("El estudiante {} tiene {} asistencias.".format(estudiante3.nombre, estudiante3.asistencia))
