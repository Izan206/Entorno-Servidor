froita="Banana"


#son inmutables, no puedes cambiar letras asi como asi
#cadena[0]="a" -> error

for i in range(len(froita)):
    print(froita[i])
    
    
#slicing
s="Hola python"
print(s[0:4]) # seria lo mismo print(s[:4])
print(s[5:11])

#tambiem sirve para crear un clon
cadena=s[:]
print(cadena)

#o cogerletras determinadas
print(s[0:10:2]) #de la 0 a la 10 de 2 en 2

