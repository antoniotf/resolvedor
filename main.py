import random
import time
import turtle

from TablaNiveles import *
from turtle import *
cadenaNivel = list(level_1[0])

lapiz = turtle.Turtle()


class Estado_Regilla():
    def __init__(self):
        cadenaNivel = list(level_1[0])
    def actualizar(self):
        self.meta = int(cadenaNivel.index('E'))
        self.personaje = int(cadenaNivel.index('P'))
        self.casillaArriba = None
        self.casillaAbajo = None
        self.casillaDerecha = None
        self.casillaIzquierda = None
        self.casillaArribaSegunda = None
        self.casillaAbajoSegunda = None
        self.casillaDerechaSegunda = None
        self.casillaIzquierdaSegunda = None
        if (self.personaje -16) > -1:
            self.casillaArriba= cadenaNivel[self.personaje-16]
        if (self.personaje -32) > -1:
            self.casillaArribaSegunda= cadenaNivel[self.personaje-32]
        if (self.personaje + 16) < 177:
            self.casillaAbajo=  cadenaNivel[self.personaje+16]
        if (self.personaje + 32) < 177:
            self.casillaAbajoSegunda=  cadenaNivel[self.personaje+32]

        if (self.personaje + 1) < 177:
            self.casillaDerecha = cadenaNivel[self.personaje+1]
        if (self.personaje + 2) < 177:
            self.casillaDerechaSegunda = cadenaNivel[self.personaje+2]
        if (self.personaje - 1) > -1:
            self.casillaIzquierda = cadenaNivel[self.personaje - 1]
        if (self.personaje - 2) > -1:
            self.casillaIzquierdaSegunda = cadenaNivel[self.personaje - 2]

    def mover(self,direccion): # 1=arriba, 2=abajo, 3=derecha, 4=izq. devuelve True si se pudo mover - personaje o caja.
        self.direccion= direccion
        self.actualizar()
        if self.direccion == 1:
            if self.casillaArriba==' ':
                cadenaNivel[self.personaje] = ' '
                cadenaNivel[(self.personaje)-16] = 'P'
                self.actualizar()
                return True
            if (self.casillaArriba =='@') and (self.casillaArribaSegunda == ' '):
                cadenaNivel[(self.personaje) - 16] = ' '
                cadenaNivel[(self.personaje) - 32] = '@'
                self.actualizar()
                return True
            self.actualizar()
            return False

        if self.direccion == 2:
            if self.casillaAbajo==' ':
                cadenaNivel[self.personaje] = ' '
                cadenaNivel[(self.personaje)+16] = 'P'
                self.actualizar()
                return True
            if (self.casillaAbajo =='@') and (self.casillaAbajoSegunda == ' '):
                cadenaNivel[(self.personaje) + 16] = ' '
                cadenaNivel[(self.personaje) + 32] = '@'
                self.actualizar()
                return True
            self.actualizar()
            return False
        if self.direccion == 3:
            if self.casillaDerecha==' ':
                cadenaNivel[self.personaje] = ' '
                cadenaNivel[(self.personaje)+1] = 'P'
                self.actualizar()
                return True
            if (self.casillaDerecha =='@') and (self.casillaDerechaSegunda == ' '):
                cadenaNivel[(self.personaje) + 1] = ' '
                cadenaNivel[(self.personaje) + 2] = '@'
                self.actualizar()
                return True
            self.actualizar()
            return False

        if self.direccion == 4:
            if self.casillaIzquierda==' ':
                cadenaNivel[self.personaje] = ' '
                cadenaNivel[(self.personaje)-1] = 'P'
                self.actualizar()
                return True
            if (self.casillaIzquierda =='@') and (self.casillaIzquierdaSegunda == ' '):
                cadenaNivel[(self.personaje) - 1] = ' '
                cadenaNivel[(self.personaje) - 2] = '@'
                self.actualizar()
                return True
            self.actualizar()
            return False

