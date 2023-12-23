#La maestria de nivel permite mejorar tus habilidades con las armas

class maestria:
    def __init__(self, nombre, nivel = 1):
        self.nombre = nombre
        self.nivel = nivel
        self.exp = 0
        self.expnextlevel = 100

    def ganar_exp(self, cantidad):
        self.exp += cantidad
        print(f"Haz ganado {cantidad} puntos de experiencia.")
        if self.exp >= self.expnextlevel:
            self.nivel += 1
            self.exp = 0
            self.expnextlevel *= 2
            print(f"¡Haz alcanzado el nivel {self.nivel} en la maestria de {self.nombre}.")

    def da_nombre(self):
        return self.nombre

    def da_nivel(self):
        return self.nivel
    
    def da_exp(self):
        return self.exp

    def prop_golpe(self):
        return 0.7 + (0.02 * self.nivel)

    def extra_dmg(self):
        return self.nivel

    def velocidad_de_ataque(self):
        return 0.05 * self.nivel

    def multipli_crit(self):
        return 1.2 + (0.05 * self.nivel)

    def prop_crit(self):
        return 0.15 + (0.2 * self.nivel)

    def no_romper(self):
        return 0.1 + (0.02 * self.nivel)

class maestriaenemiga(maestria):
    def __init__(self, nombre, nivel = 1):
        super().__init__(nombre, nivel = 1)

    def ganar_exp(self, cantidad):
        return 