alumnos = {}

while True:
    try:
     
        nombre = input("Ingrese el nombre del alumno o escriba 'salir' para terminar: ")
        if nombre.lower() == "salir":
            break

        
        nota = float(input(f"Ingrese la nota de {nombre}: "))

        
        alumnos[nombre] = nota

    except ValueError:
        print("Error: Debe ingresar un número válido para la nota.")


aprobados = {nombre: nota for nombre, nota in alumnos.items() if nota >= 6}
desaprobados = {nombre: nota for nombre, nota in alumnos.items() if nota < 6}


print("\nAlumnos aprobados:")
for nombre, nota in aprobados.items():
    print(f"{nombre}: {nota}")
print("\nAlumnos desaprobados:")
for nombre, nota in desaprobados.items():
    print(f"{nombre}: {nota}")


