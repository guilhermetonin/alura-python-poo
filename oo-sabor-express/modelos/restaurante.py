from modelos.avaliacao import Avaliacao

class Restaurante:
  '''
  Representa um restaurante e suas características.
  
  Atributos:
  - _nome (str): O nome do restaurante.
  - _tipo (str): O tipo do restaurante.
  - _ativo (bool): O estado do restaurante (False por padrão).
  - _avaliacao (list): Uma lista que contém o nome e a nota de cada avaliação.
  '''
  restaurantes = []

  def __init__(self, nome, tipo):
    '''
    Inicializa uma instância de Restaurante.

    Parâmetros:
    - nome (str): O nome do restaurante.
    - tipo (str): O tipo do restaurante.
    '''
    self._nome = nome.title() # primeire letra maiuscula
    self._tipo = tipo.title()
    # atributo protegido
    self._ativo = False
    self._avaliacao = []
    Restaurante.restaurantes.append(self)

  def __str__(self):
    '''Retorna uma representação em string formatada do restaurante'''
    return f'{self._nome} | {self._tipo}'
  
  @classmethod
  def listar_restaurantes(cls):
    '''Exibe uma lista formatada de todos os restaurantes cadastrados.'''
    print(f'{'NOME DO RESTAURANTE'.ljust(25)} | {'TIPO'.ljust(20)} | {'AVALIAÇÃO'.ljust(20)} | STATUS')

    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._tipo.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

  @property
  def ativo(self):
    '''Retorna um símbolo indicando o estado atual do restaurante.'''
    return '☑' if self._ativo else '☐'
    
  def altenar_estado(self):
    """Alterna o estado do restaurante."""
    self._ativo = not self._ativo
  
  def receber_avaliacao(self, cliente, nota):
    '''
    Registra uma avaliação para o restaurante.

    Parâmetros:
    - cliente (str): O nome do cliente da avaliação.
    - nota (float): A nota do restaurante (entre 1 e 5).
    '''
    if 0 <= nota <= 5:
      avaliacao = Avaliacao(cliente, nota)
      self._avaliacao.append(avaliacao)
      return
    print(f'A nota {nota} de avaliação está incorreta')

  @property
  def media_avaliacao(self):
    """Calcula e retorna a média das avaliações do restaurante."""
    if not self._avaliacao:
      return 'Sem avaliações'
    soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
    qtde_notas = len(self._avaliacao)
    media = round(soma_notas / qtde_notas, 1)
    return media