def redibujar_pantalla():
    global cadenaNivel
    estado_regilla.actualizar()
    x = 0
    lapiz.penup()
    lapiz.shape('square')
    lapiz.speed(0)
    #turtle.tracer(n=0, delay=0)
    turtle.tracer(0)
    for col in range(16):
        for fil in range(11):
            lapiz.color('white')
            if cadenaNivel[(fil * 16 + col)] == 'X':
                lapiz.color("black")
            if cadenaNivel[(fil * 16 + col)] == 'E':
                lapiz.color("green")
            if cadenaNivel[(fil * 16 + col)] == 'P':
                lapiz.color("red")
            if cadenaNivel[(fil * 16 + col)] == '@':
                lapiz.color("blue")
            if cadenaNivel[(fil * 16 + col)] == 'R':
                lapiz.color("pink")

            lapiz.goto(col * 21, -fil * 21)
            lapiz.stamp()
    turtle.update()

def primera_generacion(cantidad_individuos):
    print("creando generacion cero con ", cantidad_individuos," individuos")
    global listado_generacion_0
    global cadenaNivel
    global cromosoma
    cadenaNivel = list(level_1[0])
    cantidad_movimientos = 17
    cantidad_individuos_seleccionados = 100
    listado_generacion_0 =[]
    cromosoma =[]
    cromosoma.clear()
    mejor_fitness = 999
    for i in range (cantidad_individuos):
        for x in range (cantidad_movimientos):
            mov_aleatorio = random.randint(1,4)
            while estado_regilla.mover(mov_aleatorio) == False:
                mov_aleatorio = random.randint(1, 4)
            cromosoma.append(mov_aleatorio)
            ultimo_fitness = fitness()
            if ultimo_fitness < mejor_fitness:
                mejor_fitness = ultimo_fitness
            #redibujar_pantalla()
        cromosoma.append(mejor_fitness)
        listado_generacion_0.append(cromosoma.copy())
        cromosoma.clear()
        cadenaNivel = list(level_1[0])
        ultimo_fitness = 999
        mejor_fitness = 999
        #print("individuos creados =", i)
    #cromosoma.clear()
    listado_generacion_0.sort(key=lambda l: l[cantidad_movimientos], reverse=False)
    del listado_generacion_0[cantidad_individuos_seleccionados:cantidad_individuos]
    print("Generación cero creada: cromosoma 0= ",listado_generacion_0[0])
    print("Generación cero creada: cromosoma 1= ", listado_generacion_0[1])
    print("Generación cero creada: cromosoma 1= ", listado_generacion_0[3])
    print("generación 0 completa :", listado_generacion_0)




def fitness():
    global cadenaNivel
    estado_regilla.actualizar()
    ycor_personaje = int(cadenaNivel.index('P')/16)
    xcor_personaje =cadenaNivel.index('P') - (ycor_personaje * 16)
    ycor_meta = int(cadenaNivel.index('E') / 16)
    xcor_meta = cadenaNivel.index('E') - (ycor_meta * 16)
    distanciaX = abs(xcor_personaje-xcor_meta)
    distanciaY = abs(ycor_personaje - ycor_meta)
    pasos_distancia = distanciaY+distanciaX
    if pasos_distancia == 1:
        while True:
            print (" RESUELTO !!!!!!!")
            print("cromosoma = ", cromosoma)
            ejecuta_cromosoma(cromosoma)
            print("Repite solucion en 10 segundos")
            ejecuta_cromosoma(cromosoma)
            print("Repite solucion en 10 segundos")
            ejecuta_cromosoma(cromosoma)
            print("Repite solucion en 10 segundos")
    if pasos_distancia == 0:
        print ("ENCONTRADO FITNESS = 0")

    return pasos_distancia

def fitnessV2(cromosoma): # ejecuta los movimientos y devuelve el maximo fitness
    global cadenaNivel
    cadenaNivel = list(level_1[0])
    mejor_fitness =999
    ultimo_fitness = 999
    for x in cromosoma:
        estado_regilla.actualizar()
        redibujar_pantalla()
        estado_regilla.mover(x)
        print("moviendo  = ",x)
        estado_regilla.actualizar()
        ycor_personaje = int(cadenaNivel.index('P')/16)
        xcor_personaje =cadenaNivel.index('P') - (ycor_personaje * 16)
        ycor_meta = int(cadenaNivel.index('E') / 16)
        xcor_meta = cadenaNivel.index('E') - (ycor_meta * 16)
        distanciaX = abs(xcor_personaje-xcor_meta)
        distanciaY = abs(ycor_personaje - ycor_meta)
        pasos_distancia = distanciaY+distanciaX
        ultimo_fitness = pasos_distancia
        if ultimo_fitness < mejor_fitness:
            mejor_fitness = ultimo_fitness
        if pasos_distancia == 1:
            while True:
                print (" RESUELTO !!!!!!!")
                print("cromosoma = ", cromosoma)
                ejecuta_cromosoma(cromosoma)
                print("Repite solucion en 10 segundos")
                ejecuta_cromosoma(cromosoma)
                print("Repite solucion en 10 segundos")
                ejecuta_cromosoma(cromosoma)
                print("Repite solucion en 10 segundos")
    if pasos_distancia == 0:
        print ("ENCONTRADO FITNESS = 0")

    return mejor_fitness

