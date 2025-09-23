cadena=input("Introduce una cadena: ")
nuevaCadena=""
for i in range(len(cadena)):
    letra=cadena[i]
    if (letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u'):
        nuevaCadena+=letra
    elif (letra.isnumeric or letra.isspace):
        nuevaCadena+=letra
    else:
        nuevaCadena=nuevaCadena
print(nuevaCadena)