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
  key,val=line.split('\t')
  val = val.split(',')
  reemplazo = {"\t":"","\n":""}
  re=replace_all(val[-1],reemplazo)
  val[-1] = re
  for i in val:
   sys.stdout.write("{},{}\n".format(i,key))
