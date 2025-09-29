from aritmeticas import suma, resta, multiplicacion
from comparacions import maior_que, menor_que


num1=int(input("Introduce un numero: "))
num2=int(input("Introduce otro numero: "))

menu="""
=== Menú de operacións ===
1. Sumar
2. Restar
3. Multiplicar
4. ¿É maior?
5. ¿É menor?
"""
print(menu)
opcion=int(input("Introduce una opcion: "))
if (opcion==1):
    print(suma(num1, num2))
elif opcion==2:
    print(resta(num1, num2))
elif opcion==3:
    print(multiplicacion(num1,num2))
elif opcion==4:
    print(maior_que(num1, num2))
elif opcion==5:
    print(menor_que(num1, num2))
else:
    print("Opcion incorrecta")