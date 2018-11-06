import json

# Leo las familias
procesados = open("../secuencias/henikoff.txt", "r")
flias = procesados.readlines()
procesados.close()

for familia in flias:

    familia=familia.rstrip()
    familia='../resultados/'+familia

    with open(familia, 'r') as f:
        array = json.load(f)

    print (array)
