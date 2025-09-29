def decorador(funcion_b):
    def funcion_c(*args, **kwargs):
        print('Antes de la ejecucion de la funcion a decorar')
        funcion_b(*args, **kwargs)
        print('Despues de la ejecucion de la funcion a decorar')
        
    return funcion_c
        
@decorador
def saludar(nombre):
    print("Hola mundo!!", nombre)
    
saludar("Izan")