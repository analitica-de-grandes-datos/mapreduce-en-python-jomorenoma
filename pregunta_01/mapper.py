import sys
if __name__ == "__main__":
 for line in sys.stdin:
  lista = line.split(',')[2]
  sys.stdout.write("{}\t1\n".format(lista))
