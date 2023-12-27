import arma
import maestria
import criaturas
import random

luchador = maestria.Maestriaenemiga("Luchador")
combos = arma.Contundente("Combos", 1, 1000, luchador)
gusanoA = criaturas.Criatura("Gusano", "Insecto", 2, 2, 3, 1, 2, 3, combos, 2, luchador)
