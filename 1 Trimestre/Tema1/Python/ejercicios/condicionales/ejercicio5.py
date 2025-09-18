a=int(input("Introduce un numero por teclado: "))
b=int(input("Introduce otro numero por teclado: "))
c=int(input("Introduce otro numero por teclado: "))
if(a==b or b==c or a==c):
    print("Error")
elif(a>b and a>c):
    print(f"{a} es el mayor de los tres")
elif(b>a and b>c):
    print(f"{b} es el mayor de los tres")
else:
    print(f"{c} es el mayor de los tres")
