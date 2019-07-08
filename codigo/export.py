import sqlite3

# Abro el archivo para resultados
results = open("../database/export.txt", "w")

conn = sqlite3.connect('../database/proteoverso.db')

c = conn.cursor()

# Selecciono los que no estan chequeados
c.execute('''select * from henikoff where sequences >= 20;''')
rows = c.fetchall()

for row in rows:
    results.write(str(row) + '\n')


# Cierro el archivo
results.close()

# Cierro la conexion
conn.close()