import random
import arma
import maestria
import time

class Criatura:
    def __init__(self, nombre, tipo, arma, exp, maestria):
        self.nombre = nombre
        self.tipo = tipo
        self.fuerza = 20 #random.randint(1, 20)
        self.inteligencia = random.randint(1, 20)
        self.defensa = random.randint(1, 20)
        self.despecial = random.randint(1, 20)
        self.salud = random.randint(10, 20) * 10
        self.agilidad = random.randint(1, 20)
        self.arma = arma
        self.exp = exp
        self.maestria = maestria

    def atacar(self, enemigo):
        if self.arma is not None:
            ataque_total = self.arma.calculo_daño(self)
        else:
            ataque_total = self.fuerza
        #Probabilidad de fallar
        if self.maestria.prop_golpe() >= random.random():
            self.dañoinfringido(enemigo, ataque_total)
            self.arma.desgaste()    
        else:
            print(f"{self.nombre} ha fallado.")
            time.sleep(1)

    def muere(self, enemigo):
        if enemigo.salud <= 0:
            print(f"{enemigo.nombre} ha muerto")
            self.maestria.ganar_exp(enemigo.exp)
            self.arma.caracteristicas()

    def dañoinfringido(self, enemigo, daño):

        #Probabilidad de critico
        if self.maestria.prop_crit() > random.random():
            daño = int(daño * self.maestria.multipli_crit())
            mensaje_critico = " golpe critico"
        else:
            mensaje_critico = ""

        #Calculo daño/defensa
        if int(daño) > int((enemigo.defensa)/2):
            dañoreal = daño - int((enemigo.defensa)/2)
            enemigo.salud = enemigo.salud - dañoreal
            print(f"{self.nombre} ha infrindo{mensaje_critico} {dañoreal} puntos de daño.")
            print(f"{enemigo.nombre} tiene {enemigo.salud} puntos de vida.")
            time.sleep(1)
            self.muere(enemigo)
        else:
            print(f"{enemigo.nombre} no ha sufrido daño.")
            time.sleep(1)

    def estadisticas(self):
        print(f"{self.nombre}, Raza: {self.tipo}, Ataque: {self.fuerza}, Inteligencia: {self.inteligencia}, "
              f"Defensa: {self.defensa}, Agilidad: {self.agilidad}, Salud: {self.salud}")
        if self.arma is not None:
            print(f"Arma: {self.arma.nombre}")

#Personajes
espadachin = maestria.maestria("Espadachin")
luchador = maestria.maestriaenemiga("Luchador")
Esp = arma.Cortante("Espada de hierro", 5, 100, espadachin)
combos = arma.Contundente("Combos", 1, 1000, luchador)
Gobito = Criatura("Gobito", "Goblin", Esp, 0, espadachin)
Babosa = Criatura("Babosa", "Babosa", combos, 2, luchador)
Gobito.estadisticas()
Babosa.estadisticas()

#Juego
while True:
   Gobito.atacar(Babosa)
   if Gobito.salud <= 0 or Babosa.salud <= 0:
       break  
   Babosa.atacar(Gobito)
   if Gobito.salud <= 0 or Babosa.salud <= 0:
       break  