import os

restaurantes = [
  {
    'nome': 'Nonno Grill',
    'tipo': 'Rodízio',
    'ativo': False
  }, 
  {
    'nome': 'La Finestra',
    'tipo': 'Pizzaria',
    'ativo': True
  },
  {
    'nome': 'Duzé',
    'tipo': 'Hamburgueria',
    'ativo': False
  }
]

def exibir_nome_do_programa():
  '''Exibe o título principal na tela'''
  print("""
  ┏━━━┳━━━┳━━┓┏━━━┳━━━┓┏━━━┳━┓┏━┳━━━┳━━━┳━━━┳━━━┳━━━┓
  ┃┏━┓┃┏━┓┃┏┓┃┃┏━┓┃┏━┓┃┃┏━━┻┓┗┛┏┫┏━┓┃┏━┓┃┏━━┫┏━┓┃┏━┓┃
  ┃┗━━┫┃╋┃┃┗┛┗┫┃╋┃┃┗━┛┃┃┗━━┓┗┓┏┛┃┗━┛┃┗━┛┃┗━━┫┗━━┫┗━━┓
  ┗━━┓┃┗━┛┃┏━┓┃┃╋┃┃┏┓┏┛┃┏━━┛┏┛┗┓┃┏━━┫┏┓┏┫┏━━┻━━┓┣━━┓┃
  ┃┗━┛┃┏━┓┃┗━┛┃┗━┛┃┃┃┗┓┃┗━━┳┛┏┓┗┫┃╋╋┃┃┃┗┫┗━━┫┗━┛┃┗━┛┃
  ┗━━━┻┛╋┗┻━━━┻━━━┻┛┗━┛┗━━━┻━┛┗━┻┛╋╋┗┛┗━┻━━━┻━━━┻━━━┛
  """)

def exibir_opcoes():
  '''Exibe todas as opções disponíveis na tela'''
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Alterar estado do restaurante')
  print('4. Sair do programa\n')

def finalizar_app():
  '''Finaliza o programa e exibe um retorno na tela'''
  exibir_subtitulo('Encerrando o app')
  
def opcao_invalida():
  '''Avisa na tela sobre a entrada errada nas opções e retorna ao menu principal'''
  print('Opção escolhida é inválida\n')
  retornar_ao_menu()

def retornar_ao_menu():
  '''
  Recebe a entrada do usuário e retorna ao menu principal de opções
  Ao usuário enviar qualquer entrada é chamado a função 'main()' 
  '''
  input('\nDigite uma tecla para retornar ao menu ')
  main()

def exibir_subtitulo(texto):
  '''Limpa o console e exibe um subtítulo formatado na tela
  
  Argumentos:
  - texto (str): string a ser exibida como subtítulo
  '''
  os.system('cls')
  linha = '-' * (len(texto) + 4)
  print(linha)
  print(f'| {texto} |')
  print(linha, '\n')

def cadastrar_novo_restaurante():
  '''Essa função é responsável por cadastrar um novo restaurante
  
  Inputs: 
  - Nome do restaurante
  - Categoria

  Outputs:
  - Adiciona um novo restaurante à lista de restaurantes
  '''
  exibir_subtitulo('Cadastro de novos restaurantes')
  nome_restaurante = input('Nome do restaurante que deseja ser cadastrado: ')
  tipo = input(f'Categoria do {nome_restaurante}: ')
  novo_restaurante = {
    'nome': nome_restaurante,
    'tipo': tipo,
    'ativo': False 
  }

  restaurantes.append(novo_restaurante)
  print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')
  retornar_ao_menu()

def listar_restaurantes():
  '''Essa função é responsável em exibir na tela todos os restaurantes cadastrados'''
  exibir_subtitulo('Listar os restaurantes')
  print(f'{'NOME DO RESTAURANTE'.ljust(22)} | {'CATEGORIA'.ljust(20)} | {'STATUS'}')
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    tipo = restaurante['tipo']
    ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
    print(f'* {nome_restaurante.ljust(20)} | {tipo.ljust(20)} | {ativo}')
  
  retornar_ao_menu()

def alterar_estado_restaurante():
  '''Essa função é responsável em alterar o estado do restaurante
  
  Input: 
  - Nome do restaurante

  Output:
  - Alterna o estado do restaurante
  '''
  exibir_subtitulo('Alterando estado do restaurante')

  nome_restaurante = input('Nome do restaurente que deseja alterar o estado: ')
  restaurante_encontrado = False

  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurante['ativo'] = not restaurante['ativo']
      restaurante_encontrado = True
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
      print(mensagem)

  if not restaurante_encontrado:
    print('O restaurante não foi encontrado')

  retornar_ao_menu()

def escolher_opcoes():
  '''
  Recebe a entrada do usuário e direciona para a funcionalidade

  Input: 
  - Opção escolhida

  Output:
  - Chama a função correspondente
  '''
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
      case 1:
        cadastrar_novo_restaurante()
      case 2:
        listar_restaurantes()
      case 3:
        alterar_estado_restaurante()
      case 4:
        finalizar_app()
      case _:
        opcao_invalida()
  except:
    opcao_invalida()

def main():
  '''
  Ponto de entrada do programa
  - Limpa o console
  - Exibe o menu principal, permitindo a interação do usuário
  '''
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()

if __name__ == '__main__':
  main()