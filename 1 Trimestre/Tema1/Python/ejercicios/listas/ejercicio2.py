lista1=[1, 2, 3, 4, 5]


def so_pares(lista):
    nuevaLista=[]
    for num in lista1:
        if (num%2==0):
            nuevaLista.append(num)
    return nuevaLista

lista2=so_pares(lista1)
print(lista2)
