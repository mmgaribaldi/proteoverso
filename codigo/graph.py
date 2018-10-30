import csv
import numpy as np
import matplotlib.pyplot as plt

# Leo los resultados a graficar
procesados = open("../resultados/agraficar.txt", "r")
flias = procesados.readlines()

matriz = np.zeros(13)

for j, elem in enumerate(flias):

    with open('../resultados/' + str(elem).rstrip(), newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

        i = 0
        x = np.zeros(13)
        y = np.zeros(13)
        for row in spamreader:
            x[i] = row[1]
            y[i] = row[4]
            i = i+1
        x[12] = 1
        y[12] = 1
        matriz = np.vstack([matriz, y])

matriz = np.delete(matriz, 0,0)

promedio = np.zeros(13)
desviacion = np.zeros(13)

promedio[0]=np.mean(matriz[:,0])
promedio[1]=np.mean(matriz[:,1])
promedio[2]=np.mean(matriz[:,2])
promedio[3]=np.mean(matriz[:,3])
promedio[4]=np.mean(matriz[:,4])
promedio[5]=np.mean(matriz[:,11])
promedio[6]=np.mean(matriz[:,5])
promedio[7]=np.mean(matriz[:,6])
promedio[8]=np.mean(matriz[:,7])
promedio[9]=np.mean(matriz[:,8])
promedio[10]=np.mean(matriz[:,9])
promedio[11]=np.mean(matriz[:,10])
promedio[12]=np.mean(matriz[:,12])

desviacion[0]=np.std(matriz[:,0])
desviacion[1]=np.std(matriz[:,1])
desviacion[2]=np.std(matriz[:,2])
desviacion[3]=np.std(matriz[:,3])
desviacion[4]=np.std(matriz[:,4])
desviacion[5]=np.std(matriz[:,11])
desviacion[6]=np.std(matriz[:,5])
desviacion[7]=np.std(matriz[:,6])
desviacion[8]=np.std(matriz[:,7])
desviacion[9]=np.std(matriz[:,8])
desviacion[10]=np.std(matriz[:,9])
desviacion[11]=np.std(matriz[:,10])
desviacion[12]=np.std(matriz[:,12])

print(promedio)
print(desviacion)

plt.title('Familias: ')
plt.plot([x[0],x[1],x[2],x[3],x[4],x[11],x[5],x[6],x[7],x[8],x[9],x[10],x[12]], [promedio[0],promedio[1],promedio[2],promedio[3],promedio[4],promedio[5],promedio[6],promedio[7],promedio[8],promedio[9],promedio[10],promedio[11],promedio[12]])
plt.plot([x[0],x[1],x[2],x[3],x[4],x[11],x[5],x[6],x[7],x[8],x[9],x[10],x[12]], [desviacion[0],desviacion[1],desviacion[2],desviacion[3],desviacion[4],desviacion[5],desviacion[6],desviacion[7],desviacion[8],desviacion[9],desviacion[10],desviacion[11],desviacion[12]])

plt.xlabel('Valores de corte')
plt.ylabel('Promedios de clusters normalizados')
plt.show()
