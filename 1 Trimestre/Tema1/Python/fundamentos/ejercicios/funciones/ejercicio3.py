año=int(input("Introduce un año: "))

def comprobar_bisiesto(año):
    if (año<0):
        print("Error")
    elif (año%4==0):
        if(año%100!=0):
            return True
        elif (año%100==0 and año%400==0):
            return True
        else:
            return False
    else:
        return False
    
if (comprobar_bisiesto(año) is True):
    print(f"{año} es bisiesto")
else:
    print(f"{año} no es bisiesto")