import itertools
listado=[]
repeticiones = 10
for v in itertools.product([1,2,3,4], repeat=repeticiones):
    listado.append(v)

totalCombinaciones = len (listado)


