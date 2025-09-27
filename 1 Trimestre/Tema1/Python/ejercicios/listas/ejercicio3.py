""" 
Exercicio 3. Escribe unha función en Python eliminar_duplicados(lista: List) -> List que reciba unha lista con elementos duplicados e devolva unha nova lista sen duplicados, mantendo a orde orixinal.
"""
lista1=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

def eliminar_duplicados(lista):
    nuevaLista=[]
    for num in lista:
        if num not in nuevaLista:
            nuevaLista.append(num)
    return nuevaLista

lista2=eliminar_duplicados(lista1)
print(lista2)