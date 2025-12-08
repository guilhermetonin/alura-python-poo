'''Importa as classes necessárias e executa a lógica dentro da função main().'''
from modelos.veiculo import Veiculo
from modelos.carro import Carro
from modelos.moto import Moto

def main():
  '''
  Função principal e responsável por:
  - Criar e exibir três instâncias da classe Carro e da classe Moto.

  As instâncias mostram como os atributos de cada classe são criados:
  - qtde_portas (int) para Carro.
  - categoria (str) para Moto.
  Também a utilização do método __str__ que concatena as informações.
  '''
  
  # carros
  print(f'--- CARROS ---')
  carro1 = Carro('Chevrolet','Onix',4)
  carro2 = Carro('Hyundai','HB20',4)
  carro3 = Carro('Volkswagen','Fox',4)
  print(carro1)
  print(carro2)
  print(carro3)

  # motos
  print(f'\n--- MOTOS ---')
  moto1 = Moto('Honda','CG 160','Casual')
  moto2 = Moto('Yamaha','MT-03','Esportiva')
  moto3 = Moto('Honda','Bros 160','Casual')
  print(moto1)
  print(moto2)
  print(moto3)

if __name__ == '__main__':
  main()