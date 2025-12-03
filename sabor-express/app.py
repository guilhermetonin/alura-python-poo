import os

restaurantes = ['Nonno Grill', 'La Finestra']

def exibir_nome_do_programa():
  print("""
  ┏━━━┳━━━┳━━┓┏━━━┳━━━┓┏━━━┳━┓┏━┳━━━┳━━━┳━━━┳━━━┳━━━┓
  ┃┏━┓┃┏━┓┃┏┓┃┃┏━┓┃┏━┓┃┃┏━━┻┓┗┛┏┫┏━┓┃┏━┓┃┏━━┫┏━┓┃┏━┓┃
  ┃┗━━┫┃╋┃┃┗┛┗┫┃╋┃┃┗━┛┃┃┗━━┓┗┓┏┛┃┗━┛┃┗━┛┃┗━━┫┗━━┫┗━━┓
  ┗━━┓┃┗━┛┃┏━┓┃┃╋┃┃┏┓┏┛┃┏━━┛┏┛┗┓┃┏━━┫┏┓┏┫┏━━┻━━┓┣━━┓┃
  ┃┗━┛┃┏━┓┃┗━┛┃┗━┛┃┃┃┗┓┃┗━━┳┛┏┓┗┫┃╋╋┃┃┃┗┫┗━━┫┗━┛┃┗━┛┃
  ┗━━━┻┛╋┗┻━━━┻━━━┻┛┗━┛┗━━━┻━┛┗━┻┛╋╋┗┛┗━┻━━━┻━━━┻━━━┛
  """)

def exibir_opcoes():
  print('1. Cadastrar restaurante')
  print('2. Listar restaurante')
  print('3. Ativar restaurante')
  print('4. Sair do programa\n')

def finalizar_app():
  exibir_subtitulo('Encerrando o app')
  
def opcao_invalida():
  print('Opção escolhida é inválida\n')
  retornar_ao_menu()

def retornar_ao_menu():
  input('\nDigite uma tecla para retornar ao menu ')
  main()

def exibir_subtitulo(texto):
  os.system('cls')
  print(f'-- {texto} --\n')

def cadastrar_novo_restaurante():
  exibir_subtitulo('Cadastro de novos restaurantes')

  nome_restaurante = input('Nome do restaurante que deseja ser cadastrado: ')
  restaurantes.append(nome_restaurante)
  print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!')

  retornar_ao_menu()

def listar_restaurantes():
  exibir_subtitulo('Listar os restaurantes')

  for restaurante in restaurantes:
    print(f'. {restaurante}')
  
  retornar_ao_menu()

def escolher_opcoes():
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    match opcao_escolhida:
      case 1:
        cadastrar_novo_restaurante()
      case 2:
        listar_restaurantes()
      case 3:
        print('Ativar restaurante')
      case 4:
        finalizar_app()
      case _:
        opcao_invalida()
  except:
    opcao_invalida()

def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcoes()
  escolher_opcoes()

if __name__ == '__main__':
  main()