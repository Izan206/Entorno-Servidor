def suma(*args):
    suma=0
    for num in args:
        suma+=num
    print(args)
    
suma(1, 2, 4, 6, 10) #Por si queremos pasar un numero indefinido de valores

#Para pasar parametros como clave valor

def suma2(**kwargs):
    for chave, valor in kwargs.items():
        print(chave, " : ", valor)
        
suma2(chave="Izam", apellidos="Alvarez")