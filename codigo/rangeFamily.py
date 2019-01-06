import shutil
import utils
import henikoff
import os

from prody import *
from matplotlib.pylab import *

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

# Leo los que ya procese
procesados = open("../secuencias/ya.dat", "r")
fliasya = procesados.readlines()
fliasya = list(map(int, fliasya))
procesados.close()


for i in range(2,total_families):
    if i in flias:
        if i not in fliasya:
            id = 'PF' + '%0*d' % (5, i)
            file = id + "_full.fasta.gz"
            path = "../../control/"
            shutil.copy(path + file, '../secuencias/' + file)
            command = "gzip -d " + '../secuencias/' + file
            os.system(command)
            file = file[:-3]
            henikoff.calcularPesos(file)
