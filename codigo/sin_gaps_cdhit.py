import shutil
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
procesados = open("../secuencias/faltan.txt", "r")
flias = procesados.readlines()
procesados.close()

# Descargo y muevo al directorio de secuencias
for i, id in enumerate(flias):
    try:
        file = fetchPfamMSA(id, compressed=False, format='fasta', timeout=300, gaps=None)
        shutil.move(file, '../secuencias/' + file)
    except Exception as error:
        print ("Aca tenes la exception gato")

