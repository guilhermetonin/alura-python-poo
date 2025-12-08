from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'italiano')
bebida_suco = Bebida('Suco de Uva', 5, 'Médio')
prato_pao = Prato('Pão Frânces', 2.50, 'Pãozinho quentinho')

def main():
  print(bebida_suco)
  print(prato_pao)

if __name__ == '__main__':
  main()