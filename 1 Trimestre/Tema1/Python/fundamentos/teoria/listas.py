#Para copiar listas

lista=[1, 2, 3]
lista2=list(lista)

print(lista2)

#O importando copy
import copy
lista=[1, 2, 3]
lista2=copy.lista

#logica

listaA=[1, 2, 3, [1, 2]]
listaB=list(listaA)
lista[3][1]=99 #apunta a la referencia asi que sale 99 de no ser una lista habria salido el elemento original puesto que la modificacion va despues de la copia
print(listaA)

#Recorrer listas

for index, x in enumerate(listaA):
    print(f"Indice: {index}, valor: {x}")
    
#Concatenar listas
print(lista+lista2)

#ordenadr listas

t1=["a", "bb", "dddd", "ccc"]
t1.sort(len) #tambien se le pueden pasar funciones
print(t1)