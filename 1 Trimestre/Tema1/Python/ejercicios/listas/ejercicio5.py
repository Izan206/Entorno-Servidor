"""
Exercicio 5. Escribe unha función en Python coller_comúns(lista1: List, lista2: List) -> List que reciba dúas listas e devolva unha lista cos elementos comúns.
"""

from typing import List


lista1=[1, 2, 3, 4, 5, 5, 6]
lista2=[10, 9, 8, 7, 6, 5]

def coller_comuns(lista, lista2) -> List:
    nuevaLista=[]
    for elemento1 in lista:
        for elemento2 in lista2:
            if elemento1==elemento2 and elemento1 not in nuevaLista:
                nuevaLista.append(elemento1)

    return nuevaLista

print(coller_comuns(lista1, lista2))