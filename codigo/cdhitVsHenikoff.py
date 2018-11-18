import csv
import math

import numpy as np
import matplotlib.pyplot as plt

# Leo los cdhit a graficar
procesadosCdhit = open("../resultados/agraficar-cdhit.txt", "r")
flias = procesadosCdhit.readlines()

ejeX = np.zeros(len(flias))

for j, elem in enumerate(flias):

    with open('../resultados/' + str(elem).rstrip(), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in spamreader:
            if row[1] == '0.95':
                introw=math.log(float(row[3]),10)
                #introw = float(row[3])
                ejeX[j] = introw

print(ejeX)

# Leo los resultados a graficar
procesadosHeni = open("../resultados/agraficar-heni.txt", "r")
flias = procesadosHeni.readlines()

ejeY = np.zeros(len(flias))

for j, elem in enumerate(flias):

    with open('../resultados/' + str(elem).rstrip(), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')

        for row in spamreader:
            introw=math.log(float(row[4]),10)
            #introw = float(row[4])
            ejeY[j] = introw

print(ejeY)

plt.title('Cd-hit vs Henikoff: ')
plt.scatter(ejeX,ejeY)

plt.xlabel('Log(cd-hit con clusters al 95%)')
plt.ylabel('Log(Secuencias efectivas Henikoff')
plt.show()
