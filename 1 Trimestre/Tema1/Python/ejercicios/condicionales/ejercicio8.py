numero1 = int(input("Introduce un numero: "))
numero2 = int(input("Introduce otro numero: "))
menu = input("""
MENU
    a) sumar dos numeros
    b) restar dos numeros
    c) multiplicar dos numeros

Elige: """)
if (menu == "a"):
    suma=numero1+numero2
    print(f"La suma da {suma}")
elif (menu=="b"):
    resta=numero1-numero2
    print(f"La resta da {resta}")
elif (menu=="c"):
    multi=numero1*numero2
    print(f"La multiplicacion da {multi}")
else:
    print("Opcion incorrecta")