from .veiculo import Veiculo

class Carro(Veiculo):
  '''
  Representa um carro, que é um tipo de Veículo.
  Essa classe herda de Veiculo e adiciona o atributo da quantidade de portas.
  
  Atributos:
  - _marca (str): A marca da carro (herdado).
  - _modelo (str): O modelo do carro (herdado).
  - _ligado (bool): O estado de funcionamento (herdado).
  - _cor (str): A cor do carro.
  '''
  def __init__(self,marca,modelo,cor):
    '''
    Inicializa uma nova instância de Carro.

    Parâmetros:
    - marca (str): A marca da carro.
    - modelo (str): O modelo do carro.
    - cor (str): A cor do carro.
    '''
    super().__init__(marca,modelo)
    self._cor = cor
  
  def __str__(self):
    '''Retorna uma string formatada do carro e suas informações'''
    base = super().__str__()
    return f'{base} | Cor: {str(self._cor).ljust(18)} | Estado: {self.ligado}'
  
  def ligar_veiculo(self):
    """Altera o estado do veículo para ligado (True)"""
    self._ligado = True
