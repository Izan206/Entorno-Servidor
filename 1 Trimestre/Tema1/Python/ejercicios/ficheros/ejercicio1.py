""" 
Exercicio 1. Lee o seguinte ficheiro CSV nun script de Python. O nome do ficheiro recibirase por argumento do script. Almacena os datos nunha lista de dicionarios. Imprime por pantalla unicamente o apelido de cada elemento (o campo “nome e apelido” tan só conta cun único e nome é un único apelido).

"""

import csv

with open("fichero.csv") as fichero:
    lector=csv.reader(fichero)
    for fila in lector:
        