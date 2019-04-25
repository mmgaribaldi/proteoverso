import sqlite3
import utils
import os

conn = sqlite3.connect('../database/proteoverso.db')

c = conn.cursor()

# Selecciono los que no estan chequeados
c.execute('''select * from henikoff where checked = 'true';''')
rows = c.fetchall()

for row in rows:
            updateConn = sqlite3.connect('../database/proteoverso.db')
            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.40, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.45, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.50, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.55, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.60, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.65, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.70, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.75, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.80, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.85, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.90, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            updateCursor = updateConn.cursor()
            query = "INSERT INTO cdhit(pfam_id, cutoff, pfam_id_num, sequences, clusters, normalizedClusters, observations)" \
                    " VALUES( " + "'" + str(row[0]) + "'" + ", 0.95, " + str(row[1]) + ", " + str(row[4]) + ", 0, 0, 'false');"

            updateCursor.execute(query)
            updateConn.commit()

            print("Familia: " + row[0] + " OK")
            updateConn.close()

# Cierro la conexion
conn.close()
