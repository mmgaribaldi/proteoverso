import csv
import math

import numpy as np
import matplotlib.pyplot as plt

# Leo los cdhit a graficar
procesadosCdhit = open("../resultados/agraficar-cdhit.text", "r")
flias = procesadosCdhit.readlines()

ejeYa = np.zeros(len(flias))

for j, elem in enumerate(flias):

    with open('../resultados/' + str(elem).rstrip(), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in spamreader:
            if row[1] == '0.95':
                introw=math.log(float(row[3]),10)
                #introw = float(row[3])
                ejeYa[j] = introw

# Leo los resultados a graficar
procesadosHeni = open("../resultados/agraficar-heni.text", "r")
flias = procesadosHeni.readlines()

ejeYb = np.zeros(len(flias))
ejeX = np.zeros(len(flias))

for j, elem in enumerate(flias):

    with open('../resultados/' + str(elem).rstrip(), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')

        for row in spamreader:
            introw=math.log(float(row[4]),10)
            introwX=math.log(float(row[3]),10)
            ejeX[j] = introwX
            ejeYb[j] = introw

for k in range(0, len(flias)):
    if ejeX[k]<ejeYa[k] or ejeX[k]<ejeYb[k]:
        print(k)

# plt.title('Log de secuencias vs Log Henikoff y Log CD-HIT: ')
# plt.scatter(ejeX,ejeYa,label="CD-HIT")
# plt.scatter(ejeX,ejeYb,label="Henikoff")
# plt.xlabel('Log(secuencias)')
# plt.ylabel('Log(Secuencias efectivas Henikoff & Log CD-HIT')
# plt.legend()
# plt.show()
