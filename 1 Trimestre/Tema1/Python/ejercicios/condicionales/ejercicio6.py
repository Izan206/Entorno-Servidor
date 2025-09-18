a=int(input("Introduce un numero por teclado: "))
b=int(input("Introduce otro numero por teclado: "))

if (a%b==0):
    print(f"{b} e divisor de {a}")
elif (b%a==0):
    print(f"{a} e divisor de {b}")
else:
    print("Ninguno es divisor del otro")