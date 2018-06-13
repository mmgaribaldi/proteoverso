import shutil
from prody import *
from matplotlib.pylab import *
import main
print("Contando cantidad de familias...")

total_families = 0
with open("../secuencias/Pfam-A.hmm.dat", "r", encoding="utf-8") as file:
    for line in file:
        if "AC" in line.strip():
            total_families = total_families + 1

print("Cantidad total de familias del archivo HMM: " + str(total_families))

print("Seleccionando una familia al azar... ")
num_family = randint(0, total_families)
print(str(num_family))

# Descargo y muevo al directorio de secuencias
#file = fetchPfamMSA('PF02958', compressed=False, format='fasta')
#shutil.move(file, '../secuencias/' + file)

#main.calcularPesos('../secuencias/'+file)
main.calcularPesos('PF02958_full.fasta')