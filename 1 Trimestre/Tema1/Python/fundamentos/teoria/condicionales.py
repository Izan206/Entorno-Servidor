lista1=[1,2,3] #la lista uno esta guardado en una referencia de memoria y la dos en otro
lista2= [1,2,3]
lista3=lista1
print(lista1 is lista3)

#El is solo se usa normalmente con el None
valor=22
print(valor is None) #Va a dar false
print(valor is not None) #Va a dar true

#AND -> and
#OR -> or
#NOT -> not

#IF
x=4
y=2
if (x>y):
    print(f"{x} es mayor que {y}")
    

a=4
b=0
print(x>=2 and b!=0 and (a/b)>1) #Da false y no error de compilacion porque en cuanto encuentra alguna condición falsa ya corta la ejecucion si pusiese b=0 seria verdadero entonces daria error de compilacion dado que llegaria a a/b>1 lo cual matematicamente da error


z=-1
if (z>0) :
    print(f"{x} es positivo")
elif(z==0):
    print(f"z es igual a 0")
else:
    print("z es negativo")
    
