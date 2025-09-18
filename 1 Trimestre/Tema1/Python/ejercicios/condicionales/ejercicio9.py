km_recorridos=float(input("Introduce los km recorridos: "))
menu = input("""
MENU
    a) Moto: importe fixo de 1€
    b) Turismo: 0,25€ por km recorrido
    c) Camión: 0,25€ por km más 0,15€ por tonelada de peso

Elige: """)

if (menu=="a"):
    precio=1*km_recorridos
    print(f"Vas a pagar: {precio}€")
elif (menu=="b"):
    precio=0.25*km_recorridos
    print(f"Vas a pagar: {precio}€")
elif (menu=="c"): 
    peso=float(input("Introduce el peso de tu camion: "))
    precio=0.25*km_recorridos+0.15*(peso*1000)
    print(f"Vas a pagar: {precio}€")
else:
    print("Opcion incorrecta")