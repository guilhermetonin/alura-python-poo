from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'italiano')
bebida_suco = Bebida('Suco de Uva', 5, 'Médio')
prato_pao = Prato('Pão Frânces', 2.50, 'Pãozinho quentinho')

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_pao)


def main():
  print(bebida_suco)
  print(prato_pao)
  restaurante_praca.exibir_cardapio

  bebida_suco.aplicar_desconto()
  prato_pao.aplicar_desconto()
  restaurante_praca.exibir_cardapio

if __name__ == '__main__':
  main()