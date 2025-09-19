num=int(input("Introduce el numero: "))

def comprobar_par(numero):
    if (numero%2==0):
        return True
    else:
        return False

if (comprobar_par(num) is True):
    print(f"{num} es par")
else:
    print(f"{num} es impar")