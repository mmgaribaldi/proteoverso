import json
import math
from pprint import pprint

# Leo los que ya procese
procesados = open("../secuencias/procesadas.txt", "r")
flias = procesados.readlines()
flias = list(map(int, flias))
procesados.close()

for i in flias:
    if i<10:
        id="PF0000"+str(i)
    else:
        if i<100:
            id="PF000"+str(i)
        else:
            if i<1000:
                id="PF00"+str(i)
            else:
                if i<10000:
                    id="PF0"+str(i)
                else:
                    id="PF"+str(i)

    with open('../resultados/' + id + '_full.fasta_results.txtresult.json') as f:
        data = json.load(f)


    f=float(data["aminoacidos posibles"])
    f=math.log(f,10)

