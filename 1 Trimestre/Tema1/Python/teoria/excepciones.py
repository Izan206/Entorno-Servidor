temp=input("Introduzca a temperatura fahrenheit: ")
try:
    fahr=float(temp)
    celsius=(fahr-32.0)*5.0/9-0
    print(celsius)
except:
    print("Por favor, introduza un numero")
    
#Si quiero capturar una excepcion especifica


def funcion_a():
    try:
        funcion_b
    except:
        print("Error de compilacion en A")