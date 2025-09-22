contador = 0
volverPedir = True
while volverPedir == True:
    try:
        num = int(input("Introduce un numero entero positivo: "))
        if num < 0:
            raise Exception
        else:
            contador += 1
            break
    except ValueError:
        print("Tiene que ser un numero, vuelvelo a intentar")
        contador += 1
        volverPedir = True

    except Exception:
        print("Tiene que ser mayor que 0, vuelvelo a intentar")
        contador += 1
        volverPedir = True

print(f"Lo has intentado {contador} veces")
