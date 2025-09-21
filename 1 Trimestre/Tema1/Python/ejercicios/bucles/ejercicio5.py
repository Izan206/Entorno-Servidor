a=int(input("Introduce o primer valor do intervalo: "))
b=int(input("Introduce o segundo valor do intervalo: "))

if a==b:
    print("Error")
else:
    if a>b:
        a, b=b, a

    for i in range(a, b):
        if (i%2==0):
            print(i)
    