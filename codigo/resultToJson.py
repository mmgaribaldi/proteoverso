import sys

# Handler para la escritura
handle = open(str(sys.argv[1])+"_full.fasta_results.txt","r")

i=0
for line in handle:
    inicio = line.find(":")
    st = line[inicio+1:len(line)]
    if i == 0:
        largo=st.rstrip()
    if i == 1:
        largop=st.rstrip()
    if i == 2:
        secuencias=st.rstrip()
    if i == 3:
        secuenciase=st.rstrip()
    if i == 4:
        aminoacidos=st.rstrip()
    if i == 5:
        secuenciasp=st.rstrip()
    i = i+1

released = {
    "id" : str(sys.argv[1]),
    "largo" : largo,
    "largo procesado" : largop,
    "secuencias" : secuencias,
    "secuencias efectivas" : secuenciase,
    "aminoacidos posibles" : aminoacidos,
    "secuencias posibles" : secuenciasp
    }


print(released);
handle.close();