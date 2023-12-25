import maestria
import random
import time
class Arma:
    def __init__(self, nombre, estadistica, durabilidad, maestria):
        self.nombre = nombre
        self.estadistica = estadistica
        self.durabilidad = durabilidad
        self.maestria = maestria

    def desgaste(self):
        if self.maestria.no_romper() >= random.random():
            self.durabilidad -= 1 
    
    def rotura(self):
        if self.durabilidad <= 0:
            print(f"{self.nombre} se ha roto")
            self.estadistica = 0

    def obt_maestria(self):
        return maestria.maestria(self.maestria)

    def caracteristicas(self):
        return print(f"{self.nombre}: {self.estadistica} de daño (durabilidad: {self.durabilidad}), maestria {self.maestria.da_nombre()}")

#tipos de daño 
class Cortante(Arma):
    #Se asocia a espadas, dagas, hachas
    def __init__(self, nombre, estadistica, durabilidad, maestria):
        super().__init__(nombre,estadistica, durabilidad, maestria)

    def calculo_daño(self, portador, enemigo):
        daño = self.estadistica + portador.fuerza + self.maestria.extra_dmg()
        for ataque in range(int(1 + self.maestria.velocidad_de_ataque() + (portador.agilidad/100))):
            #Prop de crit
            if self.maestria.prop_crit() > random.random() + (enemigo.agilidad/100):
                daño = int(daño * self.maestria.multipli_crit())
                mensaje_critico = " golpe critico"
            else:
                mensaje_critico = ""

            #Calculo daño/defensa
            if int(daño) > int((enemigo.defensa)/2):
                dañoreal = daño - int((enemigo.defensa)/2)
                enemigo.salud = enemigo.salud - dañoreal
                self.desgaste()
                print(f"{portador.nombre} ha infrindo{mensaje_critico} {dañoreal} puntos de daño.")
                print(f"{enemigo.nombre} tiene {enemigo.salud} puntos de vida.")
                time.sleep(1)
                portador.muere(enemigo)
                
            else:
                print(f"{enemigo.nombre} no ha sufrido daño.")
                time.sleep(1)

#        return (self.estadistica + portador.fuerza)

class Contundente(Arma):
    #Se asocia a mazos, baras, daños contundentes.
    def __init__(self, nombre, estadistica, durabilidad, maestria):
        super().__init__(nombre,estadistica, durabilidad, maestria)

    def calculo_daño(self, portador):
        return self.estadistica * portador.fuerza

class Punzante(Arma):
    #Se asocia a lanzas, flechas, etc.
    def __init__(self, nombre, estadistica, durabilidad, maestria):
        super().__init__(nombre,estadistica, durabilidad, maestria)

    def calculo_daño(self, portador):
        return self.estadistica + int(portador.fuerza/2) + (2*(portador.agilidad))

class Magico(Arma):
    def __init__(self, nombre, estadistica, durabilidad, maestria):
        super().__init__(nombre,estadistica, durabilidad, maestria)

    def calculo_daño(self, portador):
        return self.estadistica + portador.inteligencia
