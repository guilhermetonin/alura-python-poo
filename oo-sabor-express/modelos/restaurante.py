from modelos.avaliacao import Avaliacao

class Restaurante:
  restaurantes = []

  def __init__(self, nome, tipo):
    self._nome = nome.title() # primeire letra maiuscula
    self._tipo = tipo.title()
    # atributo protegido
    self._ativo = False
    self._avaliacao = []
    Restaurante.restaurantes.append(self)

  # self é a referência atual
  def __str__(self):
    return f'{self._nome} | {self._tipo}'
  
  # método da classe para listar todos os restaurantes
  @classmethod
  def listar_restaurantes(cls):
    print(f'{'NOME DO RESTAURANTE'.ljust(25)} | {'TIPO'.ljust(20)} | {'AVALIAÇÃO'.ljust(20)} | STATUS')

    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._tipo.ljust(20)} | {str(restaurante.media_avaliacao).ljust(20)} | {restaurante.ativo}')

  @property
  def ativo(self):
    return '☑' if self._ativo else '☐'
    
  
  def altenar_estado(self):
    self._ativo = not self._ativo
  
  def receber_avaliacao(self, cliente, nota):
    avaliacao = Avaliacao(cliente, nota)
    self._avaliacao.append(avaliacao)

  @property
  def media_avaliacao(self):
    if not self._avaliacao:
      return 0
    soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
    qtde_notas = len(self._avaliacao)
    media = round(soma_notas / qtde_notas, 1)
    return media