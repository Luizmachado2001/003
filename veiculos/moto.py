from transporte import Transporte

class Moto(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, frete=0)
        self.fator = 0.50

    def calc_frete(self):
        print(f"Frete de Moto em {self.distancia}km = R${self.distancia*self.fator}")
