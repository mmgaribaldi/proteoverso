import shutil
import main
import os

from prody import *
from matplotlib.pylab import *
from urllib.error import HTTPError

max_retry = 1

# Descargo y muevo al directorio de secuencias
try:
    file = fetchPfamMSA("PF12216", compressed=False, format='fasta', timeout=300)
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
    print ("Aca tenes la exception gato")
#try:
main.calcularPesos('../secuencias/'+file)
#except Exception as error:
#    print("No se puede descargar")
