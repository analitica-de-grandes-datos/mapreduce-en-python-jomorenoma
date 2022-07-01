#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
 for line in sys.stdin:
  lista=line.split(',')
  sys.stdout.write("{},{}\n".format(lista[1].replace("\n",""),lista[0]))
