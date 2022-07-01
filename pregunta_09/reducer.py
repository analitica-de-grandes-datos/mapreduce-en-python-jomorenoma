#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    salida = []
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        filas = line.split(",")
        filas[2] = int(filas[2])
        salida.append(filas)

    salida = sorted (salida, key = operator.itemgetter(2))
    for i in salida[0:6]:
    	sys.stdout.write("{}   {}   {}\n".format(i[0], i[1],str(i[2])))
