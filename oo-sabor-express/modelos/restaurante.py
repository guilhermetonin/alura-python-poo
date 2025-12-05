class Restaurante:
  restaurantes = []

  def __init__(self, nome, tipo):
    self._nome = nome.title() # primeire letra maiuscula
    self._tipo = tipo.title()
    # atributo protegido
    self._ativo = False
    Restaurante.restaurantes.append(self)

  # self é a referência atual
  def __str__(self):
    return f'{self._nome} | {self._tipo}'
  
  # método da classe para listar todos os restaurantes
  @classmethod
  def listar_restaurantes(cls):
    print(f'{'NOME DO RESTAURANTE'.ljust(25)} | {'TIPO'.ljust(20)} | STATUS')

    for restaurante in cls.restaurantes:
      print(f'{restaurante._nome.ljust(25)} | {restaurante._tipo.ljust(20)} | {restaurante.ativo}')

  # permite tranformar um método em atributo, podendo acessar sem os ()
  # habilitando o controle de lógica ou validação na leitura e escrita
  @property
  def ativo(self):
    return '☑' if self._ativo else '☐'
  
  def altenar_estado(self):
    self._ativo = not self._ativo
    
# dir() - atributos, métodos e propriedades de um objeto
# vars() - dicionário desses atributos e métodos

restaurante_praca = Restaurante('praça', 'italiana')
restaurante_praca.altenar_estado()
restaurante_duze = Restaurante('Duzé', 'Gourmet')

Restaurante.listar_restaurantes()