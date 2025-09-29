"""
Exercicio 1. Escribe nun script unha función contar_frecuencia(lista: List[str]) -> Dict[str, int] que conte a frecuencia de cada palabra nunha lista de palabras. A función debe devolver un dicionario onde as chaves son as palabras e os valores son as frecuencias. Aquí tes un fragmento de código para probar dita función:
"""

from typing import Dict, List



def contar_frecuencia(lista: List[str]) -> Dict[str, int]:
    diccionario_palabras=dict()
    num_maza=0
    num_banana=0
    num_laranxa=0
    for i in lista:
        if i=="maza":
            num_maza+=1
            diccionario_palabras[i]=num_maza
        elif i=="banana":
            num_banana+=1
            diccionario_palabras[i]=num_banana
        elif i=="laranxa":
            num_laranxa+=1
            diccionario_palabras[i]=num_laranxa
            
    return diccionario_palabras
    
    
    
lista_palabras = ['maza', 'banana', 'maza', 'laranxa', 'banana', 'maza']

print(contar_frecuencia(lista_palabras))

#Debería devolver ["maza": 3, "banana": 2, "laranxa": 1]