def ejecuta_cromosoma(cromosoma_pasado): # funcion para visualizar los movimientos de un cromosoma dado.
    global cadenaNivel
    cadenaNivel = list(level_1[0])
    for x in cromosoma_pasado:
        redibujar_pantalla()
        time.sleep(0.1)
        estado_regilla.mover(x)

def cruce_generacional():
    global listado_generacion_1
    global cadenaNivel
    cadenaNivel = list(level_1[0])
    listado_generacion_1 = []
    cadenaGenes=[]
    ultimo_fitnes =999
    mejor_fitnes =999
    print("Creando cruces de ", len(listado_generacion_0)," generaciones")
    for x in range(0, len(listado_generacion_0)-1, 2):
        print(x)
        for i in range(len(listado_generacion_0[x])-1):
            if random.randint(0,100)< 90: #gen el 50% del padre y 50% de la madre.
                cadenaGenes.append(listado_generacion_0[x][i])
                estado_regilla.mover(listado_generacion_0[x][i])
                estado_regilla.actualizar()
            else:
                cadenaGenes.append(listado_generacion_0[x+1][i])
                estado_regilla.mover(listado_generacion_0[x+1][i])
                estado_regilla.actualizar()
            ultimo_fitnes = fitness()
            print("ultimo_fitnes =",ultimo_fitnes)
            print("mejor_fitnes =", mejor_fitnes)
            if ultimo_fitnes < mejor_fitnes:
                mejor_fitnes = ultimo_fitnes
        print("campo de fitness = ", mejor_fitnes, " para individuo ", x)
        cadenaGenes.append(mejor_fitnes)
        print("padre =",listado_generacion_0[x])
        print("madre =", listado_generacion_0[x+1])
        print("hijo  =", cadenaGenes)
        listado_generacion_1.append(cadenaGenes.copy())
        cadenaGenes.clear()
        campo_de_fitness = len(listado_generacion_1[0])-1
        cadenaNivel = list(level_1[0])
        ultimo_fitness = 999
        mejor_fitness = 999
        print(" reseteo de fintes mejor y ultimo a ",mejor_fitness,ultimo_fitness)

    listado_generacion_1.sort(key=lambda l: l[campo_de_fitness], reverse=False)
    del listado_generacion_1[10:x]
    print("nueva generacion 1 ordenada =", listado_generacion_1)

    '''
    for x in listado_generacion_1:
        ejecuta_cromosoma(x)
        print("ejecutado cromosoma ", x," de ", len(listado_generacion_1))
        time.sleep(1)
    '''









estado_regilla = Estado_Regilla()

estado_regilla.actualizar()
print('arriba=', estado_regilla.casillaArriba)
print('abajo=',estado_regilla.casillaAbajo)
print('derecha',estado_regilla.casillaDerecha)
print('izquierda',estado_regilla.casillaIzquierda)
print("estado_regilla.personaje= ",estado_regilla.personaje)
print ("anterior est= ",cadenaNivel)
estado_regilla.actualizar()

print("nuevo estado =", cadenaNivel)

#redibujar_pantalla()

#ejecuta_cromosoma([1, 1, 3, 4, 1, 4, 3, 3, 4, 3, 3, 1, 3, 1, 1, 0])
#print("fintes para ese = ",fitnessV2([1, 1, 1, 4, 4, 1, 1, 1, 4, 1, 1, 3, 3, 1, 4, 3, 1, 2]))

primera_generacion(1000)
cruce_generacional()



# fitness()



# prueba movimientos segun indice
'''
for x in listado_generacion_0[0]:
    print (x)
    time.sleep(0.1)
    redibujar_pantalla()
    estado_regilla.mover(x)
print("FINALIZADO")
'''
print("FINALIZADO PROGRAMA")



mainloop()
