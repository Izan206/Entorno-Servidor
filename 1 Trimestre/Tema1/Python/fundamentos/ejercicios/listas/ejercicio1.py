"""
Exercicio 1. Crea un script no que se ingresen as notas de alumnos. Vai gardando todas as notas que están entre 0 e 10 nunha lista. Cando o usuario introduza a palabra “fin”, non se pediran máis notas. Ao finalizar o ingreso de notas mostra por pantalla a media de todas as notas.
"""

listaNotas=[]
continuarPidiendo=True
suma=0
contadorNotas=0
while continuarPidiendo==True:
    notas=input("Introduce una nota o di fin para terminar: ")
    if (notas=="fin"):
        continuarPidiendo=False
    elif (notas.isdigit()):
        nota=float(notas)
        if (0<=nota<=10):
            listaNotas.append(nota)
            suma+=nota
            contadorNotas+=1
        else:
            print("La nota debe estar entre 0 y 10")
            continue
media=suma/contadorNotas
print(f"Las notas son: {listaNotas}")
print("La media da: ",media)