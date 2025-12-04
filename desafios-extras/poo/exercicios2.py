# questão 1
class Carro:
  def __init__(self, modelo, ano, cor):
    self.modelo = modelo
    self.ano = ano
    self.cor = cor

  def __str__(self):
    return f'modelo: {self.modelo} | ano: {self.ano} | cor: {self.cor}'

carro = Carro('fox', '2011', 'cinza')
# print(carro)

# questão 2
class Empresa:
  def __init__(self, nome, categoria, localizacao, numero_funcionarios):
    self.nome = nome
    self.categoria = categoria
    self.localizacao = localizacao
    self.numero_funcionarios = numero_funcionarios
    self.status = False
    
  def __str__(self):
    mensagem_status = 'ativado' if self.status else 'desativado'
    return (
      f'nome da empresa: {self.nome}\n'
      f'categoria: {self.categoria}\n'
      f'localização: {self.localizacao}\n'
      f'números de funcionários: {self.numero_funcionarios}\n'
      f'status: {mensagem_status}'
    )
  def alterar_status(self):
    self.status = not self.status
    mensagem_status = 'ativo' if self.status else 'desativada' 
    print(f'\nalterando status da empresa para {mensagem_status}')

empresa_tone = Empresa('t.one', 'tecnologia', 'franca', 22) # cria uma inst6ancia

print(empresa_tone) # exibe na tela
empresa_tone.alterar_status() # ativando
empresa_tone.alterar_status() # desativando