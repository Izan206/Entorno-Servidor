a=int(input("Introduce o primer valor do intervalo: "))
b=int(input("Introduce o segundo valor do intervalo: "))
rango=range(a,b)

if (a<b):
    a=a
    b=b
elif (b<a):
    temp=a
    a=b
    b=temp
else:
    print("Error")
        
for i in rango:
    if (i%2==0):
        print(i)
        print()
    