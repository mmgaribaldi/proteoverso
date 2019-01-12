import sys
import json
import math

# Handler para la lectura
handle = open(str(sys.argv[1]),"r")

i=0
for line in handle:
    inicio = line.find(":")
    st = line[inicio+1:len(line)]
    if i == 0:
        largo=st.rstrip()
    if i == 1:
        largop=st.rstrip()
    if i == 2:
        secuenciasg=st.rstrip()
    if i == 3:
        secuencias=st.rstrip()
    if i == 4:
        secuenciase=st.rstrip()
    if i == 5:
        aminoacidos=st.rstrip()
    if i == 6:
        secuenciasp=st.rstrip()
    i = i+1

with open(str(str(sys.argv[1]))+'result.json', 'w') as fp:

	released = {
	    "id" : str(sys.argv[1]),
	    "largo" : largo,
	    "largo procesado" : largop,
        "secuencias eliminadas" : secuenciasg,
	    "secuencias" : secuencias,
	    "secuencias efectivas" : secuenciase,
	    "aminoacidos posibles" : aminoacidos,
	    "secuencias posibles" : secuenciasp
	    }
	json.dump(released, fp)

handle.close();