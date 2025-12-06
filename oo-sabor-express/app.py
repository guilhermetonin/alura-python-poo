from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'italiano')

restaurante_praca.receber_avaliacao('gui', 10)
restaurante_praca.receber_avaliacao('Laís', 5)
restaurante_praca.receber_avaliacao('Ana', 2)

# restaurante_duze = Restaurante('duzé', 'gourmet')
# restaurante_hugs = Restaurante('hugs', 'fast-food')

# restaurante_hugs.altenar_estado()

def main():
  Restaurante.listar_restaurantes()

if __name__ == '__main__':
  main()