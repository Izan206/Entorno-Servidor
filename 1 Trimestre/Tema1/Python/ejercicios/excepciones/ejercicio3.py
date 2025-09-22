def celsius_to_farenheit(celsius: float):
    fahr=(celsius*9/5)+32
    return fahr

try:
    param=float(input("Introduce la temperatura en celsius: "))
    if (param<0):
        raise Exception
    else:
        gradosFahr=celsius_to_farenheit(param)
        print(gradosFahr, "ºF")
except (ValueError):
    print("Error: Debe ser un numero")
except Exception:
    print("Error: Debe ser positivo")