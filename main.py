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
    global listado_cromosomas
    global cadenaNivel
    global cromosoma
    cadenaNivel = list(level_1[0])
    cantidad_movimientos = 30
    cantidad_individuos_seleccionados = 1000
    listado_cromosomas =[]
    cromosoma =[]
    cromosoma.clear()
    for i in range (cantidad_individuos):
        for x in range (cantidad_movimientos):
            mov_aleatorio = random.randint(1,4)

            while estado_regilla.mover(mov_aleatorio) == False:
                mov_aleatorio = random.randint(1, 4)
            cromosoma.append(mov_aleatorio)
            #redibujar_pantalla()
        cromosoma.append(fitnessV2(cromosoma))
        listado_cromosomas.append(cromosoma.copy())
        cromosoma.clear()
        cadenaNivel = list(level_1[0])
        ultimo_fitness = 999
        mejor_fitness = 999
        if i % 10000 == 0:
            print("Creados ",i," individuos de ", cantidad_individuos, "(", i/cantidad_individuos *100 ,"%)")

        #print("individuos creados =", i)

    listado_cromosomas.sort(key=lambda l: l[cantidad_movimientos], reverse=False)
    del listado_cromosomas[cantidad_individuos_seleccionados:cantidad_individuos]
    print("Generación cero creada: cromosoma 0= ",listado_cromosomas[0])
    print("Generación cero creada: cromosoma 1= ", listado_cromosomas[1])
    print("Generación cero creada: cromosoma 9= ", listado_cromosomas[9])





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
        #redibujar_pantalla()
        estado_regilla.mover(x)
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



def mutaciones(): # Mutar todos los individuos y añadirlos al final de la lista.
    global listado_cromosomas
    global cadenaNivel
    cantidad_individuos_seleccionados = 1000
    cadenaNivel = list(level_1[0])
    cadenaGenes = []
    generacion_mutada =[]
    probabilidad_de_mutacion_para_esta_generacion = random.randint(1,99)
    for x in range(0, len(listado_cromosomas)):
        for i in range(len(listado_cromosomas[x]) - 1):
            if random.randint(0, 100) > probabilidad_de_mutacion_para_esta_generacion:  # gen muta x % probabilidades, incluso movimientos no validos.
                mutacion_aleatoria = random.randint(1,4)
                cadenaGenes.append(mutacion_aleatoria)
            else:
                cadenaGenes.append(listado_cromosomas[x][i])


        cadenaGenes.append(fitnessV2(cadenaGenes))
        generacion_mutada.append(cadenaGenes.copy())
        cadenaGenes.clear()
        campo_de_fitness = len(listado_cromosomas[0]) - 1
        cadenaNivel = list(level_1[0])
        ultimo_fitness = 999
        mejor_fitness = 999

    listado_cromosomas.extend(generacion_mutada.copy())
    listado_cromosomas.sort(key=lambda l: l[campo_de_fitness], reverse=False)
    del listado_cromosomas[cantidad_individuos_seleccionados:len(listado_cromosomas)]
    # del listado_generacion_1[10:x]








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

ejecuta_cromosoma([1, 1, 2, 1, 1, 4, 4, 3, 3, 4, 4, 1, 1, 4, 3, 1, 1, 1, 3, 1, 3, 3, 1, 1, 2, 1, 4, 4, 1])
#print("fintes para ese = ",fitnessV2([4, 1, 3, 3, 4, 4, 2, 1, 3, 3, 1, 4, 2, 2, 1]))

'''
primera_generacion(200000)

for x in range (10000):
    mutaciones()
    if x % 1000 == 0:
        #print ("despues de primera mutacion listado_cromosomas= ",listado_cromosomas)
        print(" cantidad indivicuos en  listado_cromosomas",  len(listado_cromosomas))
        print ("despues de", x," mutaciones cromosoma 0 = ", listado_cromosomas[0])
        print("despues de", x, " mutaciones cromosoma 1 = ", listado_cromosomas[1])
        print("despues de", x, " mutaciones cromosoma 2 = ", listado_cromosomas[2])
        print("despues de", x, " mutaciones cromosoma 9 = ", listado_cromosomas[9])
        print("despues de", x, " mutaciones cromosoma 18 = ", listado_cromosomas[18])
        print("despues de", x, " mutaciones cromosoma 100 = ", listado_cromosomas[100])
        print("despues de", x, " mutaciones cromosoma 500 = ", listado_cromosomas[500])
        print("despues de", x, " mutaciones cromosoma 900 = ", listado_cromosomas[900])



#print (len(listado_generacion_0)," se esperan 1500")



# fitness()



# prueba movimientos segun indice

for x in listado_generacion_0[0]:
    print (x)
    time.sleep(0.1)
    redibujar_pantalla()
    estado_regilla.mover(x)
print("FINALIZADO")
'''
print("FINALIZADO PROGRAMA")



mainloop()
