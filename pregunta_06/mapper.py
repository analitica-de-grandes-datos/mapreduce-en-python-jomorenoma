#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
if __name__ == "__main__":
 for line in sys.stdin:
  lista1=line.split('   ')[0]
  lista2=line.split('   ')[2]
  sys.stdout.write("{},{}\n".format(lista1,lista2.replace("\n","")))
