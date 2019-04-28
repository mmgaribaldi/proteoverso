import sqlite3

conn = sqlite3.connect('../database/proteoverso.db')
c = conn.cursor()


# Selecciono cdhit
c.execute('''SELECT DISTINCT pfam_id FROM cdhit ;''')
rows_cdhit = c.fetchall()


# Selecciono cdhit
c.execute('''SELECT DISTINCT pfam_id FROM henikoff where alignmentLongProcessed > 20;''')
rows_henikoff = c.fetchall()

s = set(rows_cdhit).intersection(rows_henikoff)


print(s)