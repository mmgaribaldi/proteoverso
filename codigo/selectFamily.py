import shutil
from prody import *
from matplotlib.pylab import *
import main
#print("Contando cantidad de familias...")

total_families = 0
with open("../secuencias/Pfam-A.hmm.dat", "r", encoding="utf-8") as file:
    for line in file:
        if "AC" in line.strip():
            total_families = total_families + 1

print("Cantidad total de familias del archivo HMM: " + str(total_families))

for i in range(0,9):
    num_family = randint(0, total_families)

    if num_family<10:
        id="PF0000"+str(num_family)
    if num_family<100:
        id="PF000"+str(num_family)
    if num_family<1000:
        id="PF00"+str(num_family)
    if num_family<10000:
        id="PF0"+str(num_family)
    else:
        id="PF"+str(num_family)

    # Descargo y muevo al directorio de secuencias
    file = fetchPfamMSA(id, compressed=False, format='fasta')
    shutil.move(file, '../secuencias/' + file)

    main.calcularPesos('../secuencias/'+file)
    #main.calcularPesos('PF02958_full.fasta')