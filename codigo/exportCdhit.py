import sqlite3


def toFila(r):
    linea = str(r[0][0]) + "," + str(r[0][3]) + "," + str(r[1][3]) + "," + str(r[2][3]) + "," + str(r[3][3]) + "," + str(r[4][3]) + "," + str(r[5][3]) + "," + str(r[6][3]) + "," + str(r[7][3]) + "," + str(r[8][3]) + "," + str(r[9][3]) + "," + str(r[10][3]) + "," + str(r[11][3])
    return linea

# Abro archivos para exportar
procesados = open("../database/cdhit.txt", "w")


conn = sqlite3.connect('../database/proteoverso.db')
c = conn.cursor()


# Selecciono los que no estan chequeados
c.execute('''SELECT DISTINCT pfam_id FROM cdhit ;''')
rows = c.fetchall()

for row in rows:
    updateConn = sqlite3.connect('../database/proteoverso.db')
    updateCursor = updateConn.cursor()
    query = "SELECT pfam_id, cutoff , clusters, normalizedClusters FROM cdhit WHERE pfam_id = '" + str(row[0]) + "';"
    updateCursor.execute(query)
    r = updateCursor.fetchall()
    linea = toFila(r)
    procesados.write(linea + '\n')


procesados.close()

