cantidad_alumnos=int(input("Cuantos alumnos realizaron el examen: "))
contadorAprobados=0
contadorSuspensos=0
rango=range(1, cantidad_alumnos+1)
for i in rango:
    nota=float(input(f"Introduce la nota del alumno {i}: "))
    if (nota>=5):
        contadorAprobados+=1
    else:
        contadorSuspensos+=1
    nota=0

print(f"La cantidad de alumnos aprobados es de {contadorAprobados}")
print(f"La contador de alumnos suspensos es de {contadorSuspensos}")