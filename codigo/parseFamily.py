from Bio import SeqIO
from Bio.Seq import Seq

# Aminoacidos
aminoacidos = "ARNDCEQGHILKMFPSTWYV" # FIXME -sacar a archivo-

# Lectura de la familia
familia = list(SeqIO.parse("../secuencias/PF02958_full.fasta", "fasta"))  #FIXME -parametrizar a archivo-

# Largo del alineamiento
longitud = len(familia[1].seq)
print("Largo del alineamiento: " + str(longitud))

print("Normalizando secuencia...")
for proteina in familia:
    secuencia = proteina.seq
    secuenciaString = str(secuencia)
    secuenciaString = secuenciaString.replace('.', '-')
    secuenciaString = secuenciaString.upper()

    # Reemplazo todo lo que no es aminoacido por A
    for x in range(0, longitud):
        if secuenciaString[x] is not '-':
            if secuenciaString[x] not in aminoacidos:
                secuenciaString.replace(secuenciaString[x] , 'A')


    secuenciaNormalizada = Seq(secuenciaString)
    proteina.seq = secuenciaNormalizada

# Handler para la escritura
handle = open("../secuencias/PF02958_full_normalized.fasta","w")

# Escritura
SeqIO.write(familia,handle,"fasta")
