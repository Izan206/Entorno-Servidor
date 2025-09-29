año=int(input("Introduce el año: "))
if (año<0):
    print("Error")
elif (año%4==0):
    if (año%100!=0):
        print(f"{año} es bisiesto")
    elif (año%100==0 and año%400==0):
        print(f"{año} es bisiesto")
    else:
        print(f"{año} no es bisiesto")
else:
    print(f"{año} no es bisiesto")
    