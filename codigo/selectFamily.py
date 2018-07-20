import shutil
import main
import os

from prody import *
from matplotlib.pylab import *
from urllib.error import HTTPError

max_retry = 5
total_families = 0
with open("../secuencias/Pfam-A.hmm.dat", "r", encoding="utf-8") as file:
    for line in file:
        if "AC" in line.strip():
            total_families = total_families + 1

print("Cantidad total de familias del archivo HMM: " + str(total_families))

for i in range(106,total_families):

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
        file = fetchPfamMSA(id, compressed=False, format='fasta', timeout=30)
        print(file)
        tryed=0
        while os.stat(file).st_size == 0 and tryed < max_retry:
            print("descarga fallida, reintentando...")
            try:
                file = fetchPfamMSA(id, compressed=False, format='fasta')
                tryed = tryed+1
            except ConnectionError:
                print("Error en el server...")
        shutil.move(file, '../secuencias/' + file)
    except Exception as error:
        print ("Aca tenes la exception gato") #.format(error.getcode()))
    try:
        main.calcularPesos('../secuencias/'+file)
    except Exception as error:
        print("No se puede descargar")
