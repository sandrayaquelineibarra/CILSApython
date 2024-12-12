max_num = -1

print("Ingrese números enteros positivos uno por uno. Ingrese 0 para finalizar.")

while True:
    try:
        num = int(input("Ingrese un número: "))

        if num == 0:
            break

        if num > 0:
            if num > max_num:
                max_num = num
        else:
            print("Por favor, ingrese solo números enteros positivos.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número entero positivo.")

if max_num > -1:
    print(f"El número más grande ingresado es: {max_num}")
else:
    print("No se ingresaron números positivos.")
  