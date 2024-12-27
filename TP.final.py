import csv

def cargar_datos(archivo):
  
    with open(archivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def filtrar_por_edad(datos, edad_min, edad_max):
    
    return [persona for persona in datos if edad_min <= int(persona['edad']) <= edad_max]

def buscar_por_campo(datos, campo, valor):
 
    return [persona for persona in datos if persona[campo].lower() == valor.lower()]

def guardar_resultados(datos, archivo):
    
    if datos:
        with open(archivo, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=datos[0].keys())
            writer.writeheader()
            writer.writerows(datos)
        print(f"Resultados guardados en {archivo}.")
    else:
        print("No hay datos para guardar.")

def mostrar_menu():
   
    print("\nMenú de opciones:")
    print("1. Filtrar por rango de edades")
    print("2. Buscar por nombre")
    print("3. Buscar por ciudad")
    print("4. Guardar resultados en un archivo")
    print("5. Salir")

def main():
    datos = cargar_datos('datos.csv')
    resultados = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            edad_min = int(input("Ingrese la edad mínima: "))
            edad_max = int(input("Ingrese la edad máxima: "))
            resultados = filtrar_por_edad(datos, edad_min, edad_max)
            print("\nResultados:")
            for persona in resultados:
                print(persona)

        elif opcion == '2':
            nombre = input("Ingrese el nombre a buscar: ")
            resultados = buscar_por_campo(datos, 'nombre', nombre)
            print("\nResultados:")
            for persona in resultados:
                print(persona)

        elif opcion == '3':
            ciudad = input("Ingrese la ciudad a buscar: ")
            resultados = buscar_por_campo(datos, 'ciudad', ciudad)
            print("\nResultados:")
            for persona in resultados:
                print(persona)

        elif opcion == '4':
            archivo = input("Ingrese el nombre del archivo para guardar (con extensión .csv o .txt): ")
            guardar_resultados(resultados, archivo)

        elif opcion == '5':
            print("Saliendo del programa.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

