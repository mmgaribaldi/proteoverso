import shutil
import main
import os

from prody import *
from matplotlib.pylab import *
from urllib.error import HTTPError

max_retry = 1

# Leo los que ya procese
procesados = open("../secuencias/gas.txt", "r")
flias = procesados.readlines()
flias = list(map(int, flias))
procesados.close()

for i in flias:
    if i<10:
        id="PF0000"+str(i)
    else:
        if i<100:
            id="PF000"+str(i)
        else:
            if i<1000:
                id="PF00"+str(i)
            else:
                if i<10000:
                    id="PF0"+str(i)
                else:
                    id="PF"+str(i)

        # Descargo y muevo al directorio de secuencias
        try:
            file = fetchPfamMSA(id, compressed=False, format='fasta', timeout=300)
            print(file)
            shutil.move(file, '../secuencias/' + file)
            main.calcularPesos('../secuencias/' + file)
        except Exception as error:
            print ("Aca tenes la exception gato") #.format(error.getcode()))
