import sys
if __name__ == "__main__":
 for line in sys.stdin:
  lista=line.split(',')[3:5]
  sys.stdout.write("{},{}\n".format(lista[0],lista[1]))
