""" 
Exercicio 2. Escribe nun script unha función valor_maximo(dicionario: Dict[str, int]) -> List[str] que devolva as chaves asociadas ao valor máximo nun dicionario. Devolve unha lista con todas as claves que teñan ese valor. Aquí tes un fragmento de código para probar a función:
"""

from typing import Dict, List


def valor_maximo(dicionario: Dict[str, int]) -> List[str]:
    valor_maximo=None
    claves= []
    for clave, valor in dicionario.items():
        if valor_maximo is None or valor>valor_maximo:
            valor_maximo=valor
            claves=[clave]
        elif valor==valor_maximo:
            claves.append(clave)
            
    return claves
dicionario = {'a': 5, 'b': 3, 'c': 5, 'd': 2}

print(valor_maximo(dicionario))
# Saída esperada: ['a', 'c']