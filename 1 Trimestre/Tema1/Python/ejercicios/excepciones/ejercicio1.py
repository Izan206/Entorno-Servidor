try:
    a=int(input("Introduce un numero: "))
    b=int(input("Introduce otro numero: "))
    resultado=a/b
except(ZeroDivisionError):
    print("Erro: Non se pode dividir entre cero")
except(ValueError):
    print("Entrada non válida, por favor introduce números.")
else:
    print("Resultado: ",resultado)
    
    