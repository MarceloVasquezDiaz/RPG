import random
import arma
import maestria
import time

class Criatura:
    """
    Clase que representa un enemigo o jugador

    Atributos
    - nombre, raza, estadisticas, arma, exp, maestria
    - atacar
    - muerte
    - estadisticas
    - restaurar vida
    """
    def __init__(self, nombre, tipo, fuerza, inteligencia, defensa, despecial, salud, agilidad, arma, exp, maestria):
        """
        Iniciar una instancia de la Clase Criatura

        - nombre(str): El nombre del personaje
        - tipo(str(De momento)): La raza del personaje
        - fuerza(int): Valor entre 1-20
        - inteligencia(int): Valor entre 1-20
        - defensa(int): Valor entre 1-20
        - despecial(int): Valor entre 1-20
        - salud(int): Valor entre 1-20
        - agilidad(int): Valor entre 1-20
        - arma(obj): arma creada anteriormente
        - exp(int): valor de exp que da
        - maestria(obj): maestria creada anteriormente
        """
        self.nombre = nombre
        self.tipo = tipo
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.despecial = despecial
        self.salud = salud * 10
        self.saludact = self.salud
        self.agilidad = agilidad
        self.arma = arma
        self.exp = exp
        self.maestria = maestria

    def atacar(self, enemigo):
        """
        Lanza el ataque, tiene una probabilidad de fallar dependiendo de tu nivel y la agilidad del enemigo
        """
        #Probabilidad de fallar
        if self.maestria.prop_golpe() >= random.random():
            self.arma.calculo_daño(self, enemigo) 
        else:
            print(f"{self.nombre} ha fallado.")
            time.sleep(1)
 
    def muere(self, enemigo):
        """
        Muestra si haz muerto
        """
        if enemigo.saludact <= 0:
            print(f"{enemigo.nombre} ha muerto")
            self.maestria.ganar_exp(enemigo.exp)
            self.arma.caracteristicas()

    def estadisticas(self):
        """
        Muestra las estadisticas del personaje
        """
        print(f"{self.nombre}, Raza: {self.tipo}, Ataque: {self.fuerza}, Inteligencia: {self.inteligencia}, "
              f"Defensa: {self.defensa}, Agilidad: {self.agilidad}, Salud: {self.saludact}/{self.salud}")
        if self.arma is not None:
            print(f"Arma: {self.arma.nombre}")

    def restaurarsalud(self, cantidad):
        """
        Permite restaurar salud
        """
        self.saludact = min(self.salud, self.saludact + cantidad)
        print(f"La saluda actual es {self.saludact}")

#Ejemplo

'''maestria0 = maestria.Maestria("All for one", nivel = 0)
maestria5 = maestria.Maestria("All for one", nivel = 5)
maestria10 = maestria.Maestria("All for one", nivel = 10)
maestria20 = maestria.Maestria("All for one", nivel = 20)

espada_de_hierro = arma.Cortante("Espada de hierro", 5, 100, maestria5)
lanza_de_hierro = arma.Punzante("Lanza de hierro", 3, 100, maestria20)
mazo_de_hierro = arma.Contundente("Mazo de hierro", 2, 1000, maestria20)

luchador = maestria.Maestriaenemiga("Luchador")
combos = arma.Cortante("Combos", 1, 1000, luchador)

Gobito = Criatura("Gobito", "Goblin", 10, 10, 10, 10, 10, 20, espada_de_hierro, 0, maestria5)
Babosa = Criatura("Babosa", "Babosa", 10, 10, 10, 10, 10, 10, combos, 2, luchador)

Gobito.estadisticas()
Babosa.estadisticas()

#Juego
while True:
    Gobito.atacar(Babosa)
    if Gobito.saludact == 0 or Babosa.saludact == 0:
        break
    Babosa.atacar(Gobito)
    if Gobito.saludact == 0 or Babosa.saludact == 0:
        break'''