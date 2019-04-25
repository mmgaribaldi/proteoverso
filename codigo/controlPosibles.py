import sqlite3
import math

conn = sqlite3.connect('../database/proteoverso.db')

c = conn.cursor()

# Selecciono los que no estan chequeados
c.execute('''select * from henikoff;''')
rows = c.fetchall()

for row in rows:
    newP = row[3]*math.log(21,10)
    val2 = '%.3f' % (newP)
    val1 = '%.3f' % (row[8])
    val1 = float(val1)
    val2 = float(val2)
    val1 = val1 - 1
    if val1 != val2:
        print(row)
        print(str(val1) + " ->" + str(val2))


# Cierro la conexion
conn.close()
