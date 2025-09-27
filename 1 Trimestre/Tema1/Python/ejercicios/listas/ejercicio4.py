""" 
Exercicio 4. Escribe unha función en Python contar_lonxitudes(lista: List) -> List que reciba unha lista de palabras e devolva unha lista coa lonxitude de cada palabra.
"""

from typing import List


lista=["Hola", "mundo", "soy", "Izan"]

def contar_lonxitudes(lista: List) -> List:
    nuevaLista=[]
    longitudPalabra=0
    for palabra in lista:
        longitudPalabra=len(palabra)
        nuevaLista.append(longitudPalabra)
    
    return nuevaLista

print(contar_lonxitudes(lista))