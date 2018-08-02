import sys
import json
import math

# Handler para la lectura
handle = open(str(sys.argv[1]),"r")

indice=str(sys.argv[1]).find("P")
idd = str(sys.argv[1])[indice:indice+7]

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
        aa=float(aminoacidos)
        aa=math.log(aa,10)
    if i == 5:
        secuenciasp=st.rstrip()
    i = i+1

with open(str(str(sys.argv[1]))+'.csv', 'w') as fp:

    fp.write(idd + "|" + largo + "|" + largop+ "|" + secuencias+ "|" + secuenciase + "|" +str(aa) + "|" + secuenciasp)


#print(released);
handle.close();