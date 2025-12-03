# questão 1:
def checar_par_impar():
  numero = int(input('Informe um número: '))
  if numero % 2 == 0:
    print(f'O número {numero} é par')
  else:
    print(f'O número {numero} é ímpar')

# questão 2:
def verificar_idade():
  idade = int(input('Informe sua idade: '))
  if 0 <= idade <= 12:
    print('Você é criança')
  elif 13 <= idade <= 18:
    print('Você é adolescente')
  else:
    print('Você é adulto')

# questão 3:
def login_da_empresa():
  usuario_permitido = 'admin'
  senha_do_usuario = 'admin'

  usuario = input('Informe o nome de usuário: ')
  senha = input('Informe a senha: ')

  if usuario != usuario_permitido:
    print(f'O nome {usuario} não está cadastrado')
  elif senha != senha_do_usuario:
    print(f'Senha incorreta, tente novamente')
  else: 
    print('Seja bem vindo!')

# questão 4:
def plano_cartesiano():
  x = int(input('Informe a coordenada x: '))
  y = int(input('Informeoa coordenada y: '))

  # x e y maiores que 0
  if x > 0 and y > 0:
    print('Primeiro Quadrante')
  # x é menor que 0 e y é maior que 0
  elif x < 0 and y > 0:
    print('Segundo Quadrante')
  # x e y são menores que 0
  elif x < 0 and y < 0:
    print('Terceiro Quadrante')
  # x é maior que 0 e y menor que 0
  elif x > 0 and y < 0:
    print('Quarto Quadrante')
  # caso contrário
  else:
    print('O ponto está localizado no eixo ou origem')

def main():
  checar_par_impar() # Q1
  verificar_idade() # Q2
  login_da_empresa() # Q3
  plano_cartesiano() # Q4

if __name__ == '__main__':
  main()