class Veiculo:
  def __init__(self,marca,modelo):
    self._marca = marca
    self._modelo = modelo
    self._ligado = False

  def __str__(self):
    return f'Marca: {self._marca.ljust(15)} | Modelo: {self._modelo.ljust(15)} '

  @property
  def ligado(self):
    return '☑' if self._ligado else '☒'