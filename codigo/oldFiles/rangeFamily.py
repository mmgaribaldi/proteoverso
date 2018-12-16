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
procesados = open("../secuencias/henikoff.dat", "r")
flias = procesados.readlines()
flias = list(map(int, flias))
procesados.close()

# Leo los que ya descargue
descargadas = open("../secuencias/descargadas.dat", "r")
flias_d = descargadas.readlines()
flias_d = list(map(int, flias_d))
descargadas.close()

for i in range(2,total_families):
    if i in flias:
        if i not in flias_d:

            id = 'PF' + '%0*d' % (5, i)

            try:
                file = fetchPfamMSA(id, compressed=False, gaps=None, format='fasta', timeout=300)
                shutil.move(file, '../control/' + file)

            except Exception as error:
                print("Aca tenes la exception gato")  # .format(error.getcode()))
    else:
        print("Familia" + str(i) +" no procesada!")

