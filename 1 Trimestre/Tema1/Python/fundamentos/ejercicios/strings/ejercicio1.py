cadena=input("Introduce una cadena: ")
contadorVocal=0
for i in cadena.lower():
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        contadorVocal+=1
        
print(f"La cadena {cadena} tiene {contadorVocal} vocales")
        