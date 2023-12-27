class Inventario:

    def __init__(self, tamaño):
        self.tamaño = tamaño
        self.objetos = {}

    def agregar(self, objeto, cantidad):
        if objeto in self.objetos:
            self.objetos[objeto] += cantidad
        else:
            self.objetos[objeto] = cantidad

    def usar_obj(self, objeto, cantidad):
        if objeto in self.objetos:
            if self.objetos[objeto] >= cantidad:
                self.objetos[objeto] -= cantidad
                print(f"Has usado {cantidad} {objeto}(s).")
                if self.objetos[objeto] == 0:
                    del self.objetos[objeto]
            else:
                print(f"No tienes suficientes {objeto}(s) en el inventario.")
        else:
            print(f"No tienes {objeto}(s) en el inventario.")

    def mostrar_inv(self):
        print("Inventario")
        for objeto, cantidad in self.objetos.items():
            print(f"{objeto}: {cantidad}")
