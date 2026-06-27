from transporte import Transporte

class Caminhao(Transporte):
    def __init__(self, distancia):
        super().__init__(distancia, frete=0)
        self.fator = 1.20

    def calc_frete(self):
        if self.distancia >= 50:
            print(f"Frete de Caminhao em {self.distancia}km = R${self.distancia*self.fator}")
        else:
            print("Precisa no minimo 50km")