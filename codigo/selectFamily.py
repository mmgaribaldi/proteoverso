from random import randint

print("Contando cantidad de familias...")

total_families = 0
with open("Pfam-A.hmm.dat", "r", encoding="utf-8") as file:
    for line in file:
        if "AC" in line.strip():
            total_families = total_families + 1

print("Cantidad total de familias del archivo HMM: " + str(total_families))

print("Seleccionando una familia al azar... ")
num_family = randint(0, total_families)
print(str(num_family))
