#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':
 for line in sys.stdin:
  val, key = line.split(",")
  val = int(val)
  key = key.replace("\n","")
  sys.stdout.write("{},{}\n".format(key, val))
