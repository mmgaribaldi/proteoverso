from Bio import SeqIO
from Bio.Seq import Seq

# Aminoacidos
aminoacidos = "ARNDCEQGHILKMFPSTWYV" # FIXME -sacar a archivo-

# Serializar aminoacidos
def toAminoacido(x):
    return {
        'A': 0,
        'R': 1,
        'N': 2,
        'D': 3,
        'C': 4,
        'E': 5,
        'Q': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'L': 10,
        'K': 11,
        'M': 12,
        'F': 13,
        'P': 14,
        'S': 15,
        'T': 16,
        'W': 17,
        'Y': 18,
        'V': 19,
    }[x]

# Aminoacidos distintos por posicion del alineamiento
def aminoacidosDistintos(pesos, posicion):
    cantidad = 0
    for x in range(len(aminoacidos)):
        if pesos[x][posicion] is not 0:
            cantidad = cantidad + 1
    return cantidad

# Lectura de la familia
familia = list(SeqIO.parse("../secuencias/PF02958_no_gaps.fasta", "fasta"))  #FIXME -parametrizar a archivo-

# Largo del alineamiento
longitud = len(familia[1].seq)
print("Largo del alineamiento: " + str(longitud))
cantidadProteinas = len(familia)

# Creo la matriz para calcular los pesos
pesos = [[0 for x in range(longitud)] for y in range(len(aminoacidos))]

# Lleno la matriz
for proteina in familia:
    secuencia = proteina.seq
    secuenciaString = str(secuencia)
    for x in range(0, longitud):
        if secuenciaString[x] is not '-':
            pesos[toAminoacido(secuenciaString[x])][x] = pesos[toAminoacido(secuenciaString[x])][x] + 1

# Calculo los pesos
control = 0
for proteina in familia:
    pesoPosicion = 0
    total = 0
    secuencia = proteina.seq
    secuenciaString = str(secuencia)
    for x in range(0, longitud):
        if secuenciaString[x] is not '-':
            cantidad = pesos[toAminoacido(secuenciaString[x])][x]
            cantidadDistintos = aminoacidosDistintos(pesos,x)
            pesoPosicion = 1/(cantidadDistintos*cantidad)
            total = total + pesoPosicion
    totalNormalizado = total/longitud
    print("El total de la proteina: " + proteina.description  + "es: " + str(total))
    print("El total de la proteina: " + proteina.description  + "es: " + str(totalNormalizado) + "(normalizado)")

    control = control + totalNormalizado

print(control)