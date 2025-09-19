#Para definir una funcion usamos la palabra reservada

def saludar(name: str) -> str: #Lo del str es orientativo
    print(f"Hola {name}")
    
saludar("Izan")

def saludar2(nombre, edad):
    print(f"Hola {nombre} tienes {edad} años")
    return True

x=saludar2("Izan", 19)

def incrementar(n):
 n+=1
 print("Dentro de la funcion: ",n)
 

numero=5
incrementar(numero)
print("Fuera de la funcion: ",numero) #devuelve 5 porque lo que se le pasa a la funcion incrementar se le pasa una copia de la memorua de la variable numero=5 diferente

#para guardarlo correctamente y que diese 6 fuera de la funcion tendrias que hacer :     numero=incrementar(numero)

def engadir_elemento(lista):
    lista.append(10)
    print("Dentro de la funcion: ",lista)

numeros=[1,2,3]
print(id(numeros))
engadir_elemento(numeros)
print("Fuera de la funcion: ",numeros)
#Aqui se pasa la referencia de memoria directamente y no se crea una copia como en el caso anterior que se pasaba por valor asi que cuando se invoca la funcion se modifica directamente la referencia de memoria y el resultado sera el mismo dentro y fuera de la funcion



#RETORNO DE VALORES
#Se pueden devolver varior valores en cada funcion en forma de tupla

def operar(a,b):
    suma=a+b
    resta=a-b
    return suma, resta

suma, resta=operar(4, 2)
print("Suma: ",suma)
print("Resta: ", resta)

#Early returns

def dividir(a, b):
    if b==0:
        return "Error matematico"
    if (b<0 or a<0):
        return "Solo numeros positivos"
    
    return a/b