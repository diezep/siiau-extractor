import os
import time
from typing import List

import requests
from bs4 import BeautifulSoup

from .models.clasehorario import ClaseHorario
from .models.materia import Materia
from .models.seccion import Seccion


class SIIAU:
    def __init__(self, centro: str, ciclo: int, count: int = 10000) :
        self.centro = centro
        self.ciclo = ciclo
        self.count = count

    def materia(self, materia: str)-> List[Seccion]:
      req = requests.get(self.__generar_url(self.centro, self.ciclo, materia), verify=False) 
      soup = BeautifulSoup(req.content, 'html.parser')
      secciones : List[Seccion] = self.__formatSections(soup)
      return secciones
    
    def oferta(self, materia: str = '', mostrarp:int = 10000)-> List[Seccion]:
      req = requests.get(self.__generar_url(self.centro, self.ciclo, materia=materia, mostrarp=mostrarp), verify=False) 
      soup = BeautifulSoup(req.content, 'html.parser')
      self.secciones : List[Seccion] = self.__formatSections(soup)
      return self.secciones

    def __generar_url(self, centro: str, ciclo:str, materia: str = '', mostrarp:int = 10000)-> str:
      return f'http://consulta.siiau.udg.mx/wco/sspseca.consulta_oferta?ciclop={ciclo}&crsep={materia}&cup={centro}&mostrarp={mostrarp}'
      
    def __formatDay(self, text: str)-> List[int]:
      txt = text.replace('.', '').replace(' ', '')
      dias : List[int] = []
      for d in txt:
        if d == 'L':
          dias.append(1)
        elif d == 'M':
          dias.append(2)
        elif d == 'I':
          dias.append(3)
        elif d == 'J':
          dias.append(4)
        elif d == 'V':
          dias.append(5)
        elif d == 'S':
          dias.append(6)
      return dias
      
    def __formatSections(self, soup)-> List[Seccion]:
      seccionesElements = soup.select('tr[bgcolor="A9C0DB"] ~ tr')
      secciones : List[Seccion] = []
      for element in seccionesElements:
        claveMateria = element.select_one('td:nth-child(2)').text
        nombreMateria = element.select_one('td:nth-child(3) > a').text
        cupoSeccion = int(element.select_one('td:nth-child(7)').text)
        nrc = element.select_one('td:nth-child(1)').text
        maestroElement = element.select_one('td.tdprofesor:nth-child(2)')
        maestrx =  '' if maestroElement is None else maestroElement.text

        # Horario
        horariosElements = element.select('td:nth-child(8) > table > tr')
        claseHorarios: List[ClaseHorario] = []

        for element in horariosElements :
          claseHorario : ClaseHorario = ClaseHorario()
          horas = element.select_one('td:nth-child(2)').text.split('-')
          claseHorario.inicio = int(horas[0])
          claseHorario.fin = int(horas[1])
          diasStr = element.select_one('td:nth-child(3)').text
          dias = self.__formatDay(diasStr)
          for dia in dias:
            claseHorario.dia = dia
            claseHorarios.append(claseHorario)
        claseHorarios.sort(key=lambda x: x.inicio)
        secciones.append(Seccion(nrc, Materia(claveMateria, nombreMateria), claseHorarios, [maestrx], cupoSeccion))
      return secciones

    def agendar(cookies, nrc: str):
      pass
    
    def verOferta(self, materia: str, delay: int = 1, count: int = 3600):
      for i in range(count):
        oferta = self.oferta(materia)
        os.system('clear')
        print(f'Recarga no. {i}')
        for seccion in oferta: print(f"{seccion.nrc} | {seccion.materia.clave} | {seccion.cupo} |{seccion.maestros[0]}")
        time.sleep(delay)