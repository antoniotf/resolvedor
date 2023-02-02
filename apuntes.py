class GrupoAnimal:
   x = 10

   def grupo(self) :
     self.x = self.x + 1
     print("Hasta ahora",self.x)

lista=[1,2,3,4]


lista[0] = "indice cero"
print(lista[0],lista[3])
lista[0]= GrupoAnimal()
lista.append(GrupoAnimal)



print(lista[0])
print(lista[0].x)
print(lista)