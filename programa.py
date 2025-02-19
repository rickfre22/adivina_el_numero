import random
n=int(input("escribe un numero y intenta adivinar:"))
cpu=random.randint(1,100)
i=1
while n!=cpu:
    if n<cpu:print("el numero es mayor")
    else:
        print("el numero es menor")
    n=int(input("escribe un numero otra vez: "))
    i=i+1

print("---adivinaste---")
print(f"numero de intentos: {i}")

