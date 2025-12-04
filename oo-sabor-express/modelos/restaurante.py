class Restaurante:
  restaurantes = []

  def __init__(self, nome, tipo):
    self.nome = nome
    self.tipo = tipo
    self.ativo = False
    Restaurante.restaurantes.append(self)

  # self - é a referência atual
  def __str__(self):
    return f'{self.nome} | {self.tipo}'
  
  # método para listar todos os restaurantes
  def listar_restaurantes():
    for restaurante in Restaurante.restaurantes:
      print(f'nome: {restaurante.nome} | tipo: {restaurante.tipo} | status: {restaurante.ativo}')
    
# dir() - atributos, métodos e propriedades de um objeto
# vars() - dicionário desses atributos e métodos

restaurante_praca = Restaurante('Praça', 'Italiana')
restaurante_duze = Restaurante('Duzé', 'Gourmet')

Restaurante.listar_restaurantes()