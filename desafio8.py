notas = []

print("Ingrese las notas de los exámenes una por una. Ingrese 0 para finalizar la carga.")

while True:
    try:
        nota = float(input("Ingrese una nota (0-10): "))

        if nota == 0:
            break

        if 0 < nota <= 10:
            notas.append(nota)
        else:
            print("Por favor, ingrese una nota válida entre 0 y 10.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")

if notas:
    print("\nLas notas ingresadas son:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
else:
    print("No se ingresaron notas.")
 
   