from typing import List
from models.clasehorario import ClaseHorario


class Horario: 
  def __init__(self, horarios: List[ClaseHorario] = [], ciclo: int = 0) -> None:
      self.horarios = horarios
      self.ciclo = ciclo
  def __str__(self) -> str:
    return self.horarios