import shutil
from Bio import SeqIO
from Bio.Seq import Seq
import os
import csv

from prody import *
from matplotlib.pylab import *
from urllib.error import HTTPError

max_retry = 1

# Leo los que ya procese
procesados = open("../secuencias/todos.txt.dat", "r")
flias = procesados.readlines()
procesados.close()

for id in flias:
    try:
        file = fetchPfamMSA(id.rstrip(), compressed=True, format='fasta', timeout=300)

        command = "gzip -d " + file
        os.system(command)
        file = file[:-3]

        shutil.move(file, '../control/' + file)

        # Lectura de la familia
        familia = list(SeqIO.parse("../control/" + file, "fasta"))
        longitud = len(familia[0].seq)

        heni = open("../resultados/" + id.rstrip() + "_full.fasta_results.txt.csv", "r")
        spamreader = csv.reader(heni, delimiter='|', quotechar='"')
        for row in spamreader:
            longitudHeni = int(row[1])

        if longitud == longitudHeni:
            print("Familia " + id.rstrip() + " OK")
        else:
            print(id.rstrip() + " NO OK")

    except Exception as error:
        print ("Aca tenes la exception gato") #.format(error.getcode()))
