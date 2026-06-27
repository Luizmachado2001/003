from transporte import Transporte
from veiculos import Caminhao, Moto, Drone

def main():

    dis = 80
    
    veiculo_caminhao = Caminhao(dis)
    veiculo_caminhao.calc_frete()

    veiculo_moto = Moto(20)
    veiculo_moto.calc_frete()

    veiculo_drone = Drone(5)
    veiculo_drone.calc_frete()

if __name__ == "__main__":
    main()