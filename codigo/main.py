import henikoff
import utils


max_retry = 1
total_families = 0
with open("../secuencias/Pfam-A.hmm.dat", "r", encoding="utf-8") as file:
    for line in file:
        if "AC" in line.strip():
            total_families = total_families + 1

print("Cantidad total de familias del archivo HMM: " + str(total_families))

for i in range(2000, total_families):
    id = 'PF' + '%0*d' % (5, i)
    utils.downloadsingle(id)
