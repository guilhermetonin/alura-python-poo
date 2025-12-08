from .veiculo import Veiculo

class Moto(Veiculo):
  '''
  Representa uma moto, que é um tipo de Veículo.
  Essa classe herda de Veiculo e adiciona o atributo da categoria.
  
  Atributos:
  - _marca (str): A marca da moto (herdado).
  - _modelo (str): O modelo da moto (herdado).
  - _ligado (bool): O estado de funcionamento (herdado).
  - _categoria (str): A categoria da moto (Esportiva ou Casual).
  '''
  def __init__(self,marca,modelo,categoria):
    '''
    Inicializa uma nova instância de Moto.

    Parâmetros:
    - marca (str): A marca da moto.
    - modelo (str): O modelo da moto.
    - categoria (str): A categoria da moto.
    '''
    super().__init__(marca,modelo)
    self._categoria = categoria

  def __str__(self):
    '''Retorna uma string formatada da moto e suas informações'''
    base = super().__str__()
    return f'{base} | Categoria: {self._categoria.ljust(15)} | Estado: {self.ligado}'