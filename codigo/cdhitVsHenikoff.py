import csv
import math

import numpy as np
import matplotlib.pyplot as plt

# Leo los resultados a graficar
procesados = open("../resultados/agraficar.txt", "r")
flias = procesados.readlines()

ejeX = np.zeros(len(flias))

for j, elem in enumerate(flias):

    with open('../resultados/' + str(elem).rstrip(), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        for row in spamreader:
            if row[1] == '0.95':
                introw=math.log(float(row[3]),10)
                ejeX[j] = introw

print(ejeX)
