pessoas = []

def cadastro_inicial():
  pessoas_cadastradas = [
    {
      'id': '1',
      'nome': 'Guilherme',
      'idade': 18,
      'cidade': 'Franca',
      'cargo': ''
    },
    {
      'id': '2',
      'nome': 'Gustavo',
      'idade': 22,
      'cidade': 'Batatais',
      'cargo': ''
    },
    {
      'id': '3',
      'nome': 'Gustavo',
      'idade': 16,
      'cidade': 'Franca',
      'cargo': ''
    },
  ]
  pessoas.extend(pessoas_cadastradas)

def exibir_titulo(texto):
  print(f'\n~~~{texto}~~~')

def listar_pessoas():
  exibir_titulo('LISTAR PESSOAS')
  print(f'{'NOMES'.ljust(15)} | {'IDADES'.ljust(10)} | {'CARGO'.ljust(10)} | {'CIDADES'}')
  for pessoa in pessoas:
    nome_pessoa = pessoa['nome']
    idade = pessoa['idade']
    cidade = pessoa['cidade']
    cargo = 'Não tem' if pessoa['cargo'] == '' else pessoa['cargo']
    print(f'{nome_pessoa.ljust(15)} | {str(idade).ljust(10)} | {cargo.ljust(10)} | {cidade}')

def atualizar_idade():
  exibir_titulo('IDADES ATUALIZADAS')
  for pessoa in pessoas:
    pessoa['idade'] += 1

def adicionar_profissao():
  exibir_titulo('ADICIONAR PROFISSÕES')
  for pessoa in pessoas:
    pessoa['cargo'] = input(f'Informe o cargo da pessoa: {pessoa['nome']}: ')

def buscar_pessoa():
  exibir_titulo('BUSCAR PESSOA')

  nome_pessoa = input('Qual o nome da pessoa que deseja procurar: ')
  pessoa_encontrada = False
  for pessoa in pessoas:
    if nome_pessoa == pessoa['nome']:
      print(f'Existe a pessoa {nome_pessoa} no sistema')
      pessoa_encontrada = True
  if not pessoa_encontrada:
    print('Não existe nenhuma pessoa com esse nome no sistema')

def buscar_chave():
  exibir_titulo('BUSCAR CHAVE')

  chave = input('Qual chave deseja procurar: ')
  chave_encontrada = False

  for pessoa in pessoas:
    if chave in pessoa:
      chave_encontrada = True
  if not chave_encontrada:
    print(f'A chave {chave} não existe')
  else:
    print(f'A chave {chave} existe')

def buscar_valor():
  exibir_titulo('BUSCAR VALOR')

  buscar = input('Qual valor deseja procurar: ')
  qtde = 0
  for pessoa in pessoas:
    for valor in pessoa.values():
      if buscar in str(valor):
        qtde += 1

  palavra_vez = f'vezes' if qtde >= 2 else 'vez'
  mensagem = f'O valor {buscar} não foi encontrado' if qtde == 0 else f'O valor {buscar} foi encontrado {qtde} {palavra_vez}'
  
  print(mensagem)

def main():
  cadastro_inicial()
  listar_pessoas()
  atualizar_idade()
  adicionar_profissao()
  listar_pessoas()
  buscar_pessoa()
  buscar_chave()
  buscar_valor()

if __name__ == '__main__':
  main()