""" 
Exercicio 1. Lee o seguinte ficheiro CSV nun script de Python. O nome do ficheiro recibirase por argumento do script. Almacena os datos nunha lista de dicionarios. Imprime por pantalla unicamente o apelido de cada elemento (o campo “nome e apelido” tan só conta cun único e nome é un único apelido).

"""

"""
Exercicio 2. A partir do exercicio anterior, crea unha función fila_to_dict(fila) que a partir de cada fila cree un dicionario cas seguintes claves:

“nome”: tan só o nome. Sen apelidos.

“apelido”: tan só o apelido. Sen o nome.

“dni”: o DNI pero ca letra en maiúscula.

“data_contrato”: a data do contrato pero como tipo de dato datetime.

“soldo_bruto_mensual”: o soldo bruto mensual como un float.

“IRPF”: o dato d entrada está proporcionado nun valor porcentual e deberemos almacenalo como un float, polo que debemos dividir o seu valor entre 100.

NOTA: elimina todos os espazos en branco de cada valor tanto ao comezo como ao final.

Proba a utilizar dita función na lectura do ficheiro realizada no exercicio anterior imprimindo cada dicionario.
"""

import csv
import datetime


def fila_to_dict(fila):
    partes = fila["nome e apelido"].strip().split()
    nome = partes[0]
    apelido = partes[1]
    dni = fila["dni"].strip().upper()
    data_contrato = datetime.datetime.strptime(
        fila["data contrato"].strip(), "%d-%m-%Y %H:%M")
    soldo_bruto_mensual = float(fila["soldo mensual bruto"].strip())
    IRPF = float(fila["IRPF"].strip()) / 100

    diccionario = {
        "nome": nome,
        "apelido": apelido,
        "dni": dni,
        "data_contrato": data_contrato,
        "soldo_bruto_mensual": soldo_bruto_mensual,
        "IRPF": IRPF
    }
    return diccionario

lista=[]

with open("C:/Users/Usuario/downloads/dev/entorno-servidor/1 trimestre/tema1/Python/ejercicios/ficheros/fichero.csv", "r", encoding="utf-8") as f:
    lector = csv.DictReader(f) 
    for fila in lector: 
        partes = fila["nome e apelido"].split() 
        apellido = partes[1] 
        print(apellido) 
        lista.append(apellido) 
        print(fila_to_dict(fila))
        
    print(lista)
    
