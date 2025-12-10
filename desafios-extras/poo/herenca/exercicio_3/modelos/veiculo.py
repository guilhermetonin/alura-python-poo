from abc import ABC, abstractmethod

class Veiculo(ABC):
  """
  Classe base que representa qualquer tipo de veículo.

  Atributos:
  - _marca (str): A marca do veículo.
  - _modelo (str): O modelo do veículo.
  - _ligado (bool): O estado  do veículo (True ou False).
  """

  def __init__(self,marca,modelo):
    """
    Inicializa uma nova instância de Veiculo.

    Parâmetros:
    - marca (str): A marca do veículo.
    - modelo (str): O modelo do veículo.
    """    
    self._marca = marca
    self._modelo = modelo
    self._ligado = False

  def __str__(self):
    """Retorna uma string formatada."""
    return f'Marca: {self._marca.ljust(15)} | Modelo: {self._modelo.ljust(15)} '

  @property
  def ligado(self):
    """Retorna o estado do veículo em símvolos (☑ ou ☒)."""
    return '☑' if self._ligado else '☒'
  
  @abstractmethod
  def ligar_veiculo(self):
    """Método abstrato que deve ser implementado por todas as classes filhas."""
    pass