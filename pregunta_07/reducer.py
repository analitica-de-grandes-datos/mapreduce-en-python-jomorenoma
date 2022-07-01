#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator
#
# Esta funcion reduce los elementos que tienen la misma clave
#
if __name__ == '__main__':

    curkey = None
    salida = []
    #
    # cada linea de texto recibida es una entrada clave \tabulador valor
    #
    for line in sys.stdin:

        filas = line.split(",")
        filas[2] = int(filas[2])
        key = filas[0]

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            salida.append(filas)
        else:
            #
            # Se cambio de clave. Se reinicia el acumulador.
            #
            if curkey is not None:
                #
                # una vez se han reducido todos los elementos
                # con la misma clave se imprime el resultado en
                # el flujo de salida
                #
                salida = sorted (salida, key = operator.itemgetter(2))
                for i in salida:
                 sys.stdout.write("{}   {}   {}\n".format(i[0], i[1],str(i[2])))
                salida = []

            salida.append(filas)
            curkey=key


    salida = sorted (salida, key = operator.itemgetter(2))
    for j in salida:
     sys.stdout.write("{}   {}   {}\n".format(j[0], j[1], str(j[2])))
