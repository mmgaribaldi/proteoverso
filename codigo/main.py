import sqlite3
import henikoff
import utils
import os

conn = sqlite3.connect('../database/proteoverso.db')
c = conn.cursor()

# Selecciono los que no estan chequeados
c.execute('''select * from henikoff where checked = 'false';''')
rows = c.fetchall()

for row in rows:
    try:
        utils.download(2, row[0], 0)
        file = "../secuencias/" + str(row[0]) + "_full.fasta"
        res = henikoff.calcularPesos(file)
        res = res.split("|")

        if (utils.checkFamily(res,row)):
            updateConn = sqlite3.connect('../database/proteoverso.db')
            updateCursor = updateConn.cursor()
            query = "UPDATE henikoff SET checked = 'true' WHERE pfam_id = '" + str(row[0]) + "';"
            updateCursor.execute(query)
            updateConn.commit()
            print("Familia: " + row[0] + " OK")
            updateConn.close()
        else:
            print("Familia: " + row[0] + " Fallo el control!!! Actualizando los valores en la db...")
            print(row)
            print(res)
            updateConn = sqlite3.connect('../database/proteoverso.db')
            updateCursor = updateConn.cursor()
            query = "UPDATE henikoff " \
                        "SET checked = 'false', " \
                        "alignmentLong = " + str(res[1]) + ", " \
                        "alignmentLongProcessed = " + str(res[2]) + ", " \
                        "sequences = " + str(res[3]) + ", " \
                        "sequencesRemoved = " + str(res[4]) + ", " \
                        "effectiveSequences = " + str(res[5]) + ", " \
                        "posibleAA = " + str(res[6]) + ", " \
                        "possibleSequences = " + str(res[7]) + " " \
                    "WHERE pfam_id = '" + str(row[0]) + "';"

            print(query)
            updateCursor.execute(query)
            updateConn.commit()
            print("Familia: " + row[0] + " OK")
            updateConn.close()
        command = "rm -rf " + file
        os.system(command)
    except Exception as error:
        print("Aca tenes la exception gato")

# Cierro la conexion
conn.close()
