
def questao1():
  numeros_1_a_10 = list(range(1,11))
  print(numeros_1_a_10)

  nomes = input('Informe 4 nomes separados por virgula: ').split(',')
  print(nomes)

  anos = input('Informe o ano que nasceu e o ano atual: ').split(',')
  print(anos)

def questao2():
  numeros = list(range(0,21,5))
  for n in numeros:
    print(f'número: {n}')

def questao3():
  numeros = list(range(1,11))
  soma = 0
  print(f'números: {numeros}')
  for n in numeros:
    if n % 2 != 0:
      soma += n
  print(f'soma dos números ímpares: {soma}')

def questao4():
  numeros = list(range(1,11))
  for n in reversed(numeros):
    print(f'n: {n}')

def questao5():
  numero_escolhido = int(input('Informe um número: '))
  print(f'\nTabuada do {numero_escolhido}\n')
  for tabuada in range(1,11):
    print(f'{numero_escolhido} x {tabuada} = {numero_escolhido * tabuada}')

def questao6():
  lista = [10,20,30,None,40]
  soma = 0
  for n in lista:
    try:
      soma += n
    except:
      print(f'elemento inválido: {n}')

def questao7():
  # numeros = list(range(0,10))
  numeros = []
  media = 0
  for n in numeros:
    media =+ n
  
  try:
    media = media / len(numeros)
    print(f'média: {media}')
  except:
    print('lista está vazia')



questao7()