N=int(input("Introduce un numero entero positivo: "))
rango=range(1,N+1)
if (N<0):
    print("Tiene que ser positivo")
else:
    print(f"Numero de pares entre 1 y {N}")
    for i in rango:
        if i%2==0:
            print(i)
    
    print()

    print(f"Numero de impares entre 1 y {N}")
    for i in rango:
        if i%2!=0:
            print(i)

    print()

    print(f"Suma de todos los numeros entre 1 y {N} ")
    suma=0
    for i in rango:
        suma+=i
    
    print(f"La suma da {suma}")
    print()

    print(f"Media de los numeros pares entre 1 y {N}")
    suma=0
    for i in rango:
        if (i%2==0):
            suma+=i
    media=suma/N
    print(f"La media da {media}")