from transporte import Transporte

class Drone(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, frete=0)
        self.fator = 9.50

    def calc_frete(self):
        if self.distancia > 10:
            print("passou do limite de 10km para drone")
        else:
            print(f"Frete de Drone em {self.distancia}km = R${self.distancia*self.fator}")