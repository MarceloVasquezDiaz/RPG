import maestria
import random

class Arma:
    def __init__(self, nombre, estadistica, durabilidad, maestria):
        self.nombre = nombre
        self.estadistica = estadistica
        self.durabilidad = durabilidad
        self.maestria = maestria

    def desgaste(self):
        maestria = self.obt_maestria()
        if maestria.no_romper() >= random.random():
            self.durabilidad =- 1 
    
    def rotura(self):
        if self.durabilidad <= 0:
            print(f"{self.nombre} se ha roto")
            self.estadistica = 0

    def obt_maestria(self):
        return maestria.maestria(self.maestria_n)

    def caracteristicas(self):
 #       maestria = self.obt_maestria()
#        nombre = maestria.da_nombre()
        return print(f"{self.nombre}: {self.estadistica} de daño, maestria {self.maestria.da_nombre()}")

#tipos de daño 
class Cortante(Arma):
    def __init__(self, nombre, estadistica, durabilidad, maestria_n):
        super().__init__(nombre,estadistica, durabilidad, maestria_n)

    def calculo_daño(self, portador):
        return (self.estadistica + portador.fuerza)

class Contundente(Arma):
    def __init__(self, nombre, estadistica, durabilidad, maestria_n):
        super().__init__(nombre,estadistica, durabilidad, maestria_n)

    def calculo_daño(self, portador):
        return self.estadistica * portador.fuerza

class Punzante(Arma):
    def __init__(self, nombre, estadistica, durabilidad, maestria_n):
        super().__init__(nombre,estadistica, durabilidad, maestria_n)

    def calculo_daño(self, portador):
        return self.estadistica + int(portador.fuerza/2) + (2*(portador.agilidad))

class Magico(Arma):
    def __init__(self, nombre, estadistica, durabilidad, maestria_n):
        super().__init__(nombre,estadistica, durabilidad, maestria_n)

    def calculo_daño(self, portador):
        return self.estadistica + portador.inteligencia

espadachin = maestria.maestria("Espadachin", nivel = 1)
Esp = Cortante("Espada de hierro", 5, 100, espadachin)
Esp.caracteristicas()