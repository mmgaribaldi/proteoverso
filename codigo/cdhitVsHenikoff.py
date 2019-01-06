import csv
import math

import numpy as np
import matplotlib.pyplot as plt

# Abro el archivo para resultados
resultsX = open("../secuencias/resultsX.txt", "w")
resultsY = open("../secuencias/resultsY.txt", "w")


# Leo los cdhit a graficar
procesadosCdhit = open("../secuencias/cdhit.dat", "r")
flias = procesadosCdhit.readlines()

ejeX = np.zeros(len(flias))

for j, elem in enumerate(flias):

    with open('../resultados/32.0/' + 'results_PF' + str(elem).rstrip() + '_full.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in spamreader:
            if row[1] == '0.95':
                introw=math.log(float(row[3]),10)
                #introw = float(row[3])
                ejeX[j] = introw
                resultsX.write(str(introw)+'\n')

print(ejeX)

# Leo los henikoff a graficar
procesadosHeni = open("../secuencias/henikoff.dat", "r")
flias = procesadosHeni.readlines()

ejeY = np.zeros(len(flias))

for j, elem in enumerate(flias):

    with open('../resultados/32.0/PF' + str(elem).rstrip() + '_full.fasta_results.txt.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter='|', quotechar='"')

        for row in spamreader:
            introw=math.log(float(row[4]),10)
            #introw = float(row[4])
            ejeY[j] = introw
            resultsY.write(str(introw)+'\n')

print(len(ejeY))
resultsX.close()
resultsY.close()


ejeXa = [0, 1, 2, 3, 4, 5]
ejeYa = [0, 1, 2, 3, 4, 5]


plt.title('Cd-hit vs Henikoff: ')
plt.scatter(ejeX,ejeY,s=1)
plt.scatter(ejeXa,ejeYa,label="Control",s=1)


plt.xlabel('Log(cd-hit con clusters al 95%)')
plt.ylabel('Log(Secuencias efectivas Henikoff')
plt.show()
