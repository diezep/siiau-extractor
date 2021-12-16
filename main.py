from siiau import SIIAU
import sys
if __name__ == '__main__':
  materia = sys.argv[1]
  siiau = SIIAU("D", '202210')
  siiau.verOferta(materia)
    