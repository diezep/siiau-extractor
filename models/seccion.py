from typing import List

from .horario import Horario
from .materia import Materia


class Seccion:
    def __init__(
        self,
        nrc :int = None,
        materia: Materia = Materia(),
        horarios: List[Horario] = [],
        maestros: List[str] = [],
        cupo: int = None,
    ):
        self.nrc = nrc
        self.materia = materia
        self.horarios = horarios
        self.cupo = cupo
        self.maestros = maestros

    def __str__(self) -> str:
        return f"{self.nrc}"
