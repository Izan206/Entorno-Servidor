from csv import DictReader

def fila_to_dict(fila):
    dict=[]
    partes=fila["nome e apelido"].split()
    nome=fila[0]
    dict.append(nome)
    apelido=fila[1]
    dict.append(apelido)
    
    






lista=[]
with open("C:/Users/izan.alvarezvarela/dev/entorno-servidor/1 trimestre/tema1/python/ejercicios/ficheros2/data.csv", "r") as f:
    lector=DictReader(f)
    for fila in lector:
        partes=fila["nome e apelido"].split()
        apelido=partes[1]
        lista.append(apelido)

print(lista)