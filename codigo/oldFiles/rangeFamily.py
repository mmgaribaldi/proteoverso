import shutil
import main
import os

from prody import *
from matplotlib.pylab import *
from urllib.error import HTTPError

max_retry = 1
total_families = 0
with open("../secuencias/Pfam-A.hmm.dat", "r", encoding="utf-8") as file:
    for line in file:
        if "AC" in line.strip():
            total_families = total_families + 1

print("Cantidad total de familias del archivo HMM: " + str(total_families))

# Leo los que ya procese
procesados = open("../secuencias/procesadas.dat", "r")
flias = procesados.readlines()
flias = list(map(int, flias))
procesados.close()

for i in range(2,total_families):
    if i in flias:
        id = 'PF' + '%0*d' % (5, i)

        # Descargo y muevo al directorio de secuencias
        try:
            file = fetchPfamMSA(id, compressed=True, format='fasta', timeout=300)

            shutil.move(file, '../control/' + file)

        except Exception as error:
            print ("Aca tenes la exception gato") #.format(error.getcode()))
    else:
        print("Familia" + str(i) +" no procesada!")

