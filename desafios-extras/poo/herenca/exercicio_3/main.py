'''Importa as classes necessárias e executa a lógica dentro da função main().'''
from modelos.veiculo import Veiculo
from modelos.carro import Carro

def main():
  '''
  Função principal e responsável por:
  - Criar e exibir três instâncias
  - Demonstrar o método abstrato 'ligar_veiculo' herdado da classe 'Veiculo'

  As instâncias mostram como os atributos de cada classe são criados:
  - cor (str) para Carro.
  Também a utilização do método __str__ que concatena as informações.
  '''
  
  # carros
  print(f'--- CARROS ---')
  carro1 = Carro('Chevrolet','Onix','Preto')
  carro2 = Carro('Volkswagen','Fox','Cinza')
  carro3 = Carro('Volkswagen','Polo','Prata')

  # exibe
  print(carro1)
  print(carro2)
  print(carro3)

  # alterna o estado
  carro1.ligar_veiculo()
  print(carro1)

if __name__ == '__main__':
  main()