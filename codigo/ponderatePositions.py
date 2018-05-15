from Bio import SeqIO
from Bio.Seq import Seq

# Aminoacidos
aminoacidos = "ARNDCEQGHILKMFPSTWYV" # FIXME -sacar a archivo-

# Lectura de la familia
familia = list(SeqIO.parse("PF02958_full_normalized.fasta", "fasta"))  #FIXME -parametrizar a archivo-

# Largo del alineamiento
longitud = len(familia[1].seq)
cantidadAlineamientos = len(familia)
print("Largo del alineamiento: " + str(longitud))
print("Cantidad de familias: " + str(cantidadAlineamientos))

# Array con cantidad de gaps
import numpy as np
cantidadGaps = np.zeros(longitud)

print("Contando gaps por posicion...")
for proteina in familia:
    secuencia = proteina.seq
    secuenciaString = str(secuencia)
    for i in range(0,longitud):
        if secuenciaString[i] is '-':
            cantidadGaps[i] = cantidadGaps[i]+1

# Recorro nuevamente para eliminar posiciones
for proteina in familia:
    secuencia = proteina.seq
    secuenciaString = str(secuencia)
    secuenciaLista = list(secuenciaString)
    for j in range(0,longitud):
        if ( (cantidadGaps[j]/cantidadAlineamientos) > 0.5 ): #FIXME -sacar como variable el porcentaje-
            secuenciaLista[j]='0'
    secuenciaString = "".join(secuenciaLista)
    secuenciaString = secuenciaString.replace('0','')

    secuenciaRepresentativa = Seq(secuenciaString)
    proteina.seq = secuenciaRepresentativa

# Handler para la escritura
handle = open("./PF02958_no_gaps.fasta","w")

# Escritura
SeqIO.write(familia,handle,"fasta")
