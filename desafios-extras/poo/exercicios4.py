class Livro:
  '''
  Adiciona um livro e suas informações

  Atributos:
  - livros_cadastrados (list): lista que contém todos os livros cadastrados
  - _titulo (str): O título do livro
  - _autor (str): O autor do livro
  - _ano_publicacao (int): O ano de publicação do livro
  - _disponivel (bool): Disponibilidade do livro (True por padrão)
  '''
  livros_cadastrados = []
  
  def __init__(self, titulo, autor, ano_publicacao):
    '''
    Adiciona um livro
    
    Parâmetros:
    - titulo (str): O título do livro
    - autor (str): O autor do livro
    - ano_publicacao (int): O ano de publicação do livro
    '''
    self._titulo = titulo.title()
    self._autor = autor.title()
    self._ano_publicacao = ano_publicacao
    self._disponivel = True
    Livro.livros_cadastrados.append(self)
    
  def __str__(self):
    '''Retorna as informações sobre a conta formatada'''
    return f'Título: {self._titulo} | Autor: {self._autor} | Ano de publicação: {self._ano_publicacao}'
  
  def emprestar_livro(self):
    '''
    Verifica e alterna o estado de disponibilidade do livro

    Se o livro estiver disponível é alternado para False
    Caso contrário, exibe uma mensagem indicando que não pode ser emprestado
    '''
    if self._disponivel: # true
      print('Livro está disponível para ser emprestado')
      self._disponivel = not self._disponivel 
    else:
      return print('Livro não está disponível')
  
  def verificar_disponibilidade(self, ano):
    '''
    Verifica e exibe os livros disponiveis publicados em um ano especifico, enviado pelo usuário

    Parâmetros:
    - ano (int): O ano de publicação a ser buscado

    Se estiver livros disponíveis no ano buscado, exibe o título e o autor de cada livro
    Caso contrário, exibe uma mensagem de que não tem livros para aquele ano
    '''
    print('\n--- VERIFICAR DISPONIBILIDADE ---')
    livros_disponiveis = []

    for livro in Livro.livros_cadastrados:
      if livro._disponivel and livro._ano_publicacao == ano:
        livros_disponiveis.append(livro)

    if len(livros_disponiveis) == 0:
      print('Não tem livros disponíveis nesse momento')
      return
    
    for livro in livros_disponiveis:
      print(livro)


# declara novos livros
livro_duna = Livro('Duna', 'Frank Herbert', 1965)
livro_lolita = Livro('Lolita', 'Vladimir Nabokov', 1965)
livro_dracula = Livro('Drácula', 'Bram Stoker', 1897)

# exibe o livro duna
print(livro_duna)

# alterna o estado do livro duna, sendo emprestado
livro_duna.emprestar_livro()

# verifica se há livros disponíveis neste ano
livro_duna.verificar_disponibilidade(1965)