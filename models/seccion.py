from models.maestro import Maestro
from models.horario import Horario
from typing import List
from models.materia import Materia


class Seccion:
    def __init__(
        self,
        nrc :int = None,
        materia: Materia = Materia(),
        horarios: List[Horario] = [],
        maestros: List[Maestro] = [],
        cupo: int = None,
    ):
        self.nrc = nrc
        self.materia = materia
        self.horarios = horarios
        self.cupo = cupo
        self.maestros = maestros

    def __str__(self) -> str:
        return f"{self.nrc}"
