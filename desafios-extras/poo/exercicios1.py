class Restaurante:
  nome = ''
  tipo = ''
  ativo = False

# cria um novo objeto
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'

# questão 1
restaurante_praca.tipo = 'Italiana'

# questão 2
print(f'nome do restaurante: {restaurante_praca.nome}')

# questão 3
mensagem = 'ativado' if restaurante_praca.ativo else 'desativado'
print(f'o restaurante está atualmente {mensagem}')

# questão 4
tipo = Restaurante.tipo
print(f'tipo: {tipo}') # vázio

# questão 5
restaurante_praca.nome = 'Bistrô'
print(f'novo nome do restaurante: {restaurante_praca.nome}')

# questão 6
restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'

# questão 7
restaurante_pizza.tipo = 'Fast Food'
print(f'o restaurante {restaurante_pizza.nome} é do tipo {restaurante_pizza.tipo}')

# questão 8
restaurante_pizza.ativo = not restaurante_pizza.ativo

# questão 9
mensagem = 'ativado' if restaurante_pizza.ativo else 'desativado'
print(f'o restaurante {restaurante_pizza.nome} está {mensagem}')

# questão 10
print(f'nome do restaurante: {restaurante_praca.nome}')
print(f'tipo do {restaurante_praca.nome}: {restaurante_praca.tipo}')


