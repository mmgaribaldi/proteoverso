import utils
import henikoff

pfamid = 'PF15847'

utils.download(2,pfamid,18000)
val = henikoff.calcularPesos(pfamid + '_full.fasta')
print(val)
