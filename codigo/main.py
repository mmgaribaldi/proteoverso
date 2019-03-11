import sqlite3
import henikoff
import utils

conn = sqlite3.connect('../database/proteoverso.db')

c = conn.cursor()

# Selecciono los que no estan chequeados
c.execute('''select * from henikoff where checked = 'false';''')
rows = c.fetchall()

for row in rows:
    utils.download(2, row[0], 0)
    res = henikoff.calcularPesos("../secuencias/" + str(row[0]) + "_full.fasta")
    res = res.split("|")

    if (utils.checkFamily(res,row)):
        updateConn = sqlite3.connect('../database/proteoverso.db')
        updateCursor = updateConn.cursor()
        query = "UPDATE henikoff SET checked = 'true' WHERE pfam_id = '" + str(row[0]) + "';"
        print(query)
        updateCursor.execute(query)
        updateConn.commit()
        print("Familia: " + row[0] + " OK")
        updateConn.close()
    else:
        print("Familia: " + row[0] + " FAIL!!!")
        print(res)
        print(row)

# Cierro la conexion
conn.close()
