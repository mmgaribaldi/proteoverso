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

print(ejeYa)

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

print(ejeYb)

plt.title('Cd-hit vs Henikoff: ')
plt.scatter(ejeX,ejeYa)
plt.scatter(ejeX,ejeYb)
plt.xlabel('Log(cd-hit con clusters al 95%)')
plt.ylabel('Log(Secuencias efectivas Henikoff')
plt.show()
