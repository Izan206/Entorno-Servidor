a=int(input("Introduce un numero: "))
b=int(input("Introduce otro numero: "))
c=int(input("Introduce otro numero: "))

def comprobar_valores_iguais(num1, num2, num3):
    if (a==b or a==c or b==c):
        return True
    else:
        return False

def calcular_menor_numero(num1, num2, num3):
    if (a<b and a<c):
        return a
    elif (b<a and b<c):
        return b
    else:
        return c

if (comprobar_valores_iguais(a, b, c) is True):
    print("Error")
else:
    menor=calcular_menor_numero(a, b, c)
    print(f"El numero mas pequeño es {menor}")