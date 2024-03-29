import shutil
import os
import math
import sqlite3
from prody import *

# Definiciones de funciones


def download(mode, path, total):

    if mode == 1:
        for i in range(2, total):
            id = 'PF' + '%0*d' % (5, i)
            # Descargo y muevo al directorio de secuencias
            try:
                file = fetchPfamMSA(id, compressed=True, format='fasta', timeout=300)
                shutil.copy(file, '../control/' + file)
                command = "gzip -d " + file
                os.system(command)
                file = file[:-3]
                shutil.move(file, '../secuencias/' + file)
            except Exception as error:
                print ("No se pudo descargar!")
    if mode == 2:
        try:
            file = fetchPfamMSA(path, compressed=True, format='fasta', timeout=300)
            shutil.copy(file, '../control/' + file)
            command = "gzip -d " + file
            os.system(command)
            file = file[:-3]
            shutil.move(file, '../secuencias/' + file)
        except Exception as error:
            print("No se pudo descargar!")


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


# Des-Serializar aminoacidos
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
        exponentes=np.zeros(1)
        return exponentes


def checkFamily(values,db):
    if values[0] == db[0]:
        if str(values[1]) == str(db[2]):
            if str(values[2]) == str(db[3]):
                if str(values[3]) == str(db[4]):
                    if str(values[4]) == str(db[5]):
                        if str(values[5]) == str(db[6]):
                            if str(values[6]) == str(db[7]):
                                if str(values[7]) == str(db[8]):
                                    return True
    return False


def export(campo,condicion):
    # Abro el archivo para resultados
    results = open("../database/export.txt", "w")

    conn = sqlite3.connect('../database/proteoverso.db')

    c = conn.cursor()

    # armo la query
    query = "select * from henikoff where " + campo + " " + condicion + ";"

    # Selecciono los que no estan chequeados
    c.execute(query)
    rows = c.fetchall()

    for row in rows:
        results.write(str(row) + '\n')

    # Cierro el archivo
    results.close()

    # Cierro la conexion
    conn.close()