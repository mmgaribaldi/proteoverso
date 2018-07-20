from Bio import SeqIO
from Bio.Seq import Seq
import math

##  Definiciones de funciones

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

# Des-Serializar(?) aminoacidos
def fromAminoacido(c):
    return {
        0: 'A',
        1: 'R',
        2: 'N',
        3: 'D',
        4: 'C',
        5: 'E',
        6: 'Q',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'L',
        11: 'K',
        12: 'M',
        13: 'F',
        14: 'P',
        15: 'S',
        16: 'T',
        17: 'W',
        18: 'Y',
        19: 'V',
        20: '-',
    }[c]

# Aminoacidos distintos por posicion del alineamiento
def aminoacidosDistintos(pesos, posicion, aminoacidos):
    cantidad = 0
    for x in range(len(aminoacidos)):
        if pesos[x][posicion] is not 0:
            cantidad = cantidad + 1
    return cantidad

def calcularExponentes(longitud,factor):
    import numpy as np
    if longitud > 10:
        exponentes = np.zeros(int(math.ceil(longitud/factor)))
        i = 0
        while (longitud > factor):
            longitud = longitud - factor
            exponentes[i] = factor
            i = i + 1
        exponentes[i] = longitud
        return exponentes
    else:
        exponentes=0
        return exponentes


def calcularPesos(family):

    # Aminoacidos
    aminoacidos = "ARNDCEQGHILKMFPSTWYV" # FIXME -sacar a archivo-

    # Lectura de la familia
    familia = list(SeqIO.parse("../secuencias/" + family, "fasta"))

    # Abro el archivo para resultados
    results = open("../secuencias/"+family+"_results.txt","w")

    # Largo del alineamiento
    longitud = len(familia[0].seq)
    print("Largo del alineamiento: " + str(longitud))
    results.write("Largo del alineamiento: " + str(longitud)+"\n")


    #print("Normalizando secuencia...")
    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        secuenciaString = secuenciaString.replace('.', '-')
        secuenciaString = secuenciaString.upper()

        # Reemplazo todo lo que no es aminoacido por A
        for x in range(0, longitud):
            if secuenciaString[x] is not '-':
                if secuenciaString[x] not in aminoacidos:
                    secuenciaString = secuenciaString.replace(secuenciaString[x] , 'A')


        secuenciaNormalizada = Seq(secuenciaString)
        proteina.seq = secuenciaNormalizada

    cantidadAlineamientos = len(familia)
    print("Cantidad de proteinas en la familia: " + str(cantidadAlineamientos))

    # Array con cantidad de gaps
    import numpy as np
    cantidadGaps = np.zeros(longitud)

    #print("Contando gaps por posicion...")
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
    handle = open("../secuencias/"+family+"_no_gaps.fasta","w")

    # Escritura
    SeqIO.write(familia,handle,"fasta")



    # Largo del alineamiento procesado
    longitud = len(familia[1].seq)
    print("Largo del alineamiento ya procesado: " + str(longitud))
    results.write("Largo del alineamiento ya procesado: " + str(longitud)+ "\n")
    cantidadProteinas = len(familia)

    # Creo la matriz para calcular los pesos
    pesos = [[0 for x in range(longitud)] for y in range(len(aminoacidos)+1)]

    # Creo un array para grabar los pesos
    pesosSecuencias = [ 0 for x in range(cantidadAlineamientos)]

    # Lleno la matriz
    #print("Llenando la matriz con fecuencias aminoacidicas...")
    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        for x in range(0, longitud):
            if secuenciaString[x] is not '-':
                pesos[toAminoacido(secuenciaString[x])][x] = pesos[toAminoacido(secuenciaString[x])][x] + 1
            else:
                pesos[20][x] = pesos[20][x] + 1 # sacar este hardcodeo de 20
    #print("Matriz completa... Comprobando suma de columnas...")

    # Calculo el numero efectivo de secuencias
    control = 0
    h = 0
    indice = 0
    for proteina in familia:
        pesoPosicion = 0
        total = 0
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        for x in range(0, longitud):
            if secuenciaString[x] is not '-':
                cantidad = pesos[toAminoacido(secuenciaString[x])][x]
                cantidadDistintos = aminoacidosDistintos(pesos,x,aminoacidos)
                pesoPosicion = 1/(cantidadDistintos*cantidad)
                total = total + pesoPosicion
        totalNormalizado = total/longitud

        pesosSecuencias[indice] = totalNormalizado
        indice = indice + 1

        hParcial = totalNormalizado * math.log(totalNormalizado) * -1
        h = h + hParcial
        control = control + totalNormalizado

    numeroEfectivo = math.exp(h)

    #print("Suma total (control, deberia ser 1): " + str(control))
    #print("El valor de H es: " + str(h))
    print("El numero total de proteinas de la familia es: " + str(cantidadProteinas))
    print("El numero efectivo de secuencias de esta familia es: " + str(int(numeroEfectivo)))
    results.write("El numero total de proteinas de la familia es: " + str(cantidadProteinas)+ "\n")
    results.write("El numero efectivo de secuencias de esta familia es: " + str(int(numeroEfectivo))+ "\n")

    ## Calculo el numero efectivo de aminoacidos

    # Vacio la matriz
    pesos = [[0 for x in range(longitud)] for y in range(len(aminoacidos)+1)]

    # Lleno la matriz con pesos ponderados
    indice = 0
    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        for x in range(0, longitud):
            p = secuenciaString[x]
            if secuenciaString[x] is not '-':
                pesos[toAminoacido(secuenciaString[x])][x] = pesos[toAminoacido(secuenciaString[x])][x] + (pesosSecuencias[indice]*cantidadAlineamientos)
            else:
                pesos[20][x] = pesos[20][x] + (pesosSecuencias[indice]*cantidadAlineamientos) # sacar este hardcodeo de 20
        indice = indice + 1

    posibles = 1

    for columna in range(0, longitud):
        hj=0
        for fila in range(0, 21):
            pj = pesos[fila][columna]/cantidadAlineamientos
            if pj != 0:
                hj = hj + (-1)*pj*math.log(pj)
        aaj = math.exp(hj)
        #print("En la posicion " + str(columna) + " hay " + str(aaj) + " aminoacidos representativos")

        posibles = posibles * aaj

    print("Aminoacidos positbles: " + str(posibles))
    results.write("Aminoacidos posibles: " + str(posibles)+ "\n")

    exponentes = calcularExponentes(longitud,10)
    secuenciasPosibles = 1
    for exponente in exponentes:
        secuenciasPosibles = secuenciasPosibles+math.log(math.pow(21,exponente),10)

    print("Secuencias posibles para este alineamiento(resultado expresado logaritmicamente en base 10): " + str(secuenciasPosibles))
    results.write("Secuencias posibles para este alineamiento(resultado expresado logaritmicamente en base 10): " + str(secuenciasPosibles)+ "\n")

    # Cierro el archivo con resultados
    results.close()
