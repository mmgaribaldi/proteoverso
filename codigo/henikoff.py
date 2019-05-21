from Bio import SeqIO
from Bio.Seq import Seq
import math
import utils

AMINOACIDOS = "ARNDCEQGHILKMFPSTWYV"
GAP_POS = 20
GAP_RATE = 0.50


def calcularPesos(family):

    # Lectura de la familia
    familia = list(SeqIO.parse("../secuencias/" + family, "fasta"))

    # Largo del alineamiento
    longitud = len(familia[0].seq)

    #print("Normalizando secuencia...")
    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        secuenciaString = secuenciaString.replace('.', '-')
        secuenciaString = secuenciaString.upper()

        # Reemplazo lo que no es aminoacido por A
        for x in range(0, longitud):
            if secuenciaString[x] is not '-':
                if secuenciaString[x] not in AMINOACIDOS:
                    secuenciaString = secuenciaString.replace(secuenciaString[x], 'A')


        secuenciaNormalizada = Seq(secuenciaString)
        proteina.seq = secuenciaNormalizada

    cantidadAlineamientos = len(familia)

    # Array con cantidad de gaps
    import numpy as np
    cantidadGaps = np.zeros(longitud)

    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        for i in range(0,longitud):
            if secuenciaString[i] is '-':
                cantidadGaps[i] = cantidadGaps[i]+1

    # Contador para secuencias eliminadas por resultar todos GAPS con las posiciones eliminadas
    eliminadas = 0

    # Familia nueva para reescribir
    familiaSG = []
    # Recorro nuevamente para eliminar posiciones
    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        secuenciaLista = list(secuenciaString)
        for j in range(0,longitud):
            if cantidadGaps[j]/cantidadAlineamientos > GAP_RATE :
                secuenciaLista[j]='0'
        secuenciaString = "".join(secuenciaLista)
        secuenciaString = secuenciaString.replace('0','')

        if secuenciaString.count('-') != len(secuenciaString):
            secuenciaRepresentativa = Seq(secuenciaString)
            proteina.seq = secuenciaRepresentativa
            proteinaSG = proteina
            familiaSG.append(proteinaSG)
        else:
            eliminadas = eliminadas + 1

    # Comienzo a utilizar la familia sin GAPS
    familia = familiaSG

    # Largo del alineamiento procesado
    longitudp = len(familia[0].seq)

    # Creo la matriz para calcular los pesos
    pesos = [[0 for x in range(longitudp)] for y in range(len(AMINOACIDOS)+1)]

    # Creo un array para grabar los pesos
    pesosSecuencias = [ 0 for x in range(cantidadAlineamientos)]

    # Lleno la matriz
    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        for x in range(0, longitudp):
            if secuenciaString[x] is not '-':
                pesos[utils.toAminoacido(secuenciaString[x])][x] = \
                pesos[utils.toAminoacido(secuenciaString[x])][x] + 1
            else:
                pesos[GAP_POS][x] = pesos[GAP_POS][x] + 1

    # Calculo el numero efectivo de secuencias
    control = 0
    h = 0
    indice = 0
    for proteina in familia:
        pesoPosicion = 0
        total = 0
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        for x in range(0, longitudp):
            if secuenciaString[x] is not '-':
                cantidad = pesos[utils.toAminoacido(secuenciaString[x])][x]
                cantidadDistintos = utils.aminoacidosDistintos(pesos, x, AMINOACIDOS)
                pesoPosicion = 1/(cantidadDistintos*cantidad)
                total = total + pesoPosicion
        totalNormalizado = total/longitudp

        pesosSecuencias[indice] = totalNormalizado
        indice = indice + 1

        if totalNormalizado > 0:
            hParcial = totalNormalizado * math.log(totalNormalizado) * -1
            h = h + hParcial
        control = control + totalNormalizado

    numeroEfectivo = math.exp(h)

    # Secuencias sin las que son todos gaps
    secuenciassg = cantidadAlineamientos-eliminadas

    ## Calculo el numero efectivo de aminoacidos

    # Vacio la matriz
    pesos = [[0 for x in range(longitudp)] for y in range(len(AMINOACIDOS)+1)]

    # Lleno la matriz con pesos ponderados
    indice = 0
    for proteina in familia:
        secuencia = proteina.seq
        secuenciaString = str(secuencia)
        for x in range(0, longitudp):
            p = secuenciaString[x]
            if secuenciaString[x] is not '-':
                pesos[utils.toAminoacido(secuenciaString[x])][x] = \
                pesos[utils.toAminoacido(secuenciaString[x])][x] + \
                (pesosSecuencias[indice]*cantidadAlineamientos)
            else:
                pesos[GAP_POS][x] = pesos[GAP_POS][x] + (pesosSecuencias[indice]*cantidadAlineamientos)
        indice = indice + 1

    posibles = 1

    for columna in range(0, longitudp):
        hj=0
        for fila in range(0, 21):
            pj = pesos[fila][columna]/cantidadAlineamientos
            if pj != 0:
                hj = hj + (-1)*pj*math.log(pj)
        aaj = math.exp(hj)

        posibles = posibles + math.log(aaj,10)


    exponentes = utils.calcularExponentes(longitudp,10)
    secuenciasPosibles = 1
    for exponente in exponentes:
        secuenciasPosibles = secuenciasPosibles+math.log(math.pow(21,exponente),10)

    family = family[14:21]
    return str(family) + "|" + str(longitud) + "|" + str(longitudp) + "|" + str(secuenciassg) + "|" + \
           str(eliminadas) + "|" + str(int(numeroEfectivo)) + "|" + str(posibles) + \
           "|" + str(secuenciasPosibles)
