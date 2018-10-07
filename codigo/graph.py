import csv
import numpy as np
import matplotlib.pyplot as plt


# Leo los resultados a graficar
procesados = open("../resultados/agraficar.txt", "r")
flias = procesados.readlines()

for j, elem in enumerate(flias):

    with open('../resultados/' + str(elem).rstrip(), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        i = 0
        x = np.zeros(11)
        y = np.zeros(11)
        for row in spamreader:
            x[i] = row[1]
            y[i] = row[4]
            i = i+1

        plt.title('Familia: ' + str(elem[8:-10]))
        plt.plot([x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10]], [y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9],y[10]])
        plt.xlabel('Valores de corte')
        plt.ylabel('# clusters normalizados')
        plt.savefig(str(elem) + ".png")
        plt.close()