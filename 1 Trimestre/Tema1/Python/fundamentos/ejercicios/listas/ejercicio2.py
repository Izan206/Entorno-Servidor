"""
Exercicio 2. Escribe unha función en Python so_pares(lista: List) -> List que reciba unha lista de números e devolva unha nova lista que conteña só os números pares da lista orixinal.
"""

lista1=[1, 2, 3, 4, 5]


def so_pares(lista):
    nuevaLista=[]
    for num in lista1:
        if (num%2==0):
            nuevaLista.append(num)
    return nuevaLista

lista2=so_pares(lista1)
print(lista2)
