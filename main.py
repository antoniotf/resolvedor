import itertools
from TablaNiveles import *
listado=[]
repeticiones = 10
for v in itertools.product([1,2,3,4], repeat=repeticiones):
    listado.append(v)

totalCombinaciones = len (listado)


#Cargar laberinto en lista  (x, y, tipo)
gridJuego= [ [ 0 for i in range(16) ] for j in range(11) ]

gridJuego[1][3]=1



print (gridJuego)