import shutil
import main
import os

from prody import *
from matplotlib.pylab import *

max_retry = 5
total_families = 0
with open("../secuencias/Pfam-A.hmm.dat", "r", encoding="utf-8") as file:
    for line in file:
        if "AC" in line.strip():
            total_families = total_families + 1

print("Cantidad total de familias del archivo HMM: " + str(total_families))

for i in range(2,total_families):

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
    file = fetchPfamMSA(id, compressed=False, format='fasta', timeout=600)
    print(file)
    tryed=0
    while os.stat(file).st_size == 0 and tryed < max_retry:
        print("descarga fallida, reintentando...")
        file = fetchPfamMSA(id, compressed=False, format='fasta')
        tryed = tryed+1

    shutil.move(file, '../secuencias/' + file)
    main.calcularPesos('../secuencias/'+file)
