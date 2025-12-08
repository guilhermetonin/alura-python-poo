from .veiculo import Veiculo

class Carro(Veiculo):
  '''
  Representa um carro, que é um tipo de Veículo.
  Essa classe herda de Veiculo e adiciona o atributo da quantidade de portas.
  
  Atributos:
  - _marca (str): A marca da carro (herdado).
  - _modelo (str): O modelo do carro (herdado).
  - _ligado (bool): O estado de funcionamento (herdado).
  - _qtde_portas (int): A quantidade de portas que tem no carro.
  '''
  def __init__(self,marca,modelo,qtde_portas):
    '''
    Inicializa uma nova instância de Carro.

    Parâmetros:
    - marca (str): A marca da carro.
    - modelo (str): O modelo do carro.
    - qtde_portas (int): A quantidade de portas do carro.
    '''
    super().__init__(marca,modelo)
    self._qtde_portas = qtde_portas
  
  def __str__(self):
    '''Retorna uma string formatada do carro e suas informações'''
    base = super().__str__()
    return f'{base} | Portas: {str(self._qtde_portas).ljust(18)} | Estado: {self.ligado}'