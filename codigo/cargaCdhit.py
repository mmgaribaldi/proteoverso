import sqlite3
import utils
import os

# Leo los que ya procese
procesados = open("../secuencias/cdhit.dat", "r")
flias = procesados.readlines()
procesados.close()

for flia in flias:
    flia = flia.rstrip()
    hits = open("../../32.0/results_" + flia + "_full.csv", "r")
    f = hits.readlines()
    hits.close()

    for fl in f:
        fl = fl.rstrip()
        fla = fl.split(",")

        updateConn = sqlite3.connect('../database/proteoverso.db')
        updateCursor = updateConn.cursor()

        query = "UPDATE cdhit " \
                "SET " \
                    "clusters = " + fla[3] + ", " \
                    "normalizedClusters = " + fla[4] + ", " \
                    "observations = 'imported' " \
                "WHERE pfam_id = '" + fla[0][0:7] + "' AND cutoff = '" + fla[1] + "';"

        updateCursor.execute(query)
        updateConn.commit()

        # Cierro la conexion
        updateConn.close()
