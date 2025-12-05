# class da conta bancaria
class ContaBancaria:
  '''
  Atributos:
  - _titular (str): o nome do títular da conta
  - _saldo (float): o saldo atual da conta
  - _status (bool): o estado da conta (ativada ou desativada)
  
  Propriedade:
  - status (str): retorna o status atual formatado com um símbolo (☑ ou ☐)
  '''

  def __init__(self, titular, saldo):
    '''
    Cria uma nova conta bancaria

    Parâmetros:
    - titular (str): o nome do titular, é formatado automaticamente
    - saldo (float): o saldo atual da conta
    '''
    self._titular = titular.title()
    self._saldo = saldo
    self._status = False
  
  def __str__(self):
    '''Retorna as informações sobre a conta formatada'''
    return f'Nome: {self._titular} | Saldo: R$ {self._saldo} | Status: {self.status}'

  @property
  def status(self):
    '''Formata o status para símbolos visuais'''
    return '☑' if self._status else '☐'

  def altenar_estado(self):
    '''
    Alterna o estado da conta, podendo ativar ou desativar
    Modifica o atributo 'self._status'
    '''
    self._status = not self._status
    
# cria novas contas bancarias
conta_vinicius = ContaBancaria('Vinicius', 2500)
conta_miguel = ContaBancaria('miguel', 1250)

conta_vinicius.altenar_estado() # alterna o estado atual, ativando a conta

# exibe as contas bancarias
print(conta_vinicius)
print(conta_miguel)

# class dos clientes do banco
class ClienteBanco:
  '''
  Adiciona e salva as informações de um novo cliente

  Atributos:
  - _nome_titular (str): o nome do cliente
  - _idade (int): a idade do cliente
  - _telefone (str): o telefone do cliente
  - clientes (list): lista que armazena todos os clientes cadastrados
  '''
  clientes = []

  def __init__(self, nome_titular, idade, telefone):
    '''
    Adiciona um cliente
    Parâmetros:
    - nome_titular (str): o nome titular da conta
    - idade (int): a idade do titular
    - telefone (str): o telefone do titular
    '''
    self._nome_titular = nome_titular.title()
    self._idade = idade
    self._telefone = telefone
    ClienteBanco.clientes.append(self)

  @classmethod
  def listar_clientes(cls):
    '''
    Método de Classe: 
    Exibe uma lista formatada de todos os clientes cadastrados
    '''
    print(f'\n{'NOME DO CLIENTE'.ljust(25)} | {'IDADE'.ljust(10)} | {'TELEFONE'}')

    for cliente in cls.clientes:
      print(f'{cliente._nome_titular.ljust(25)} | {str(cliente._idade).ljust(10)} | {cliente._telefone}')

# cadastra novos clientes
vinicius = ClienteBanco('vinicius fernandes', 22, '(16) 99984-8484')
miguel = ClienteBanco('Miguel leandrini', 25, '(16) 99972-9284')

# exibe todos os clientes
ClienteBanco.listar_clientes()