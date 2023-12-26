import random
import arma
import maestria
import time

class Criatura:
    def __init__(self, nombre, tipo, fuerza, inteligencia, defensa, despecial, salud, agilidad, arma, exp, maestria):
        self.nombre = nombre
        self.tipo = tipo
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.despecial = despecial
        self.salud = salud * 10
        self.agilidad = agilidad
        self.arma = arma
        self.exp = exp
        self.maestria = maestria

    def atacar(self, enemigo):
        #Probabilidad de fallar
        if self.maestria.prop_golpe() >= random.random():
            self.arma.calculo_daño(self, enemigo) 
        else:
            print(f"{self.nombre} ha fallado.")
            time.sleep(1)

    def muere(self, enemigo):
        if enemigo.salud <= 0:
            print(f"{enemigo.nombre} ha muerto")
            self.maestria.ganar_exp(enemigo.exp)
            self.arma.caracteristicas()

    def estadisticas(self):
        print(f"{self.nombre}, Raza: {self.tipo}, Ataque: {self.fuerza}, Inteligencia: {self.inteligencia}, "
              f"Defensa: {self.defensa}, Agilidad: {self.agilidad}, Salud: {self.salud}")
        if self.arma is not None:
            print(f"Arma: {self.arma.nombre}")



#Personajes

maestria0 = maestria.maestria("All for one", nivel = 0)
maestria5 = maestria.maestria("All for one", nivel = 5)
maestria10 = maestria.maestria("All for one", nivel = 10)
maestria20 = maestria.maestria("All for one", nivel = 20)

espada_de_hierro = arma.Cortante("Espada de hierro", 5, 100, maestria20)
lanza_de_hierro = arma.Punzante("Lanza de hierro", 3, 100, maestria20)
mazo_de_hierro = arma.Contundente("Mazo de hierro", 2, 1000, maestria20)

luchador = maestria.maestriaenemiga("Luchador")
combos = arma.Cortante("Combos", 1, 1000, luchador)

Gobito = Criatura("Gobito", "Goblin", 10, 10, 10, 10, 10, 20, mazo_de_hierro, 0, maestria20)
Babosa = Criatura("Babosa", "Babosa", 10, 10, 10, 10, 10, 10, combos, 2, luchador)

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
