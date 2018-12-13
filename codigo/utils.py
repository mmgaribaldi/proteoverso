import shutil
import os

from prody import *
from matplotlib.pylab import *


def download(mode, path, total):

    if mode == 1:
        # Leo los que ya procese
        procesados = open(path, "r")
        flias = procesados.readlines()
        flias = list(map(int, flias))
        procesados.close()

        for i in range(2,total):
            if i in flias:
                print("Familia" + str(i) +" ya procesada!")
            else:

                id = 'PF' + '%0*d' % (5, i)

                # Descargo y muevo al directorio de secuencias
                try:
                    file = fetchPfamMSA(id, compressed=True, format='fasta', timeout=300)

                    shutil.copy(file, '../control/' + file)

                    command = "gzip -d " + file
                    os.system(command)
                    file = file[:-3]

                    print(file)
                    shutil.move(file, '../secuencias/' + file)
                    main.calcularPesos('../secuencias/'+file)

                    command = "echo " + id[2:10] + " >> ../" + path
                    os.system(command)

                except Exception as error:
                    print ("Aca tenes la exception gato") #.format(error.getcode()))
    if mode == 2:
        try:
            file = fetchPfamMSA(path, compressed=True, format='fasta', timeout=300)

            shutil.copy(file, '../control/' + file)

            command = "gzip -d " + file
            os.system(command)
            file = file[:-3]

            print(file)
            shutil.move(file, '../secuencias/' + file)
            main.calcularPesos('../secuencias/' + file)

            command = "echo " + id[2:10] + " >> ../" + path
            os.system(command)

        except Exception as error:
            print("Aca tenes la exception gato")  # .format(error.getcode()))

