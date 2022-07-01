#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

def replace_all(text,dic):
 for i,j in dic.items():
  text = text.replace(i,j)
 return text

if __name__ == "__main__":
 for line in sys.stdin:
  lista=line.split('   ')
  reemplazo = {"\t":"","\n":""}
  re = replace_all(lista[2],reemplazo)
  lista[2] = re
  sys.stdout.write("{},{}\n".format(lista[0],lista[2]))
