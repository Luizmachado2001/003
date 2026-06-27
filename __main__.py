from veiculos.moto import Moto
from veiculos.caminhao import Caminhao
from veiculos.drone import Drone

def main():
    dis = 20
    
    veiculo_caminhao = Caminhao(dis)
    veiculo_caminhao.calc_frete()

if __name__ == "__main__":
    main()