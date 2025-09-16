#Es tipado dinamico porque las variables pueden cambiar de tipo
cadena="Hola"
print(type(cadena))
cadena=3;
print(type(cadena))

#Es tipado forte porque no se pueden realizar operaciones entre variables de diferente tipo
x=10
y="mundo"

#z=x+y #Error

#NO se pueden hacer variables que empiecen por numeros ni con palabras reservadas como def, None
#def = 25 || 22izan=20


#Cada linea en python es una instruccion diferente, no hay ;

#Al dividir dos enteros el resultado va dar un float, si la division no es exacta se queda solo con la parte entera
entero1=20
entero2=4
div=entero1/entero2
print(div, type(div))

#None se usa para identificar alguna ausencia de definicion en una variable
variable_sin_valor=None
"""

"""

#Conjuntos y Tuplas

conjunto= {1, 2, 2, 3, 4 ,5} #si repites numeros la longitud es la misma 

print(len(conjunto))

#Conversion

num_float = 3.14
num_int = int(num_float) #de float a int

#Solicitud de datos al usuario, por defecto es un string asi que hay que convertirlo

dato=int(input("Introduce un numero: "))
print(dato)

#Uso de print(f)
nombre="Izan"
print(f"Mi nombre es {nombre}")

#Lineas en blanco
print()