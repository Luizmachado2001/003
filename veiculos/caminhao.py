from transporte import Transporte

class Caminhao(Transporte):
    def __init__(self, distancia):
        self.fator = 1.20


    def calc_frete(self):
        if self.distancia >= 50:
            print("frete permitido")
        else:
            print("Precisa no minimo 50km")