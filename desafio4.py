numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))


if numero2 != 0:  
    if numero1 % numero2 == 0:
        print(f"{numero1} es múltiplo de {numero2}.")
    else:
        print(f"{numero1} no es múltiplo de {numero2}.")
else:
    print("El segundo número no puede ser cero.")