class ClaseHorario:
  def __init__(self, inicio:int = None, fin:int = None, dia:int = None):
      self.inicio = inicio
      self.fin = fin
      self.dia = dia
  def __str__(self) -> str:
      return f"{self.inicio}-{self.fin} {self.dia}"