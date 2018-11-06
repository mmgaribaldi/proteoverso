import json
import numpy as np
from numpy import array

# Leo las familias
procesados = open("../secuencias/henikoff.txt", "r")
flias = procesados.readlines()
procesados.close()
henikoff = []

for familia in flias:

    familia=familia.rstrip()
    familia='../resultados/'+familia

    with open(familia, 'r') as f:
        array = json.load(f)

        normalizado = int(array['secuencias efectivas'])/int(array['secuencias'])
        henikoff.append(normalizado)

np.array(henikoff)

promedio=np.mean(henikoff)
desvio=np.std(henikoff)

print(promedio)
print(desvio)