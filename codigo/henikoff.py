from Bio import SeqIO
from Bio.Seq import Seq
import math
import utils

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
    print("Cantidad de secuencias en la familia: " + str(cantidadAlineamientos))

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
            if ( (cantidadGaps[j]/cantidadAlineamientos) > 0.50 ): #FIXME -sacar como variable el porcentaje-
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

    # Handler para la escritura
    handle = open("../secuencias/"+family+"_no_gaps.fasta","w")

    # Escritura
    SeqIO.write(familiaSG, handle, "fasta")

    familia = familiaSG

    # Largo del alineamiento procesado
    longitud = len(familia[0].seq)
    print("Largo del alineamiento ya procesado: " + str(longitud))
    results.write("Largo del alineamiento ya procesado: " + str(longitud)+ "\n")
    print("Secuencias eliminadas por ser solo GAPS: " + str(eliminadas))
    results.write("Secuencias eliminadas por ser solo GAPS: " + str(eliminadas) + "\n")

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
                pesos[utils.toAminoacido(secuenciaString[x])][x] = pesos[utils.toAminoacido(secuenciaString[x])][x] + 1
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
                cantidad = pesos[utils.toAminoacido(secuenciaString[x])][x]
                cantidadDistintos = utils.aminoacidosDistintos(pesos,x,aminoacidos)
                pesoPosicion = 1/(cantidadDistintos*cantidad)
                total = total + pesoPosicion
        totalNormalizado = total/longitud

        pesosSecuencias[indice] = totalNormalizado
        indice = indice + 1

        if totalNormalizado > 0:
            hParcial = totalNormalizado * math.log(totalNormalizado) * -1
            h = h + hParcial
        control = control + totalNormalizado

    numeroEfectivo = math.exp(h)

    #print("Suma total (control, deberia ser 1): " + str(control))
    #print("El valor de H es: " + str(h))
    print("Cantidad de secuencias luego de procesar GAPS: " + str(cantidadAlineamientos-eliminadas))
    print("El numero efectivo de secuencias de esta familia es: " + str(int(numeroEfectivo)))
    results.write("Cantidad de secuencias luego de procesar GAPS: " + str(cantidadAlineamientos-eliminadas) + "\n")
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
                pesos[utils.toAminoacido(secuenciaString[x])][x] = pesos[utils.toAminoacido(secuenciaString[x])][x] + (pesosSecuencias[indice]*cantidadAlineamientos)
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

        posibles = posibles + math.log(aaj,10)

    print("Logaritmo de secuencias posibles segun alineamiento: " + str(posibles))
    results.write("Logaritmo de secuencias posibles segun alineamiento: " + str(posibles)+ "\n")

    exponentes = utils.calcularExponentes(longitud,10)
    secuenciasPosibles = 1
    for exponente in exponentes:
        secuenciasPosibles = secuenciasPosibles+math.log(math.pow(21,exponente),10)

    print("Logaritmo de secuencias posibles segun longitud: " + str(secuenciasPosibles))
    results.write("Logaritmo de secuencias posibles segun longitud: " + str(secuenciasPosibles)+ "\n")

    # Cierro el archivo con resultados
    results.close()
