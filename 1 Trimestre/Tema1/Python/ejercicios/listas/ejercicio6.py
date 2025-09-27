"""
Exercicio 6. Escribe unha función en Python piramide(lonxitude: int) que imprima unha pirámide de números. Esta recibe un enteiro que indica a lonxitude da pirámide.

Por exemplo se introducimos a lonxitude 5, imprimirase:

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
Utiliza a función range().
"""

longitud=int(input("Introduce la longitud de la piramide: "))

def piramide(lonxitud: int):
    for i in range(1, lonxitud+1):
        for x in range(1, i+1):
            print(x, end=' ')
        print()

piramide(longitud)