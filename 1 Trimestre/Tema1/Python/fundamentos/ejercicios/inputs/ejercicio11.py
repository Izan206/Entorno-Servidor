salario_bruto = float(input("Introduce tu salario bruto: "))
irpf = float(input("Introduce el IRPF: "))
salario_neto=salario_bruto-(salario_bruto*(irpf/100))
print(f"El salario neto es: {salario_neto}")