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

        key,val = line.split(",")
        val = int(val)

        if key == curkey:
            #
            # No se ha cambiado de clave. Aca se acumulan los valores para la misma
            # clave.
            #
            salida.append(val)
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
                salida = sorted(salida)
                sys.stdout.write("{}\t".format(curkey))
                for i_field, field in enumerate(salida):
                 if i_field == len(salida)-1:
                  sys.stdout.write("{}\n".format(field))
                 else:
                  sys.stdout.write("{},".format(field))
                salida = []

            salida.append(val)
            curkey=key


    salida = sorted(salida)
    sys.stdout.write("{}\t".format(curkey))
    for i_field, field in enumerate(salida):
     if i_field == len(salida)-1:
      sys.stdout.write("{}\n".format(field))
     else:
      sys.stdout.write("{},".format(field))
